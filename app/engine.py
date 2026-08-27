"""SoltaniHunt scoring and generation engine. Author: Mourad.Soltani"""

from __future__ import annotations

import re
from collections import Counter
from typing import Iterable

STOP = {
    "the", "and", "for", "with", "that", "this", "from", "your", "you",
    "are", "our", "will", "have", "has", "was", "were", "been", "being",
    "not", "but", "all", "any", "can", "may", "into", "about", "over",
    "such", "than", "then", "them", "they", "their", "what", "when",
    "who", "how", "why", "job", "role", "team", "work", "working",
}

AUTHOR = "Mourad.Soltani"


def tokenize(text: str) -> list[str]:
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9+#.]{1,}", text.lower())
    return [w for w in words if w not in STOP and len(w) > 2]


def keywords(text: str, n: int = 18) -> list[str]:
    counts = Counter(tokenize(text))
    return [w for w, _ in counts.most_common(n)]


def fit_score(profile_text: str, job_text: str) -> dict:
    p = set(tokenize(profile_text))
    j = set(tokenize(job_text))
    if not j:
        return {"score": 0.0, "matched": [], "missing": [], "author": AUTHOR}
    matched = sorted(p & j)
    missing = sorted(j - p)
    score = round(100.0 * len(matched) / max(len(j), 1), 1)
    return {
        "score": min(score, 99.9),
        "matched": matched[:24],
        "missing": missing[:24],
        "author": AUTHOR,
    }


def tailor_bullets(profile: str, job: str, title: str) -> list[str]:
    miss = fit_score(profile, job)["missing"][:6]
    skills = keywords(profile, 8)
    skill_line = ", ".join(skills[:4]) or "core engineering skills"
    bullets = [
        f"Delivered outcomes aligned with {title} using {skill_line}. — Mourad.Soltani",
        "Translated ambiguous product requirements into shipped, measurable features.",
        "Partnered with stakeholders to reduce cycle time and raise quality bars.",
    ]
    if miss:
        bullets.append(
            f"Ready to deepen: {', '.join(miss[:4])} to close remaining gaps for this role."
        )
    return bullets


def cover_letter(name: str, title: str, company: str, profile: str, job: str) -> str:
    score = fit_score(profile, job)["score"]
    kws = keywords(job, 6)
    focus = ", ".join(kws[:4]) if kws else "the posted priorities"
    return (
        f"Dear {company} hiring team,\n\n"
        f"I am {name} applying for {title}. My background maps at {score}% "
        f"to the posting, especially around {focus}.\n\n"
        f"{profile.strip()[:420]}\n\n"
        f"I would welcome a conversation about how I can contribute at {company}.\n\n"
        f"Sincerely,\n{name}\n— drafted with SoltaniHunt by Mourad.Soltani\n"
    )


def interview_pack(title: str, job: str) -> dict:
    kws = keywords(job, 10)
    behavioral = [
        f"Tell me about a time you owned work related to {kws[0]}." if kws else "Tell me about a high-impact project.",
        "Describe a disagreement with a stakeholder and how you resolved it.",
        "Walk through a failure, what you learned, and what changed after.",
    ]
    technical = [
        f"How would you design a system that supports {kws[1]}?" if len(kws) > 1 else "How do you design for reliability?",
        "How do you measure success for this role in the first 90 days?",
        "What would you automate first on this team, and why?",
    ]
    return {
        "role": title,
        "behavioral": behavioral,
        "technical": technical,
        "talking_points": kws[:8],
        "author": AUTHOR,
    }


def normalize_iterable(items: Iterable[str]) -> list[str]:
    return [i.strip() for i in items if i and i.strip()]
