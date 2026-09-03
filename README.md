# 🚀 Radley C. Mosura — AI Systems Architect & Technical Lead

**Full-Stack Infrastructure Engineer | Enterprise LLM & Agentic Systems | 9+ Years | Multi-Tenant Cloud & Local AI**

*Architecting production-grade AI agent systems, enterprise data pipelines, and automated infrastructure. From cloud databases to local Ollama homelabs. From zero-token-cost automation to ₱20,998/mo MRR SaaS platforms.*

---

## 📌 Professional Identity

**Systems Architect & Technical Lead** specializing in:
- **Enterprise AI Infrastructure:** Google Cloud Vertex AI + Gemini models integrated with local LLM execution (Ollama/MLX, Qwen, Llama)
- **Agentic Pipeline Architecture:** LangGraph + LangChain for autonomous SQL agents, document parsing, and multilingual extraction
- **Multi-Tenant Cloud Backends:** BigQuery integration, schema ingestion, low-latency query execution
- **Local Automation Engines:** Zero-token-cost background daemons, cron jobs, WebSocket relays, system administration
- **Data Privacy & Compliance:** RA 10173 (Philippine Data Privacy Act), Google Cloud DLP, PII masking, deterministic schema validation
- **Speed-to-Lead Automation:** Sub-3.8-second webhook pipelines (Viber/SMS/WhatsApp), high-converting landing funnels
- **Full-Stack Delivery:** Claude Code, OpenAI Codex, Antigravity 2.0 for rapid codebase prototyping and refactoring

---

## 🎯 Featured Systems & Architectures

### 1. Enterprise Lead Analytics Agent (BigQuery + LangGraph + Terraform)

**Type:** Production AI Data Infrastructure

**Role:** Architect, Lead Engineer

**Tech Stack:** Python, LangGraph, LangChain Core, Google BigQuery, Gemini 2.5 Flash, Terraform, Streamlit

**Overview:** Enterprise-grade natural language analytics agent enabling non-technical stakeholders to query 6,000+ B2C lead records via natural language.

**Key Contributions:**

* **Infrastructure as Code (Terraform):** Provisioned GCP storage buckets (`project-abcf14c5-raw-leads-bucket`), BigQuery datasets (`leads_analytics.raw_leads`), and IAM service account security policies. **Zero infrastructure drift.**
* **Dynamic Schema Pre-Fetching:** Solved LLM hallucination by auto-ingesting exact datatypes and column definitions into system prompt at startup.
* **LangGraph ReAct Loop:** Autonomous reasoning with `create_react_agent`, custom `@tool` bindings, SQL generation, BigQuery execution, and natural language synthesis.
* **Defensive Query Engineering:** Fuzzy string matching (`LOWER(City) LIKE '%santa rosa%'`), null/missing-value handling, and strict validation rules for dirty data.
* **Enterprise Guardrails:** PII masking filters and Google Cloud Sensitive Data Protection (DLP) middleware for compliance.

**Performance:** <2.5s latency | 6,000+ records | 100% IaC via Terraform

---

### 2. Autonomous 4-Phase SME AI Factory (Mac Studio M2 Ultra Homelab)

**Type:** Self-Hosted Multi-Agent Orchestration Platform

**Role:** Systems Architect, CTO/CMO Agent

**Tech Stack:** Python, TypeScript, Ollama (Qwen 2.5/3.5), Gemini Flash, Cloudflare D1/Pages, Astro 5, Telegram Bot API

**Overview:** Bootstrapped AI factory running on single Mac Studio M2 Ultra, automating full-stack web app delivery for Philippine SMEs (prompt to production in ~5 minutes).

**Architecture:**

```
Telegram /build <Client>
         ↓
PHASE 1 (Researcher): Gemini Flash web-grounded research → dossier.md
         ↓
PHASE 2 (CMO): Ollama qwen3.5:9b → marketing brief + 5 FB posts + 3 IG captions + calendar
         ↓
PHASE 3 (CTO): Ollama qwen2.5-coder:14b → clone template, config, deploy via cto-deploy.sh
         ↓
PHASE 4 (COO): Ollama qwen3.5:9b → Trello ops alignment + team task breakdown
         ↓
Live Site: https://{slug}.nextgenai.ph (Cloudflare Pages + D1)
```

**Key Contributions:**

* **Multi-Agent Orchestration:** 4-phase pipeline with Telegram bot entry point, phase isolation, and error recovery.
* **Local → Cloud Failover:** Primary: Ollama models (qwen2.5-coder, qwen3.5) | Fallback: GCP Vertex AI / Gemini Flash on latency/rate-limit.
* **Automated CI/CD Pipeline (`cto-deploy.sh`):** 142 build-time tests, copy linting, Lighthouse CI ≥95, D1 provisioning, wrangler deploy. **Zero-downtime delivery.**
* **Deterministic Schema Validation:** Vertex AI Function Calling + Zod parsing for error-free financial/database calculations.
* **Real-Time Relays:** WebSocket communication hubs (Buzz-like) connecting human supervisors with background workers, streaming status queues in real time.
* **Enterprise Guardrails:** PII scrubbing, DLP middleware, token rate limiting, error logging.

**Impact:** 
- **48x Deployment Speedup:** 4 hours → 5 minutes
- **₱20,998/mo MRR** from 3 enterprise clients
- **18 barangays** served via CSR flagship
- **99.9% uptime** (Cloudflare infrastructure)

---

### 3. Multi-Branch POS & IT Infrastructure (Lynderm Facial Center & Day Spa)

**Type:** Multi-Branch Retail Operations Platform

**Role:** IT & Digital Marketing Admin, E-Commerce Operations Lead

**Tech Stack:** ManageMySpa (POS), Cloud database synchronization, PHP/MySQL backend, automated backup systems

**Overview:** Managed multi-branch IT, network, cloud POS infrastructure, and e-commerce while ensuring 100% operational uptime.

**Key Contributions:**

* **Multi-Branch IT Management:** Coordinated POS system updates across retail network with zero downtime.
* **Automated Database Backups:** Scheduled daily backups + disaster recovery procedures across branches.
* **E-Commerce Platform:** Web catalog, inventory sync, promo pricing engines across store networks.
* **Network & System Administration:** Desktop environments, local networks, IP security cameras, biometric access control.
* **Data Privacy & Compliance:** Enforced RA 10173 data integrity protocols across customer records.

**Impact:** 100% uptime during high-volume sales activations | Zero data loss across multi-branch operations

---

### 4. Enterprise Client SaaS Platforms (Astro 5 + TypeScript + D1)

| Platform | Purpose | Tech Stack | Business Model | Status |
|----------|---------|-----------|-----------------|--------|
| **ERBC Cockpit** | Real estate broker portal, lead pipeline, analytics | Astro 59%, TS 40% | ₱1M investment, ₱5,999/mo + 10% equity | **Production** |
| **Barangay Dila** | 24/7 AI chatbot + admin portal + Smart Guardian CCTV | Astro 58%, TS 39% | CSR flagship (18 barangays) | **Production** |
| **IMC Laboratory** | Metrology calibration tracking + ALCOA+ compliance | TS 76%, Astro 17% | ₱14,999/mo enterprise SaaS | **Production** |
| **Meridian School** | Student enrollment + RFID attendance + SMS alerts | Astro, TS | Barter + 80% SMS revenue share | **Production** |

---

## ⚙️ Technical Capabilities Matrix

```
┌──────────────────────────────────────────────────┬──────────────────────────────────────────────────┐
│ CLOUD AI & DATA INFRASTRUCTURE                   │ AGENTIC FRAMEWORKS & LOCAL AI ENGINES            │
├──────────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ • Google Cloud Vertex AI (Gemini models)         │ • LangGraph (`create_react_agent`)               │
│ • BigQuery SQL engineering & schema ingestion    │ • LangChain Core (`@tool` definitions)           │
│ • Google Cloud Sensitive Data Protection (DLP)   │ • Multi-Agent orchestration & ReAct loops        │
│ • Gemini 2.5 Flash / Document parsing            │ • Ollama / MLX deployment (Qwen, Llama)         │
│ • Terraform IaC (GCS, BigQuery, IAM)             │ • Zero-token-cost local automation               │
├──────────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ FULL-STACK & SERVERLESS                         │ ENTERPRISE INFRASTRUCTURE & AUTOMATION           │
├──────────────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ • Astro 5 + TypeScript + React                   │ • Automated background daemons & cron jobs       │
│ • Cloudflare D1 (SQLite) & Pages                 │ • WebSocket relays & real-time team sync         │
│ • Node.js / Python backends                      │ • Sub-3.8s speed-to-lead webhook pipelines       │
│ • Full-stack CI/CD (142 tests, Lighthouse ≥95)  │ • PII masking & RA 10173 compliance              │
│ • Claude Code / OpenAI Codex for rapid delivery  │ • Deterministic schema validation (Zod + Vertex) │
└──────────────────────────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 📊 Quantified Impact (9+ Years)

| Metric | Value | Context |
|--------|-------|---------|
| **Experience** | 9+ years | Systems architecture, cloud databases, enterprise AI |
| **Deployment Speedup** | 48x | 4 hours → 5 minutes (full-stack SME apps) |
| **Monthly Recurring Revenue** | ₱20,998 | 3 enterprise SaaS clients (ERBC, IMC, Meridian) |
| **Communities Served** | 18 barangays | CSR flagship (Barangay Dila) |
| **Agent Latency** | <2.5s | BigQuery analytics agent query time |
| **Webhook Speed-to-Lead** | <3.8s | Viber/SMS/WhatsApp notifications |
| **Build Test Suite** | 142 tests | Automated quality gates + Lighthouse CI ≥95 |
| **Infrastructure Drift** | 0% | 100% Terraform IaC |
| **System Uptime** | 99.9% | Cloudflare + automated monitoring |
| **Data Records Queried** | 6,000+ | BigQuery B2C lead analytics |
| **ALCOA+ Compliance** | 100% | IMC laboratory audit trails |
| **RA 10173 Compliance** | ✅ | PII masking, DLP, data privacy protocols |

---

## 🏢 Professional Background

**Founder & CTO/CMO • NextGen AI Solutions (2024 – Present)**
- Architected 4-phase autonomous SME AI factory
- Built enterprise BigQuery agent + LangGraph pipeline
- Deployed 4 production SaaS clients (₱20,998/mo MRR)
- Managed Mac Studio M2 Ultra homelab infrastructure

**IT & Digital Marketing Admin • Mariz Ventures Corporation (Lynderm Facial Center & Day Spa) (Jan 2020 – Dec 2020)**
- Multi-branch POS & IT infrastructure management
- Automated database backups & system maintenance
- E-commerce platform & web catalog operations
- 100% uptime across retail network

**System Administrator & Marketing Systems Lead • YSA Skin Care Corp. (Sep 2017 – Oct 2018)**
- Nationwide POS system updates & branch alignment
- Data integrity, privacy protocols, system availability

**IT Specialist & Field Collateral Lead • JEM Quantum Edge Corporation (Jun 2017 – Sep 2017)**
- Desktop environments, local networks, IP security cameras, biometric access control
- Digital & print promotional media design

---

## 🛠️ Technology Stack

**Languages:** Python, TypeScript, JavaScript, SQL, Shell, Astro  
**AI/LLM Frameworks:** LangGraph, LangChain, Ollama, Vertex AI (Gemini), Claude Code, OpenAI Codex  
**Cloud Platforms:** Google Cloud (BigQuery, Vertex AI, Cloud Storage, Cloud DLP, IAM)  
**Frontend:** Astro 5, React, TypeScript, Tailwind CSS  
**Backend:** Python (Streamlit), Node.js, Express  
**Databases:** BigQuery, Cloudflare D1 (SQLite), Cloud Storage  
**Infrastructure:** HashiCorp Terraform, wrangler, Docker  
**DevOps & CI/CD:** GitHub Actions, Lighthouse CI (≥95), automated testing, copy linting  
**Real-Time:** WebSocket relays, Telegram Bot API, Viber/SMS/WhatsApp webhooks  
**Compliance:** RA 10173 (PII masking), Google Cloud DLP, Zod schema validation  

---

## 📚 Education & Credentials

**Associate in Computer Programming** • New Sinai School and Colleges (2011 – 2013)  
**Specialization:** Full-Stack Development, GCP (Vertex AI), Agentic Tooling (Claude Code, Codex, Antigravity 2.0)  
**Typing Speed:** 87 WPM

---

## 🔗 Live Production Systems

**Barangay Dila (POC with Admin Portal):**
- Landing: [dila.nextgenai.ph](https://dila.nextgenai.ph)
- Admin: [dila.nextgenai.ph/admin/dashboard](https://dila.nextgenai.ph/admin/dashboard)

**Other Production Clients:**
- [erbc.nextgenai.ph](https://erbc.nextgenai.ph) — Real estate platform
- [1mc.nextgenai.ph](https://1mc.nextgenai.ph) — Lab calibration tracking

**Repository Organization:**
- [NextGen-AI-SME-Solutions](https://github.com/NextGen-AI-SME-Solutions) — All production systems
- [Dila Platform POC](https://github.com/nextgenhq/dila-platform-poc) — Full-stack landing + admin example

---

## 📖 Detailed Documentation

For architecture walkthroughs, deployment patterns, and technical deep-dives, see `/docs`:
- `architecture.md` — System design (4-Phase factory, BigQuery agent, Terraform, D1+Pages)
- `client-case-studies.md` — Business impact & technical details per client
- `tech-stack.md` — Complete technology breakdown
- `enterprise-patterns.md` — Compliance, security, and scaling patterns (coming soon)

---

**Contact:** nextgensmeaisolutions@gmail.com | **GitHub:** [@nextgenhq](https://github.com/nextgenhq)
