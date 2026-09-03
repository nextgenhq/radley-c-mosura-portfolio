# Architecture Overview

## System Architecture: 4-Phase SME AI Factory

```
┌─ Telegram Bot (/build <Client>) ────────────────────────────────┐
│                                                                   │
├─ PHASE 1: RESEARCHER (Gemini Flash)                             │
│  → web-grounded research → research/dossier.md                  │
│                                                                   │
├─ PHASE 2: CMO (Ollama qwen3.5:9b)                               │
│  → marketing/brief.md + 5 FB posts + 3 IG captions + calendar   │
│                                                                   │
├─ PHASE 3: CTO (Ollama qwen2.5-coder:14b)                        │
│  → Clone sme-landing-template                                   │
│  → Write brand.config.ts + src/content/client/*.md              │
│  → Run cto-deploy.sh → D1 + CF Pages secret setup + wrangler    │
│  → Output: live site at https://{slug}.nextgenai.ph             │
│                                                                   │
├─ PHASE 4: COO (Ollama qwen3.5:9b)                               │
│  → operations/alignment.md + Trello tasks for physical team     │
│                                                                   │
└─ Integrations: Trello (pipeline + ops), CF Pages, FB Graph API ─┘
```

## BigQuery Agent Architecture

```
User Input (Natural Language)
         ↓
  LangGraph ReAct Loop
         ↓
  [Thought] ← System Prompt + Schema Context
         ↓
  [Action] → LangChain Tool Execution
         ↓
  SQL Generation + BigQuery Execution
         ↓
  [Observation] ← Raw Query Results (6,000+ leads)
         ↓
  [Thought] → Synthesis & Summarization
         ↓
Natural Language Business Insight
```

## Infrastructure as Code (Terraform)

**GCP Resources Provisioned:**

- **Google Cloud Storage:** `project-abcf14c5-raw-leads-bucket` (raw data ingestion)
- **BigQuery Dataset:** `leads_analytics` (structured warehouse)
- **BigQuery Table:** `leads_analytics.raw_leads` (6,000+ B2C records with schema)
- **IAM Service Account:** Restricted tool execution scopes, PII masking policies

**Configuration Lifecycle:**

1. Define resources in `main.tf`
2. Run `terraform init` → initialize GCP backend
3. Run `terraform plan` → validate resource graph
4. Run `terraform apply` → provision or update
5. **Zero drift:** All future updates declarative only

## Cloudflare D1 + Pages Deployment Pipeline

```
Local Development
         ↓
cto-deploy.sh (Automated Script)
         ├─ Build validation (Astro compile)
         ├─ Test suite (142 tests)
         ├─ Lighthouse CI (≥95 score)
         ├─ Copy linting
         ├─ D1 database creation ({slug}-leads)
         ├─ wrangler.toml template generation
         ├─ CF Pages secret injection
         └─ wrangler deploy → live
         ↓
https://{slug}.nextgenai.ph (Live Production)
```

## Local → Cloud Failover Routing

**Primary:** Ollama models (qwen2.5-coder, qwen3.5) running locally on Mac Studio M2 Ultra

**Fallback:** GCP Vertex AI / Gemini 2.5 Flash endpoints

**Routing Logic:**
- Try local Ollama first (latency <1s, zero cost)
- On timeout or rate limit → switch to Gemini Flash
- Log routing decisions for observability

---

## Scale & Performance Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Agent Latency | <2.5s | SQL generation + BigQuery execution |
| Deployment Time | ~5 min | Full-stack SME site (template → live) |
| Data Records | 6,000+ | B2C leads in BigQuery warehouse |
| CI/CD Tests | 142 | Build-time + Lighthouse + linting |
| Active Clients | 4 | ERBC, Dila, IMC, Meridian |
| Monthly Recurring | ₱20,998 | ERBC + IMC + performance fees |
