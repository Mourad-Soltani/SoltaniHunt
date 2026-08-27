# Architecture — Mourad.Soltani

```
Browser  →  FastAPI (app/main.py)
              ├── /api/health
              ├── /api/profile  →  store.py (SQLite)
              ├── /api/jobs     →  engine.py (fit + generation)
              └── /             →  frontend/*
```

## Components

| Module | Role |
|--------|------|
| `app/engine.py` | Tokenize, fit score, bullets, cover letter, interview pack |
| `app/store.py` | SQLite profile + jobs |
| `app/main.py` | HTTP API + static mount |
| `frontend/` | Single-page dashboard |
| `tests/test_health.py` | Offline health + pipeline assertions |

## Design choices for buyers

- **No cloud dependency** → easy to demo and diligence.
- **MIT** → low friction to integrate; exclusive rights via paid assignment.
- **Thin UI** → replace with your design system without a heavy SPA.
- **Clear extension point** → swap `engine.py` for LLM-backed generation later.

## Data

SQLite file under `data/` (gitignored). Created on first API use.
