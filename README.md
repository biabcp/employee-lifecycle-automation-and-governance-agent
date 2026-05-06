# Employee Lifecycle Automation & Governance Agent

## Executive Summary
**Employee Lifecycle Automation & Governance Agent** is a local full-stack governance platform that turns onboarding, transfers, and offboarding into controlled, auditable workflows with access risk tracking, evidence capture, role-based views, and AI-enabled governance summaries.

This project is designed for cybersecurity, GRC, identity governance, and compliance automation portfolio demonstration. It emphasizes lifecycle control coverage, workflow transparency, and audit-ready traceability using synthetic demo data in a local demo environment.

## Problem Statement
Employee lifecycle events often span HR, IT, Security, and governance teams. Without coordinated workflow controls, organizations face:
- fragmented onboarding/offboarding/transfers processes,
- delayed access provisioning or deprovisioning,
- unclear ownership of approvals,
- incomplete audit evidence,
- and poor visibility into lifecycle access risk.

## Solution Overview
This repository demonstrates a practical local implementation of **employee lifecycle governance** where:
- requests move through lifecycle workflow stages,
- role-based users review and approve actions,
- audit evidence is captured for lifecycle events,
- access risk records are modeled and surfaced,
- and a governance agent provides role-specific status summaries.

## Key Features
- Role-based platform experience for Admin, HR, IT, Security, and GRC reviewers.
- Core lifecycle workflows for onboarding, transfers, and offboarding.
- Governance state modeling across request, approval, provisioning, review, evidence, and closure stages.
- Audit evidence capture and record visibility.
- Access risk tracking for lifecycle governance signals.
- API-first backend with local frontend dashboard and local services via Docker Compose.

## Governance Agent Capabilities
The governance agent is a **demo/local governance assistant** designed to:
- Summarize employee lifecycle status.
- Identify overdue onboarding, offboarding, or transfer tasks.
- Flag missing approval evidence.
- Highlight access governance risk signals.
- Generate audit-ready governance summaries.
- Provide role-specific views for HR, IT, Security, Admin, and GRC.

See: [`docs/governance-agent.md`](docs/governance-agent.md).

## Demo Users
### Synthetic local demo accounts
> ⚠️ These credentials are for **local demo use only** with synthetic demo data.

- `admin@example.com`
- `hr@example.com`
- `it@example.com`
- `security@example.com`
- `grc@example.com`

Default local demo password (if unchanged in seed/demo config): `password123`.

## Security Note
This project uses synthetic demo data and local-only credentials. It is designed as a portfolio demonstration of lifecycle governance workflows, not a production identity governance, HRIS, IAM, or access management system.

- Demo credentials are for local testing only.
- No production secrets should be committed.
- Use `.env.example` as the baseline for local environment configuration.
- Do not use `password123`-style credentials in production.
- This app is not a replacement for enterprise IAM, IGA, SIEM, SOAR, HRIS, or GRC platforms.

See: [`docs/security-note.md`](docs/security-note.md).

## Architecture
High-level architecture documentation and Mermaid diagram:
- [`docs/architecture.md`](docs/architecture.md)

## Project Metrics
Defensible capability-based metrics for this portfolio project:
- **5 demo user roles**: Admin, HR, IT, Security, and GRC.
- **3 core lifecycle workflows**: onboarding, transfer, and offboarding.
- **5+ lifecycle governance risk signals modeled**.
- **8+ audit evidence fields** captured per lifecycle event.
- **10+ governance states** across request, approval, provisioning, review, evidence, and closure.
- **100% synthetic demo data**.
- **Local Docker Compose environment** for repeatable portfolio review.

See: [`docs/project-metrics.md`](docs/project-metrics.md).

## Tech Stack
- **Frontend**: React + Vite + TypeScript
- **Backend**: FastAPI + SQLAlchemy + Pydantic
- **Data**: PostgreSQL
- **Queue/Async Services**: Celery + Redis
- **Storage/Email (local services)**: MinIO + MailHog
- **Auth/Security**: JWT + bcrypt
- **Containerization**: Docker Compose

## Quick Start
1. Clone repository.
2. Create local environment config from `.env.example`.
3. Start services:
   ```bash
   docker compose up --build
   ```
4. Access:
   - Backend API docs: `http://localhost:8000/docs`
   - Frontend UI: `http://localhost:5173`

## Example Use Cases
- **Onboarding governance**: Track approvals, provisioning tasks, and required evidence for a new hire.
- **Transfer governance**: Validate role change approvals, recertify access, and monitor transfer-related risk.
- **Offboarding governance**: Coordinate deprovisioning, verify evidence completeness, and identify overdue tasks.
- **GRC review readiness**: Compile lifecycle status and evidence coverage for audit-oriented review.

See walkthrough: [`docs/demo-walkthrough.md`](docs/demo-walkthrough.md).

## Portfolio Positioning
### Resume-ready bullet
- Built full-stack lifecycle governance platform for onboarding, transfers, and offboarding with role-based workflows, access risk tracking, evidence capture, and AI-enabled governance summaries | Modeled 5 demo roles, 3 lifecycle workflows, 5+ risk signals, and audit-ready evidence records using synthetic data in a local Docker environment.

### LinkedIn-ready summary
- I built a local full-stack Employee Lifecycle Automation & Governance Agent to demonstrate how HR, IT, Security, and GRC workflows can be converted into controlled, auditable lifecycle processes with access risk tracking, evidence capture, and AI-enabled governance summaries.

## Roadmap
See phased roadmap: [`docs/roadmap.md`](docs/roadmap.md).

## Screenshots
Screenshot placeholders and suggested captures are documented in:
- [`docs/screenshots.md`](docs/screenshots.md)

## Not Production Use
This repository is a **local demo environment** intended for portfolio and educational purposes only.

## License
Licensed under the terms in [`LICENSE`](LICENSE).
