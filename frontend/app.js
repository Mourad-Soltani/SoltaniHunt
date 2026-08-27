/* SoltaniHunt client — Mourad.Soltani */
async function json(url, opts) {
  const res = await fetch(url, opts);
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

async function loadHealth() {
  const el = document.getElementById("health");
  try {
    const h = await json("/api/health");
    el.textContent = h.ok ? `healthy · ${h.author}` : "down";
    el.classList.toggle("ok", h.ok);
  } catch {
    el.textContent = "offline";
  }
}

async function loadProfile() {
  const p = await json("/api/profile");
  const f = document.getElementById("profile-form");
  f.name.value = p.name || "";
  f.headline.value = p.headline || "";
  f.summary.value = p.summary || "";
  f.skills.value = (p.skills || []).join(", ");
}

async function loadJobs() {
  const data = await json("/api/jobs");
  const root = document.getElementById("jobs");
  if (!data.jobs.length) {
    root.innerHTML = "<p>No postings yet. Mourad.Soltani</p>";
    return;
  }
  root.innerHTML = data.jobs
    .map(
      (j) => `<div class="job" data-id="${j.id}">
        <strong>${j.title}</strong> · ${j.company}
        <div class="score">${j.score ?? "—"}% fit</div>
      </div>`
    )
    .join("");
  root.querySelectorAll(".job").forEach((el) => {
    el.onclick = () => showJob(el.dataset.id);
  });
}

async function showJob(id) {
  const job = await json(`/api/jobs/${id}`);
  const box = document.getElementById("detail");
  box.hidden = false;
  document.getElementById("pack").textContent = JSON.stringify(job, null, 2);
}

document.getElementById("profile-form").onsubmit = async (e) => {
  e.preventDefault();
  const f = e.target;
  await json("/api/profile", {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: f.name.value,
      headline: f.headline.value,
      summary: f.summary.value,
      skills: f.skills.value,
    }),
  });
  await loadProfile();
};

document.getElementById("job-form").onsubmit = async (e) => {
  e.preventDefault();
  const f = e.target;
  const job = await json("/api/jobs", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: f.title.value,
      company: f.company.value,
      location: f.location.value,
      url: f.url.value,
      description: f.description.value,
    }),
  });
  f.reset();
  await loadJobs();
  await showJob(job.id);
};

loadHealth();
loadProfile();
loadJobs();
