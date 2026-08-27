# Architecture — Mourad.Soltani

```
browser -> FastAPI (app/main.py)
             |-- /api/health
             |-- /api/profile
             |-- /api/jobs
             +-- static frontend
store.py  SQLite file in data/
engine.py deterministic fit + generation
```

No external paid APIs in v1 so tests stay deterministic.
Author stamp: Mourad.Soltani
