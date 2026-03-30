# 🐧 Linux Interactive Learning

Interactive, browser-based Linux terminal challenges — designed to be **embedded directly into course content** via iframes.  
No installation. No backend. Just open a URL and learn by doing.

🌐 **Live Site:** [https://linux-interactive-learning.pages.dev](https://linux-interactive-learning.pages.dev)

---

## How It Works

Each challenge is a single self-contained HTML file served at a **clean short URL**:

```
https://linux-interactive-learning.pages.dev/lx-filesystem
https://linux-interactive-learning.pages.dev/lx-server-rescue
… (see table below for every slug)
```

Embed any challenge into your course (or Udemy supplementary materials) with a simple iframe:

```html
<iframe
  src="https://linux-interactive-learning.pages.dev/lx-filesystem"
  width="100%"
  height="650px"
  frameborder="0"
  allow="fullscreen"
  title="Mis-deployed artifact"
></iframe>
```

---

## Hands-on challenges

Each link opens a **browser-based, hands-on** terminal simulation (no install). Add your **Udemy** (or course) lecture links in the **Course link** column when you publish.

**Base URL:** `https://linux-interactive-learning.pages.dev` — each challenge is `/<slug>` (e.g. `/lx-filesystem`).

| Slug | Hands-on title | One-line description | Course link |
|------|----------------|----------------------|-------------|
| `/lx-filesystem` | **Mis-deployed artifact** | Wrong-path release: trace configs and logs with `ls`, `pwd`, `cd`, hidden files, and key dirs (`/`, `/home`, `/etc`, `/var`). Ends with the same commands-and-notes recap as other challenges. | |
| `/lx-server-rescue` | **Hands-On Server Rescue Lab** | Diagnose a simulated outage with `top`, `ss`, logs, `kill`, and `systemctl`—like a mini on-call. | |
| `/lx-log-detective` | **Hands-On Log Forensics** | Trace failures in app logs using `grep`, `tail`, `sort`, `uniq`, and counting patterns. | |
| `/lx-permissions` | **Hands-On Permissions & Ownership** | Fix “permission denied” with `ls -l`, `chmod`, `chown`, `umask`, and reading modes. | |
| `/lx-pipelines` | **Hands-On Shell Pipelines** | Slice CSV-style data with `cut`, `sort`, `uniq`, `grep`, `awk`, and classic pipes. | |
| `/lx-disk-space` | **Hands-On Disk & Storage Triage** | Find what’s filling the disk with `df`, `du`, and `find` before services fail. | |

### Descriptions (for syllabi or Udemy sections)

1. **Mis-deployed artifact** — Incident-style walkthrough: same navigation skills ops use when a bundle is on the wrong path (home → root → `/etc` / `/var` and back), then a recap of the commands you used and short notes.  
2. **Hands-On Server Rescue Lab** — Step-through incident: processes, sockets, MySQL logs, killing a stuck PID, restarting a service.  
3. **Hands-On Log Forensics** — Investigate a realistic app outage using log listing, tail, grep, counts, and ranked error types.  
4. **Hands-On Permissions & Ownership** — Read `ls -l` output and apply `chmod` / `chown` / `umask` so scripts and services behave correctly.  
5. **Hands-On Shell Pipelines** — Build data pipelines: preview files, cut columns, sort/dedupe, rank frequencies, filter, and quick `awk` totals.  
6. **Hands-On Disk & Storage Triage** — Use `df` and `du` to locate heavy directories and `find` for oversized or stale files.

> **Admin:** use `https://<your-domain>/admin.html` — lists all challenges with copyable URLs and embed codes. (On **Cloudflare Workers** with static assets, avoid `/admin` rewrite rules; they can cause redirect loops. Use `admin.html` directly.)

---

## Repository Structure

```
linux-interactive-learning/
├── index.html              ← Public landing page (/)
├── admin.html              ← Master dashboard (open as /admin.html)
├── _redirects              ← Cloudflare URL rewrites (/slug → /challenges/slug)
│
├── challenges/             ← All challenge HTML files
│   ├── lx-filesystem.html
│   ├── lx-server-rescue.html
│   ├── lx-log-detective.html
│   ├── lx-permissions.html
│   ├── lx-pipelines.html
│   └── lx-disk-space.html
│
├── assets/                 ← Shared assets (images, icons)
├── docs/
│   └── CLOUDFLARE-PAGES-DEPLOY.md
└── README.md
```

---

## 🚀 Deploying to Cloudflare Pages (Drag & Drop)

### First-Time Setup

1. Go to [dash.cloudflare.com](https://dash.cloudflare.com)
2. Navigate to **Workers & Pages** in the left sidebar
3. Click **Create** (top right)
4. Select the **Pages** tab
5. Click **"Upload assets"** _(NOT "Connect to Git")_
6. Give your project a name, e.g. `linux-interactive-learning`
7. Click **"Create project"**
8. Drag the **entire project folder** into the upload area
9. Click **"Deploy site"**

**Settings to choose:**
- Build command: _(leave empty)_
- Build output directory: _(leave empty)_
- `_redirects` file is picked up automatically — no config needed

Your site is live at `https://your-project-name.pages.dev` instantly.

---

### Updating / Adding New Challenges

1. Add your new challenge HTML to `challenges/`
2. Add a rewrite line to `_redirects`
3. Add the entry to the `challenges` array in `admin.html`
4. Go to [dash.cloudflare.com](https://dash.cloudflare.com) → **Workers & Pages** → your project
5. Click **"Create new deployment"** → Upload the full folder again

> ⚡ Each drag & drop replaces the previous deployment. Always drag the **full folder** (not just changed files).

---

## Adding a New Challenge

### Step 1 — Create the HTML file
Add your challenge to the `challenges/` folder:
```
challenges/lx-your-topic.html
```

### Step 2 — Add the URL rewrite
Open `_redirects` and add one line:
```
/lx-your-topic   /challenges/lx-your-topic   200
```
The `200` code means a **transparent rewrite** — the URL stays as `/lx-your-topic` in the browser (perfect for iframes).

### Step 3 — Register it in admin
Open `admin.html`, find the `challenges` array in the `<script>` section, and add:
```javascript
{
  slug: 'lx-your-topic',
  title: 'Your Challenge Title',
  description: 'What students will learn and do.',
  difficulty: 'Beginner',       // Beginner | Intermediate | Advanced
  tags: ['tag1', 'tag2'],
  status: 'live'                // live | coming-soon
}
```

### Step 4 — Deploy
Drag & drop the full folder to Cloudflare Pages. Done.

---

## Running Locally

```bash
cd linux-interactive-learning
python3 -m http.server 8000
```

Then visit:
- `http://localhost:8000` — landing page
- `http://localhost:8000/admin.html` — admin dashboard
- `http://localhost:8000/challenges/lx-<slug>.html` — any challenge (e.g. `lx-filesystem.html`, `lx-pipelines.html`)

> Note: Short URL rewrites (`/lx-filesystem`) only work on Cloudflare Pages, not locally. Use the full `/challenges/filename.html` path when testing locally.

---

## License

MIT — Free to use and modify for educational purposes.