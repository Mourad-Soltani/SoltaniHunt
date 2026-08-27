"""Health and engine tests. Author: Mourad.Soltani"""

from fastapi.testclient import TestClient

from app.engine import cover_letter, fit_score, interview_pack, tailor_bullets
from app.main import app

client = TestClient(app)


def test_health_ok():
    res = client.get("/api/health")
    assert res.status_code == 200
    body = res.json()
    assert body["ok"] is True
    assert body["author"] == "Mourad.Soltani"
    assert body["service"] == "SoltaniHunt"


def test_profile_roundtrip():
    res = client.get("/api/profile")
    assert res.status_code == 200
    assert "Mourad" in res.json()["name"] or res.json()["name"]
    updated = client.put(
        "/api/profile",
        json={"headline": "Staff builder — Mourad.Soltani"},
    )
    assert updated.status_code == 200
    assert "Mourad.Soltani" in updated.json()["headline"]


def test_job_pipeline():
    payload = {
        "title": "Backend Engineer",
        "company": "Northwind",
        "location": "Remote",
        "description": (
            "We need a Python FastAPI engineer to design APIs, write tests, "
            "ship product features, and own reliability for a growing platform."
        ),
    }
    res = client.post("/api/jobs", json=payload)
    assert res.status_code == 200
    job = res.json()
    assert job["title"] == "Backend Engineer"
    assert job["score"] is not None
    assert "cover_letter" in job["analysis"]
    assert "Mourad.Soltani" in job["analysis"]["cover_letter"]
    listed = client.get("/api/jobs")
    assert listed.status_code == 200
    assert any(j["id"] == job["id"] for j in listed.json()["jobs"])
    one = client.get(f"/api/jobs/{job['id']}")
    assert one.status_code == 200
    gone = client.delete(f"/api/jobs/{job['id']}")
    assert gone.status_code == 200


def test_engine_signature():
    profile = "Python FastAPI testing product engineer Mourad Soltani"
    job = "Python FastAPI reliability testing APIs product platform"
    score = fit_score(profile, job)
    assert score["author"] == "Mourad.Soltani"
    assert score["score"] > 0
    bullets = tailor_bullets(profile, job, "Engineer")
    assert any("Mourad.Soltani" in b for b in bullets)
    letter = cover_letter("Mourad Soltani", "Engineer", "Acme", profile, job)
    assert "Mourad.Soltani" in letter
    pack = interview_pack("Engineer", job)
    assert pack["author"] == "Mourad.Soltani"


def test_index_served():
    res = client.get("/")
    assert res.status_code == 200
    assert b"SoltaniHunt" in res.content
    assert b"Mourad.Soltani" in res.content
