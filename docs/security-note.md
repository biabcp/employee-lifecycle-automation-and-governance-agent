# Security Note

This project uses synthetic demo data and local-only credentials. It is designed as a portfolio demonstration of lifecycle governance workflows, not a production identity governance, HRIS, IAM, or access management system.

## Security boundaries
- Local demo environment only.
- Synthetic local demo accounts only.
- No production business data.
- No production identity or access automation authority.

## Required safe usage practices
- Demo credentials are for local testing only.
- No production secrets should be committed to this repository.
- Use `.env.example` as the baseline for local configuration.
- Store sensitive real credentials outside version control.
- Do not use `password123`-style credentials in production.

## Platform non-replacement statement
This repository is not a replacement for enterprise:
- IAM / IGA
- SIEM / SOAR
- HRIS
- GRC governance platforms

## Not production use
Use this project for portfolio demonstration, local experimentation, and governance workflow concept validation only.
