# Contributing

Thanks for contributing to this portfolio project.

## Local development
1. Copy environment values from `.env.example`.
2. Start services:
   ```bash
   docker compose up --build
   ```
3. Backend API docs:
   - `http://localhost:8000/docs`
4. Frontend app:
   - `http://localhost:5173`

## Testing
Run backend tests:
```bash
docker compose run --rm backend pytest
```

## Contribution expectations
- Keep changes aligned with employee lifecycle governance scope.
- Preserve non-production and synthetic demo data positioning.
- Avoid claiming unsupported enterprise integrations or production outcomes.
