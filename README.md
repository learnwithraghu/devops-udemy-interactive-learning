# 🐧 Linux Interactive Learning

Interactive, browser-based Linux terminal challenges — designed to be **embedded directly into course content** via iframes.  
No installation. No backend. Just open a URL and learn by doing.

🌐 **Live Site:** [https://linux-interactive-learning.pages.dev](https://linux-interactive-learning.pages.dev)

---

## How It Works

Each challenge is a single self-contained HTML file served at a **clean short URL**:

```
https://your-project.pages.dev/lx-filesystem
https://your-project.pages.dev/lx-server-rescue
```

Embed any challenge into your course with a simple iframe:

```html
<iframe
  src="https://your-project.pages.dev/lx-filesystem"
  width="100%"
  height="650px"
  frameborder="0"
  allow="fullscreen"
  title="Linux Filesystem Explorer"
></iframe>
```

---

## Available Challenges

| Slug | Title | Difficulty | Status |
|------|-------|------------|--------|
| `/lx-filesystem` | Linux Filesystem Explorer | Beginner | ✅ Live |
| `/lx-server-rescue` | Server Rescue Challenge | Intermediate | ✅ Live |

> **Admin Dashboard:** `/admin` — lists all challenges with copyable URLs and embed codes.

---

## Repository Structure

```
linux-interactive-learning/
├── index.html              ← Public landing page (/)
├── admin.html              ← Master dashboard (/admin)
├── _redirects              ← Cloudflare URL rewrites (/slug → /challenges/slug)
│
├── challenges/             ← All challenge HTML files
│   ├── lx-filesystem.html
│   ├── lx-server-rescue.html
│   └── (add new ones here)
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
- `http://localhost:8000/challenges/lx-filesystem.html` — filesystem challenge
- `http://localhost:8000/challenges/lx-server-rescue.html` — server rescue

> Note: Short URL rewrites (`/lx-filesystem`) only work on Cloudflare Pages, not locally. Use the full `/challenges/filename.html` path when testing locally.

---

## License

MIT — Free to use and modify for educational purposes.