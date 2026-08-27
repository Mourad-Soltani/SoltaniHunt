"""SoltaniHunt API. Signature: Mourad.Soltani"""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app import __version__
from app.engine import cover_letter, fit_score, interview_pack, tailor_bullets
from app.store import (
    add_job,
    delete_job,
    get_job,
    get_profile,
    list_jobs,
    profile_blob,
    update_profile,
)

AUTHOR = "Mourad.Soltani"
FRONTEND = Path(__file__).resolve().parent.parent / "frontend"

app = FastAPI(
    title="SoltaniHunt",
    description="Local-first AI job search by Mourad.Soltani",
    version=__version__,
)


class ProfileIn(BaseModel):
    name: str | None = None
    headline: str | None = None
    summary: str | None = None
    skills: list[str] | str | None = None


class JobIn(BaseModel):
    title: str = Field(..., min_length=2)
    company: str = Field(..., min_length=1)
    location: str = ""
    description: str = Field(..., min_length=20)
    url: str = ""


@app.get("/api/health")
def health():
    return {
        "ok": True,
        "service": "SoltaniHunt",
        "version": __version__,
        "author": AUTHOR,
    }


@app.get("/api/profile")
def api_profile():
    return get_profile()


@app.put("/api/profile")
def api_update_profile(body: ProfileIn):
    return update_profile(body.model_dump(exclude_none=True))


@app.get("/api/jobs")
def api_jobs():
    return {"jobs": list_jobs(), "author": AUTHOR}


@app.post("/api/jobs")
def api_add_job(body: JobIn):
    blob = profile_blob()
    analysis = fit_score(blob, f"{body.title} {body.company} {body.description}")
    analysis["bullets"] = tailor_bullets(blob, body.description, body.title)
    analysis["cover_letter"] = cover_letter(
        get_profile()["name"], body.title, body.company, get_profile()["summary"], body.description
    )
    analysis["interview"] = interview_pack(body.title, body.description)
    return add_job(body.model_dump(), analysis)


@app.get("/api/jobs/{job_id}")
def api_job(job_id: int):
    job = get_job(job_id)
    if not job:
        raise HTTPException(404, "Job not found")
    return job


@app.delete("/api/jobs/{job_id}")
def api_delete_job(job_id: int):
    if not delete_job(job_id):
        raise HTTPException(404, "Job not found")
    return {"ok": True, "author": AUTHOR}


if FRONTEND.exists():
    app.mount("/static", StaticFiles(directory=FRONTEND), name="static")


@app.get("/")
def index():
    index_path = FRONTEND / "index.html"
    if not index_path.exists():
        raise HTTPException(500, "frontend missing")
    return FileResponse(index_path)
