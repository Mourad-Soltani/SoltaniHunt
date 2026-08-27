# SoltaniHunt — Asset sale notes

**Author:** Mourad.Soltani  
**Repository:** https://github.com/Mourad-Soltani/SoltaniHunt  
**Status:** Pre-revenue MVP · tests green · public MIT source

## What you are buying (typical asset deal)

| Included | Not included by default |
|----------|-------------------------|
| Full source (this repo) | Users, revenue, or brand trademarks beyond the repo name |
| MIT-licensed code | Cloud hosting / domain |
| Docs, tests, Dockerfile | Ongoing employment (negotiable) |
| Right to fork / rebrand under MIT | Exclusive IP assignment (requires paid assignment at close) |

For a **paid exclusive acquisition**, seller executes a one-page IP assignment of the SoltaniHunt name and codebase after cleared payment.

## Technical diligence (run yourself)

```bash
pip install -r requirements.txt
python -m pytest tests/ -q          # expect: 5 passed
uvicorn app.main:app --port 8000
curl -s http://127.0.0.1:8000/api/health
```

Stack: Python 3.12-friendly, FastAPI, SQLite file DB, static frontend. No required third-party API keys.

## Known scope (honest)

- Fit scoring is **deterministic keyword-based** (not a trained model).  
- UI is functional, not a polished design system.  
- No multi-tenant auth, billing, or job-board scrapers in v1.  
- Designed for local / single-user or small deploy; scale needs buyer engineering.

## Suggested evaluation questions

1. Does `/api/health` and the pytest suite pass on your machine?  
2. Does the dashboard create a job and return analysis JSON?  
3. Is MIT + assignment enough for your product counsel?  
4. Do you need 7–60 days of transition support (extra fee)?

## Commercial contact

Serious buyers: GitHub issue **`Acquisition interest`** on this repo, or message the GitHub account **Mourad-Soltani**.

Price and payment terms are negotiated per offer (as-is vs support package). No obligation until a written agreement and payment schedule are accepted.
