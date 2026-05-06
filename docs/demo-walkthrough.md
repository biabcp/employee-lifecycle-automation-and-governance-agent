# Demo Walkthrough

This walkthrough is designed for recruiters, hiring managers, and technical reviewers evaluating employee lifecycle governance coverage.

## 1) Start the local demo environment
```bash
docker compose up --build
```

Access points:
- Frontend: `http://localhost:5173`
- Backend API docs: `http://localhost:8000/docs`

## 2) Log in as each demo role
Use the synthetic local demo accounts listed in the README:
- Admin
- HR
- IT
- Security
- GRC

> Demo mode note: credentials and data are synthetic and local-only.

## 3) Review dashboard
- Confirm that lifecycle records and governance statuses are visible.
- Compare role-based access/visibility differences where implemented.

## 4) Create or inspect onboarding workflow
- Create a new onboarding request or inspect an existing seeded record.
- Validate request metadata, approvals, and provisioning tasks.
- Review associated audit evidence fields.

## 5) Review transfer workflow
- Inspect a transfer lifecycle record and state transitions.
- Confirm approval requirements and transfer-specific access review checkpoints.

## 6) Review offboarding workflow
- Inspect deprovisioning tasks and closure requirements.
- Verify timing and evidence checkpoints for access removal governance.

## 7) Check access risk
- Review modeled access risk signals tied to lifecycle events.
- Identify high-priority records requiring governance action.

## 8) Review evidence records
- Validate evidence attributes (request/approval/provisioning/review traceability).
- Confirm that records are auditable in demo format.

## 9) Use or inspect governance agent output
- Review governance summaries for lifecycle status and exceptions.
- Compare role-specific summary outputs for HR, IT, Security, Admin, and GRC.

## 10) Export or review audit summary
- If export/report endpoints are available, generate an audit-oriented summary.
- If not implemented, present this step as **currently modeled/planned** in demo mode.

---

## Current implementation honesty guide
When presenting this project, use these labels where needed:
- **Implemented**: functionality available in current code paths.
- **Demo-mode**: represented in synthetic data flow or UI/API modeling.
- **Planned**: roadmap capability not yet implemented.
