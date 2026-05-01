# employee-lifecycle-automation-governance-agent

Enterprise local platform for employee lifecycle governance across onboarding, offboarding, transfers, access, risk, evidence, and audit.

## Quick start
- `docker compose up --build`
- Backend: http://localhost:8000/docs
- Frontend: http://localhost:5173

## Demo users
- admin@example.com / password123
- hr@example.com / password123
- it@example.com / password123
- security@example.com / password123
- grc@example.com / password123
- auditor@example.com / password123
- manager@example.com / password123

## Included
- FastAPI + PostgreSQL + SQLAlchemy
- JWT + bcrypt auth
- RBAC (Admin/HR Admin enforced in current routes)
- Workflow creation for onboarding
- Task generation
- Audit logging
- Celery worker/beat + Redis wiring
- MinIO + MailHog services
- React + Vite frontend shell
- Seed script with demo users and employees

## Testing
- `docker compose run --rm backend pytest`
