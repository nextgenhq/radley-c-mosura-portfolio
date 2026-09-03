# 🚀 Radley Mosura — Portfolio Showcase

**Senior Agentic Data & Full-Stack AI Engineer**

*Specializing in Multi-Agent Orchestration, Local AI Homelabs, Enterprise GCP Data Pipelines, and Full-Stack SME Applications.*

---

## 🛠️ Featured Highlight Projects

### 1. Enterprise Lead Analytics Agent (BigQuery + LangGraph + Terraform)

**Type:** Production Infrastructure & AI Data Agent

**Role:** Lead Architect & Data Engineer

**Tech Stack:** Python, LangGraph, LangChain, Google BigQuery, Gemini 2.5 Flash, HashiCorp Terraform, Streamlit

**Overview:** Built an enterprise-grade natural language analytics agent that allows non-technical business stakeholders to query over 6,000+ raw B2C lead records in BigQuery using plain English.

**Architecture & Key Contributions:**

* **Infrastructure as Code (IaC):** Authored HashiCorp Terraform (`main.tf`) modules to provision Google Cloud Storage buckets for raw ingestion and BigQuery datasets (`leads_analytics.raw_leads`) with strict IAM service account security.
* **Dynamic Schema Pre-Fetching:** Solved LLM SQL schema hallucination by implementing automated startup schema pre-fetching that feeds exact datatypes and column definitions directly into system context.
* **LangGraph ReAct Loop:** Built an autonomous reasoning loop using LangGraph (`create_react_agent`) and custom `@tool` bindings that generate optimized SQL, execute queries via the native BigQuery Python SDK, and synthesize raw dataset returns into natural language business summaries.
* **Defensive Query Engineering:** Implemented fuzzy string matching rules (`LOWER(City) LIKE '%santa rosa%'`) and strict missing-value handling to seamlessly navigate dirty data formats.

---

### 2. Autonomous 4-Phase SME AI Factory (Local Homelab)

**Type:** Self-Hosted AI Agent Orchestrator

**Role:** AI Systems Engineer & CTO Agent

**Tech Stack:** Python, TypeScript, Ollama (Qwen 2.5/3.5), Gemini Flash, Cloudflare D1/Pages, Astro 5, Telegram Bot API

**Overview:** Designed and deployed a self-hosted AI factory running on a Mac Studio M2 Ultra that automates full-stack web app delivery for Philippine SMEs from prompt to production in under 5 minutes.

**Architecture & Key Contributions:**

* **4-Phase Multi-Agent Pipeline:**
  * **Phase 1 (Researcher):** Web-grounded research dossier creation using Gemini Flash.
  * **Phase 2 (CMO):** Content generation (marketing briefs, social media schedules) via local `qwen3.5:9b`.
  * **Phase 3 (CTO - Core Focus):** Code generation, template cloning, and automated deployment via `qwen2.5-coder:14b`.
  * **Phase 4 (COO):** Trello ops task alignment via `qwen3.5:9b`.

* **Automated CI/CD Deployment:** Authored `cto-deploy.sh` pipeline enforcing 142 build-time tests, copy linting, and Lighthouse CI performance gates (≥95) before deploying to Cloudflare Pages and D1 databases.
* **Local / Cloud Hybrid Failover:** Configured local Ollama models for primary execution with dynamic failover routing to GCP Vertex AI / Gemini endpoints.

---

## 💼 Enterprise Client Production Systems

| Client Platform | Purpose & Architecture | Stack | Status & Metric |
| --- | --- | --- | --- |
| **ERBC Cockpit** | Real estate broker portal, lead management, and analytics dashboard. | Astro 5, TypeScript, Cloudflare D1 | **Production** (₱1M / 10% Investor System) |
| **Barangay Dila System** | Public service AI chatbot, admin portal, and Smart Guardian CCTV overlay. | Astro 5, TypeScript, Tailwind | **Production** (CSR Flagship across 18 Barangays) |
| **IMC Laboratory** | Metrology calibration tracking system with strict ALCOA+ compliance. | TypeScript, Astro, Custom CSS | **Production** (₱15k/mo Enterprise SaaS) |
| **Meridian School** | Student enrollment platform with integrated RFID attendance and automated SMS alerts. | Astro, TypeScript, SMS API | **Production** (Barter System + Revenue Share) |

---

## ⚙️ Core Technical Capabilities Matrix

```
┌─────────────────────────────────────────────────┬─────────────────────────────────────────────────┐
│ Cloud AI & Data Systems                         │ Agentic Frameworks & Homelabs                   │
├─────────────────────────────────────────────────┼─────────────────────────────────────────────────┤
│ • GCP BigQuery / SQL Engineering                │ • LangChain / LangGraph                         │
│ • HashiCorp Terraform (IaC)                     │ • Multi-Agent Orchestration                     │
│ • Gemini 2.5 Flash / Vertex AI                  │ • Ollama / Local Model Deployment (Qwen, MLX)   │
│ • Dynamic Tool Calling & Schema Ingestion       │ • Autonomous ReAct Loops                        │
├─────────────────────────────────────────────────┼─────────────────────────────────────────────────┤
│ Full-Stack & Infrastructure                     │ Security & Quality Engineering                  │
├─────────────────────────────────────────────────┼─────────────────────────────────────────────────┤
│ • Node.js / TypeScript / Python                 │ • PII Masking & Sensitive Data Protection       │
│ • Astro 5 / React / Tailwind CSS                │ • Automated Copy-Linting & Lighthouse CI (≥95)  │
│ • Cloudflare D1 (SQL) & Cloudflare Pages        │ • Failover Model Routing & Token Rate Limiting  │
└─────────────────────────────────────────────────┴─────────────────────────────────────────────────┘
```

---

## 📊 Summary Metrics & System Impact

* **Agent Speed:** Reduced SQL generation and insight synthesis latency to <2.5 seconds.
* **Deployment Efficiency:** Streamlined full-stack SME website and database deployments from hours to ~5 minutes.
* **Zero Infrastructure Drift:** 100% of BigQuery datasets and storage buckets provisioned declaratively via Terraform.
* **Data Scale:** Production agent pipeline actively querying 6,000+ B2C lead records with strict validation rules.
* **Revenue Impact:** ₱20,998/mo recurring (ERBC ₱5,999 + IMC ₱14,999 + performance fees).
* **Social Impact:** CSR flagship (Barangay Dila) scales across 18 barangays in Santa Rosa.

---

## 🔗 Repository Links

**NextGen AI Solutions Org:**
- [sme-landing-template](https://github.com/NextGen-AI-SME-Solutions/sme-landing-template) — Master Astro 5 template (51.8% Astro, 46.1% TS)
- [erbc](https://github.com/NextGen-AI-SME-Solutions/erbc) — ERBC real estate platform (58.9% Astro, 39.6% TS)
- [dila](https://github.com/NextGen-AI-SME-Solutions/dila) — Barangay Dila client system (57.9% Astro, 38.8% TS)
- [ai-homelab-setup](https://github.com/NextGen-AI-SME-Solutions/ai-homelab-setup) — Self-hosted AI orchestration (76.5% Python, 22.5% Shell)
- [AI-Home-Lab-Ollama](https://github.com/NextGen-AI-SME-Solutions/AI-Home-Lab-Ollama) — Ollama deployment automation (100% Shell)
- [nextgen-website](https://github.com/NextGen-AI-SME-Solutions/nextgen-website) — Corporate site (48.6% Astro, 45.5% TS)

---

## 📚 Documentation

For detailed architecture walkthroughs, deployment pipelines, and client case studies, see `/docs`.
