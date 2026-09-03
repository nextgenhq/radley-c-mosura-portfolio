# Technology Stack Overview

## Backend & Data Layer

### Python Ecosystem
- **LangChain Core:** `@tool` decorators for custom tool definitions
- **LangGraph:** `create_react_agent` for autonomous reasoning loops
- **Google BigQuery Python SDK:** Native query execution with streaming results
- **GCP Credentials Management:** Service account JSON auth
- **Streamlit:** Web UI for agent interaction

### SQL & Data Warehousing
- **BigQuery SQL:** Advanced query patterns
  - Fuzzy string matching: `LOWER(City) LIKE '%pattern%'`
  - NULL/missing value handling: `COALESCE(field, 'unknown')`
  - Dynamic column wrapping with backticks for reserved keywords
  - Aggregations and time-series analysis
- **Cloudflare D1:** SQLite-compatible database for application state (leads, users, subscriptions)
- **Google Cloud Storage:** Raw lead data ingestion buckets

### Infrastructure & DevOps
- **HashiCorp Terraform:** IaC for GCP provisioning
  - Google Cloud Storage bucket creation
  - BigQuery dataset and table schemas
  - IAM service account roles and permissions
  - Zero manual configuration drift
- **Google Cloud IAM:** Restricted service account scopes for tool execution
- **wrangler.toml:** Cloudflare Workers configuration

## Frontend & Web Application Layer

### Frameworks & Build Tools
- **Astro 5:** Static site generation with SSR optional, optimized for performance
- **TypeScript:** End-to-end type safety
- **React:** Interactive UI components (islands architecture in Astro)
- **Tailwind CSS:** Utility-first styling
- **Cloudflare Pages:** Serverless hosting with automatic deploys

### Content & Data Management
- **Markdown:** Client content (services, testimonials, FAQs) stored as .md files
- **Frontmatter:** YAML metadata for content organization
- **Astro Content Collections:** Automated validation and type-checking

## AI & LLM Layer

### Local Execution (Primary)
- **Ollama:** Local model serving on Mac Studio M2 Ultra
  - `qwen2.5-coder:14b` — Code generation (CTO agent)
  - `qwen3.5:9b` — General reasoning (Researcher, CMO, COO agents)
- **MLX Runtime:** Optimized inference on Apple Silicon
- **Custom Tool Calling:** Ollama tool_use patterns for agent tasks

### Cloud Execution (Failover)
- **GCP Vertex AI:** Managed model endpoint for redundancy
- **Gemini 2.5 Flash:** Fast, cost-effective fallback LLM
- **Dynamic Routing:** Local → cloud failover on latency/rate-limit

## CI/CD & Quality Assurance

### Testing & Validation
- **Astro Compile Test:** Build validation
- **Unit Tests:** 142 total tests across codebase
- **Lighthouse CI:** Performance gate ≥95 score
- **Copy Linting:** Markdown grammar and style checks
- **LHCI GitHub Integration:** Automated perf regression detection

### Deployment Pipeline
- **cto-deploy.sh:** Orchestrates the full deploy sequence
  1. Run all tests
  2. Build Astro project
  3. Create D1 database (if new)
  4. Generate wrangler.toml
  5. Inject CF Pages secrets
  6. Deploy to Cloudflare
- **Zero-Downtime:** Deployments complete in ~5 minutes

## Integration & External APIs

### Communication
- **Telegram Bot API:** Entry point for 4-Phase pipeline (`/build` command)
- **SMS API:** Parent alerts (Meridian), broker notifications (ERBC)
- **Facebook Graph API:** Social media content scheduling (CMO agent output)

### Observability
- **Structured Logging:** Agent decisions, tool calls, routing decisions
- **Error Tracking:** Ollama failures, BigQuery timeouts, Gemini fallback events
- **Token Usage Metrics:** LLM input/output tracking for cost optimization

## Security & Compliance

### Data Protection
- **PII Masking:** Lead records obfuscated in development
- **IAM Service Accounts:** Scoped credentials for BigQuery tool access
- **Cloudflare D1 Encryption:** At-rest and in-transit
- **ALCOA+ Compliance:** Audit trails for IMC laboratory system

### Access Control
- **GitHub Secrets:** API keys and credentials stored securely
- **IAM Roles:** Least-privilege principle for service accounts
- **RBAC:** Role-based access for client admin portals

---

## Language Composition by Repository

| Repository | Primary Language | Secondary | Distribution |
|------------|------------------|-----------|---------------|
| **sme-landing-template** | Astro 51.8% | TS 46.1% | Shell 1.2%, Other 0.9% |
| **erbc** | Astro 58.9% | TS 39.6% | Other 1.5% |
| **dila** | Astro 57.9% | TS 38.8% | JS 2.1%, Other 1.2% |
| **1mc** | TS 76.4% | Astro 16.9% | CSS 6.3%, Other 0.4% |
| **nextgen-website** | Astro 48.6% | TS 45.5% | CSS 4.5%, JS 0.9%, Shell 0.4%, HTML 0.1% |
| **ai-homelab-setup** | Python 76.5% | Shell 22.5% | TS 1% |
| **AI-Home-Lab-Ollama** | Shell 100% | — | — |

---

## Deployment Architecture

```
Local Development (Mac Studio M2 Ultra)
         ↓
[Python agent + LangGraph]
[Ollama (qwen2.5-coder)]
         ↓
cto-deploy.sh
         ↓
[Astro Build | Tests | Lighthouse | Lint]
         ↓
[wrangler deploy]
         ↓
Cloudflare Global Edge Network
         ↓
https://{slug}.nextgenai.ph (Client Site)
         ↓
Cloudflare D1 (Database)
Google BigQuery (Analytics Warehouse)
```
