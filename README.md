# SoltaniHunt

Local-first AI job-search workspace.

Trending 2026 pattern: evaluate postings on your machine, score fit against your profile, tailor resume bullets, draft a cover letter, and generate an interview pack.

**Author:** Mourad.Soltani

## Why this project

GitHub trending in August 2026 is dominated by agent skills and local job-search harnesses. SoltaniHunt is a complete, testable slice of that idea that runs without a paid model key. The engine is deterministic keyword-fit so the health suite stays offline-stable. Swap in an LLM later via `SOLTANI_LLM_URL` if you want.

## Features

- Profile store (SQLite)
- Job pipeline with fit score, matched/missing keywords
- Tailored bullets + cover letter + interview questions
- Health endpoint
- Minimal dashboard

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest tests/ -q
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open http://127.0.0.1:8000

## Health test

```bash
python -m pytest tests/test_health.py -q
```

Must pass before release. Signature `Mourad.Soltani` is asserted in API and generated artifacts.

## Layout

```
SoltaniHunt/
  app/           FastAPI + engine + store
  frontend/      dashboard
  tests/         health suite
  data/          sqlite (created at runtime)
  docs/          notes
  CONTEXT.md     resume file for free-tier pauses
```

## License

MIT — Mourad.Soltani
