# SoltaniHunt

**Local-first AI job-search pipeline** — score postings, tailor bullets, draft cover letters, and build interview packs on your machine. No paid LLM required.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue.svg)](requirements.txt)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/)
[![Author](https://img.shields.io/badge/Author-Mourad.Soltani-black.svg)](https://github.com/Mourad-Soltani)

**Repo:** [github.com/Mourad-Soltani/SoltaniHunt](https://github.com/Mourad-Soltani/SoltaniHunt)

---

## Why it exists

Job boards and cloud AI apply tools send your CV off-machine. SoltaniHunt keeps the loop **local**:

| Capability | What you get |
|------------|----------------|
| Fit score | Keyword match vs your profile (matched / missing skills) |
| Tailoring | Resume-style bullets aimed at the posting |
| Cover letter | Draft letter with score + keywords |
| Interview pack | Behavioral + technical prompts + talking points |
| Dashboard | Simple UI over the same API |
| Health suite | `pytest` green offline |

Deterministic engine by default (stable demos, no API keys). Optional LLM hook for buyers who want generative upgrades.

---

## Quick start (60 seconds)

```bash
git clone https://github.com/Mourad-Soltani/SoltaniHunt.git
cd SoltaniHunt
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest tests/ -q
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open **http://127.0.0.1:8000**

Docker:

```bash
docker build -t soltanihunt .
docker run --rm -p 8000:8000 soltanihunt
```

---

## API surface

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/api/health` | Liveness + author stamp |
| `GET`/`PUT` | `/api/profile` | Candidate profile |
| `GET`/`POST` | `/api/jobs` | List / add + score + generate |
| `GET`/`DELETE` | `/api/jobs/{id}` | Detail / remove |
| `GET` | `/` | Dashboard |

---

## Stack

- **Backend:** FastAPI, Pydantic, SQLite
- **Frontend:** Static HTML / CSS / JS (no Node build)
- **Tests:** pytest + TestClient
- **Ops:** Dockerfile, `scripts/health.sh`

---

## Project layout

```
SoltaniHunt/
├── app/           # FastAPI, scoring engine, SQLite store
├── frontend/      # Dashboard
├── tests/         # Health + pipeline tests
├── docs/          # Architecture
├── scripts/       # Health runner
├── SALE.md        # Acquisition / asset-sale notes
├── Dockerfile
└── requirements.txt
```

---

## For buyers / acquirers

This repository is a **complete, tested MVP** suitable for:

- White-label / embed into a career product
- Local privacy-focused job-search tools
- Acqui-hire or asset purchase (code + brand)

See **[SALE.md](SALE.md)** for what is included, excluded, and how to evaluate the asset.

**Contact for serious offers:** open a GitHub issue titled `Acquisition interest` or contact the GitHub account **Mourad-Soltani**.

---

## License

MIT © 2026 **Mourad.Soltani** — see [LICENSE](LICENSE).

Commercial exclusive assignment of the brand/repo is handled under a separate IP assignment at close.
