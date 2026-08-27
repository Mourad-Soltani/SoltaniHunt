# SoltaniHunt — Session Context
# Signature: Mourad.Soltani
# Saved: 2026-08-27
# Purpose: resume development after free-tier reset

## Project
Local-first AI job-search framework (trending 2026: MadsLorentzen/ai-job-search style).
Evaluate postings, score fit, tailor resume bullets, draft cover letters, generate interview packs.

## Status
- Scaffold: complete
- Backend FastAPI + SQLite: complete
- Heuristic "AI" engine (no paid API required): complete
- Frontend dashboard: complete
- Health tests: complete
- Signature: Mourad.Soltani in all source files

## Run
```
cd SoltaniHunt
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m pytest tests/ -q
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Next if resuming
- Optional LLM adapter behind SOLTANI_LLM_URL
- CSV import of job boards
- PDF resume export
