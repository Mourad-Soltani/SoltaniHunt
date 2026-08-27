"""SQLite store for SoltaniHunt. Author: Mourad.Soltani"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "soltanihunt.db"
AUTHOR = "Mourad.Soltani"


def connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with connect() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS profile (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                name TEXT NOT NULL,
                headline TEXT,
                summary TEXT,
                skills TEXT,
                author TEXT
            );
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                location TEXT,
                description TEXT NOT NULL,
                url TEXT,
                score REAL,
                analysis TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
        row = conn.execute("SELECT id FROM profile WHERE id = 1").fetchone()
        if not row:
            conn.execute(
                "INSERT INTO profile (id, name, headline, summary, skills, author) VALUES (1, ?, ?, ?, ?, ?)",
                (
                    "Mourad Soltani",
                    "Full-stack engineer & product builder",
                    "I ship reliable web systems, automation, and AI-assisted tools with a bias for clarity and ownership.",
                    json.dumps(
                        [
                            "Python",
                            "FastAPI",
                            "TypeScript",
                            "React",
                            "SQLite",
                            "testing",
                            "product",
                        ]
                    ),
                    AUTHOR,
                ),
            )


def get_profile() -> dict[str, Any]:
    init_db()
    with connect() as conn:
        row = conn.execute("SELECT * FROM profile WHERE id = 1").fetchone()
    data = dict(row)
    data["skills"] = json.loads(data["skills"] or "[]")
    return data


def update_profile(payload: dict[str, Any]) -> dict[str, Any]:
    init_db()
    current = get_profile()
    name = payload.get("name", current["name"])
    headline = payload.get("headline", current["headline"])
    summary = payload.get("summary", current["summary"])
    skills = payload.get("skills", current["skills"])
    if isinstance(skills, str):
        skills = [s.strip() for s in skills.split(",") if s.strip()]
    with connect() as conn:
        conn.execute(
            "UPDATE profile SET name=?, headline=?, summary=?, skills=?, author=? WHERE id=1",
            (name, headline, summary, json.dumps(skills), AUTHOR),
        )
    return get_profile()


def profile_blob() -> str:
    p = get_profile()
    return " ".join(
        [p["name"], p.get("headline") or "", p.get("summary") or "", " ".join(p.get("skills") or [])]
    )


def add_job(payload: dict[str, Any], analysis: dict[str, Any]) -> dict[str, Any]:
    init_db()
    with connect() as conn:
        cur = conn.execute(
            """
            INSERT INTO jobs (title, company, location, description, url, score, analysis)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                payload["title"],
                payload["company"],
                payload.get("location") or "",
                payload["description"],
                payload.get("url") or "",
                analysis.get("score"),
                json.dumps(analysis),
            ),
        )
        job_id = cur.lastrowid
    return get_job(job_id)


def list_jobs() -> list[dict[str, Any]]:
    init_db()
    with connect() as conn:
        rows = conn.execute(
            "SELECT id, title, company, location, url, score, created_at FROM jobs ORDER BY id DESC"
        ).fetchall()
    return [dict(r) for r in rows]


def get_job(job_id: int) -> dict[str, Any] | None:
    init_db()
    with connect() as conn:
        row = conn.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()
    if not row:
        return None
    data = dict(row)
    data["analysis"] = json.loads(data["analysis"] or "{}")
    return data


def delete_job(job_id: int) -> bool:
    init_db()
    with connect() as conn:
        cur = conn.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
        return cur.rowcount > 0
