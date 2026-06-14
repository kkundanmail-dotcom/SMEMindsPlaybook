# SMEMinds Playbook Backend

FastAPI service for user registration and playbook progress sync.

## Setup

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload --port 8000
```

API is at `http://127.0.0.1:8000/api`. OpenAPI docs at `/docs`.

## Env vars

- `SMEMINDS_JWT_SECRET` — JWT signing secret (default: `dev-secret-change-me` — change in prod)
- `SMEMINDS_ADMIN_KEY` — header `X-Admin-Key` for `/api/admin/users` (default: `dev-admin-key`)

## Endpoints

| Method | Path                 | Auth   | Body / Notes                                |
|--------|----------------------|--------|---------------------------------------------|
| GET    | `/api/health`        | none   | liveness check                              |
| POST   | `/api/register`      | none   | `{email, password, name, role}` → token     |
| POST   | `/api/login`         | none   | `{email, password}` → token                 |
| GET    | `/api/me`            | Bearer | current user profile                        |
| GET    | `/api/progress`      | Bearer | `{visited, checklists, quizScores, feedback}` |
| PUT    | `/api/progress`      | Bearer | replace progress blob                       |
| GET    | `/api/admin/stats`   | X-Admin-Key | aggregate counts (users, visits, quizzes, feedback) |
| GET    | `/api/admin/users`   | X-Admin-Key | list users with progress stats         |
| GET    | `/api/admin/users/{id}/progress` | X-Admin-Key | full progress for one user      |
| GET    | `/admin`             | none (login in UI) | admin dashboard HTML              |

## Storage

SQLite file `smeminds.db` next to `main.py`. Two tables: `users`, `progress` (single JSON blob per user). Delete the file to reset.

## Client wiring

The playbook (`src/app.js`) reads `window.SMEMINDS_API_BASE` (default `http://127.0.0.1:8000/api`). Set it on the window before app load if you host the API elsewhere.
