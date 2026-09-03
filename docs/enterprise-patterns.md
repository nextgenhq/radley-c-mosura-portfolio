# Enterprise Architecture Patterns & Compliance

## RA 10173 (Philippine Data Privacy Act) Compliance Framework

### Implementation Layers

**1. Data Classification & PII Detection**
```
Customer Input
     ↓
[Google Cloud DLP Classification]
     ↓
├─ PII Fields: Names, emails, phone, SSN, medical history
├─ Quasi-Identifiers: Age, location, occupation
└─ Non-Sensitive: Product preferences, feedback
     ↓
Route based on sensitivity level
```

**2. PII Masking Strategy**
```python
# Before external model routing
sensitive_fields = ['phone', 'email', 'name', 'address']

def mask_pii(data: dict) -> dict:
    masked = data.copy()
    for field in sensitive_fields:
        if field in masked:
            masked[field] = f"[REDACTED_{field.upper()}]"
    return masked

# Send masked data to Gemini Flash for processing
response = gemini_client.process(mask_pii(lead_record))
```

**3. Access Control & IAM Roles**
- **Service Account (Tool Execution):** Scoped to BigQuery `leads_analytics` dataset only
- **Admin Portal Users:** Role-based access (Viewer, Editor, Admin)
- **API Keys:** Environment-based rotation, no hardcoded secrets
- **Audit Trail:** All data access logged with timestamp, user, action

**4. Data Retention & Deletion**
- **Leads:** 12-month retention (per contract)
- **Audit Logs:** 24-month retention
- **Deletion:** On-demand customer request + automated archive to Cold Storage

---

## Deterministic Schema Validation (Vertex AI Function Calling + Zod)

### Problem: LLM Math Hallucination
Raw LLM outputs can contain calculation errors. For financial systems, this is unacceptable.

### Solution: Enforced Structured Output

**1. Define Schema with Zod**
```typescript
import { z } from 'zod';

const LeadScoreSchema = z.object({
  lead_id: z.string().uuid(),
  engagement_score: z.number().min(0).max(100),
  conversion_probability: z.number().min(0).max(1),
  recommended_tier: z.enum(['bronze', 'silver', 'gold', 'platinum']),
  calculations_shown: z.string().describe('Show math for auditability')
});

type LeadScore = z.infer<typeof LeadScoreSchema>;
```

**2. Bind Schema to Vertex AI Function Calling**
```python
# LLM is constrained to output only valid schema
response = vertex_ai_client.predict(
    prompt="Score this lead based on engagement metrics...",
    tools=[
        {
            "name": "calculate_lead_score",
            "input_schema": zod_to_openapi_schema(LeadScoreSchema)
        }
    ]
)

# Automatically parse and validate response
parsed = LeadScoreSchema.parse(response.tool_use[0].input)
```

**3. Auditability**
- Store raw LLM output + final validated output
- Include calculation steps (LLM-generated "show your work")
- Fail safely: if schema validation fails, escalate to human review

---

## WebSocket Relay Architecture (Real-Time Team Sync)

### Use Case: ERBC Broker Dashboard
Brokers need real-time updates when new leads arrive. Ollama code generation shouldn't block the dashboard.

### Architecture

```
┌─ Background Worker (Ollama qwen2.5-coder)
│  └─ Generates new lead form code
│     └─ Posts to WebSocket relay
│
┌─ WebSocket Relay Hub (Node.js)
│  └─ Receives message
│  └─ Broadcasts to all connected clients
│
├─ ERBC Dashboard (Astro + React)
│  └─ Listens on WebSocket
│  └─ Renders new lead form in real-time
│
└─ Supervisor Admin Panel
   └─ Monitors background queue
   └─ Can pause/resume workers
```

### Implementation

**Relay Server (Express + ws)**
```typescript
const WebSocket = require('ws');
const app = require('express')();
const http = require('http').createServer(app);
const wss = new WebSocket.Server({ server: http });

const clients = new Set();

wss.on('connection', (ws) => {
  clients.add(ws);
  ws.on('message', (message) => {
    // Broadcast to all clients
    clients.forEach(client => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  });
  ws.on('close', () => clients.delete(ws));
});

http.listen(3000);
```

**Background Worker (Python)**
```python
import websocket
import json

def send_relay(event_type: str, data: dict):
    ws = websocket.create_connection('ws://relay:3000')
    payload = json.dumps({
        'type': event_type,
        'timestamp': datetime.now().isoformat(),
        'data': data
    })
    ws.send(payload)
    ws.close()

# After Ollama completes code generation
send_relay('form_generated', {
    'client_id': 'erbc',
    'form_name': 'lead_intake_v2',
    'html': generated_html
})
```

**Dashboard Listener (Astro + React)**
```tsx
useEffect(() => {
  const ws = new WebSocket('wss://relay.nextgenai.ph');
  
  ws.onmessage = (event) => {
    const { type, data } = JSON.parse(event.data);
    
    if (type === 'form_generated') {
      setFormHTML(data.html);
      showNotification(`New form available: ${data.form_name}`);
    }
  };
  
  return () => ws.close();
}, []);
```

---

## Sub-3.8-Second Speed-to-Lead Pipeline

### Challenge
Philippine retail clients expect SMS/Viber notifications within seconds of a lead form submission.

### Architecture

```
Lead Submission (Client Site)
     ↓
[Cloudflare D1 INSERT]  ← ~50ms
     ↓
[Webhook Trigger]
     ↓
[SMS/Viber Gateway]  ← ~200ms (carrier)
     ↓
[Broker Phone Alert]
     ↓
Total: <3.8 seconds
```

### Implementation

**1. Webhook on D1 INSERT (Wrangler Trigger)**
```toml
# wrangler.toml
[[d1_databases]]
name = "leads"
binding = "DB"
database_name = "erbc-leads"

# Automatic webhook on INSERT
[[triggers.d1]]
database_binding = "DB"
events = ["create"]
handler = "trigger_lead_notification"
```

**2. Edge Function (Cloudflare Workers)**
```typescript
export async function onRequest(context) {
  const { request, env } = context;
  const lead = await request.json();

  // Send to Viber + SMS in parallel
  const viber = env.VIBER_API.post('/send', {
    phone: lead.broker_phone,
    message: `New lead: ${lead.name}, ${lead.city}`
  });

  const sms = env.SMS_API.post('/send', {
    recipient: lead.broker_phone,
    body: `Lead: ${lead.name}`
  });

  await Promise.all([viber, sms]);
  return new Response('OK', { status: 200 });
}
```

**3. Rate Limiting & Retry Logic**
```python
# Prevent SMS/Viber spam
rate_limiter = RateLimiter(
    max_leads_per_broker=50,  # per hour
    cooldown=10  # seconds between notifications
)

# Exponential backoff on failure
@retry(max_attempts=3, backoff_factor=2)
async def send_notification(broker_id, lead_data):
    try:
        await viber_client.send(broker_id, lead_data)
    except Exception as e:
        logger.error(f"Notification failed for {broker_id}: {e}")
        raise
```

---

## ALCOA+ Compliance (IMC Laboratory)

### What is ALCOA+?
**Attributable, Legible, Contemporaneous, Original, Accurate** + **complete, consistent, enduring, available**

Required for pharmaceutical/medical device calibration records.

### Implementation in IMC System

**1. Attributable**
- Every record linked to technician via unique ID
- Digital signature (not just username)
- Cannot be reassigned post-creation

```typescript
const calibrationRecord = {
  id: uuid(),
  calibration_date: new Date(),
  technician_id: currentUser.id,
  technician_signature: generateDigitalSignature(currentUser.private_key),
  equipment_sn: 'SPEC-12345',
  measurements: [...]
};
```

**2. Legible**
- All data stored as plain text or standard formats (no proprietary binary)
- Audit trail in human-readable format

```sql
CREATE TABLE audit_trail (
  id UUID PRIMARY KEY,
  record_id UUID NOT NULL,
  action VARCHAR(50),
  old_value TEXT,
  new_value TEXT,
  timestamp TIMESTAMPTZ NOT NULL,
  user_id UUID NOT NULL
);
```

**3. Contemporaneous**
- Timestamp at time of record creation (server time, not client)
- Cannot backdate or edit timestamp

```python
def create_calibration_record(data):
    record = {
        **data,
        created_at: datetime.utcnow(),  # Server time, immutable
        created_by: current_user.id
    }
    db.calibrations.insert_one(record)
```

**4. Original**
- Original record preserved immutably
- All changes tracked via audit log (no direct edits)

```python
async def update_calibration(record_id, changes):
    # Get original
    original = await db.calibrations.find_one({'_id': record_id})
    
    # Create audit entry (not an update)
    audit_entry = {
        record_id: record_id,
        original_values: original,
        new_values: changes,
        timestamp: datetime.utcnow(),
        user_id: current_user.id,
        reason: request.body.reason
    }
    
    await db.audit_trail.insert_one(audit_entry)
    # Original record stays unchanged
```

**5. Accurate**
- Calculations validated (Zod schema, double-entry verification)
- Cross-check against equipment specs

```typescript
async function validateCalibrationData(measurement: MeasurementInput) {
  const equipment = await getEquipmentSpecs(measurement.equipment_sn);
  
  // Check measurement is within tolerance
  if (measurement.reading > equipment.max_tolerance) {
    throw new Error(`Reading exceeds equipment max tolerance`);
  }
  
  // Double-entry: second technician must verify
  measurement.verified_by = null;  // Requires second signature
}
```

**6. Complete**
- All required fields present
- No missing data accepted

**7. Consistent**
- Same units across records (no mixing metric/imperial)
- Standardized formats

**8. Enduring**
- Long-term data preservation (audit logs kept 7+ years)
- Migration path for format changes

**9. Available**
- Records accessible within 24 hours
- Export capability (PDF with digital signatures)

---

## Local Ollama → Cloud Failover Routing

### Rationale
- **Local:** Sub-1s latency, zero token cost, full control
- **Cloud:** Reliable, scalable, handles demand spikes

### Implementation

```python
async def route_to_llm(prompt: str, model: str = "qwen2.5-coder:14b"):
    """Route with intelligent failover"""
    
    # Step 1: Try local Ollama
    try:
        response = await ollama_client.generate(
            model=model,
            prompt=prompt,
            timeout=5  # Fail fast
        )
        logger.info(f"Local Ollama succeeded ({response.duration}ms)")
        return response
    
    except asyncio.TimeoutError:
        logger.warning("Local Ollama timeout, falling back to Gemini")
    except Exception as e:
        logger.warning(f"Local Ollama error: {e}")
    
    # Step 2: Fallback to Gemini
    try:
        response = await gemini_client.generate_content(
            prompt=prompt,
            safety_settings=SAFETY_SETTINGS,
            temperature=0.0  # Deterministic for code
        )
        logger.info("Gemini fallback succeeded")
        return response
    
    except Exception as e:
        logger.error(f"All LLM routes failed: {e}")
        raise LLMServiceError("Unable to reach any LLM endpoint")

# Track routing decisions for observability
routing_metrics = {
    'ollama_success': 0,
    'ollama_timeout': 0,
    'gemini_fallback': 0,
    'total_failures': 0
}
```

### Metrics & Monitoring

- **Local Success Rate:** Target ≥95%
- **Fallback Rate:** Track to identify homelab capacity issues
- **Total Latency:** <3s across all routes
- **Cost:** Local usage tracked, cloud usage tagged per client

---

## Conclusion

These patterns ensure that NextGen AI platforms are:
- **Legally Compliant:** RA 10173, ALCOA+ audit trails
- **Performant:** <3.8s speed-to-lead, <2.5s analytics queries
- **Reliable:** Automated failover, deterministic validation
- **Observable:** Comprehensive audit logs and routing metrics
