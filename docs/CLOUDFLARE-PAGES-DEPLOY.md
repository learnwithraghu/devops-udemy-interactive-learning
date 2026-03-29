# Deploy to Cloudflare Pages

This guide will help you deploy your Linux learning HTML files to Cloudflare Pages.

## Files to Deploy

- `linux-learn-by-doing.html` - Terminal-based Linux learning experience
- `linux-server-rescue.html` - Debug challenge simulation

---

## Option 1: Deploy via GitHub (Recommended)

### Step 1: Push to GitHub

```bash
cd /Users/raghunandanask/Desktop/github-repo/random

# Initialize git if not already
git init

# Add files
git add linux-learn-by-doing.html linux-server-rescue.html

# Commit
git commit -m "Add Linux learning applications"

# Create repo on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/linux-learning.git
git branch -M main
git push -u origin main
```

### Step 2: Connect to Cloudflare Pages

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Navigate to **Workers & Pages**
3. Click **Create application**
4. Select **Pages** → **Connect to Git**

5. Choose your GitHub repository
6. Configure build settings:
   - **Project name**: `linux-learning`
   - **Production branch**: `main`
   - **Build command**: (leave empty)
   - **Build output directory**: `/`

7. Click **Deploy**

---

## Option 2: Direct Upload

### Step 1: Create a Deployment Package

```bash
cd /Users/raghunandanask/Desktop/github-repo/random

# Create output directory
mkdir -p dist
cp linux-learn-by-doing.html dist/index.html
cp linux-server-rescue.html dist/
```

### Step 2: Deploy via Wrangler

```bash
# Install Wrangler CLI
npm install -g wrangler

# Login to Cloudflare
wrangler login

# Deploy
cd dist
wrangler pages deploy . --project-name=linux-learning
```

Your files will be available at:
- `https://linux-learning.pages.dev/index.html`
- `https://linux-learning.pages.dev/linux-server-rescue.html`

---

## Option 3: Drag & Drop (Quick)

1. Go to [Cloudflare Pages](https://pages.cloudflare.com/)
2. Click **Create a project**
3. Select **Direct upload** tab
4. Drag your `dist` folder (or the individual HTML files)
5. Name your project
6. Click **Deploy**

---

## Custom Domain Setup

### Use a Custom Domain

1. In Cloudflare Pages dashboard, select your project
2. Go to **Custom domains**
3. Click **Add custom domain**
4. Enter your domain (e.g., `learn.yourdomain.com`)
5. Cloudflare will automatically verify and configure SSL

### Subdirectory Approach

If you want URLs like `yourdomain.com/linux-learning/`:

1. Deploy to Cloudflare Workers
2. Configure routing in `wrangler.toml`:

```toml
name = "linux-learning"
main = "src/index.js"
compatibility_date = "2024-01-01"

[[routes]]
pattern = "yourdomain.com/linux-learning/*"
script = "linux-learning"
```

---

## Environment Variables

For enhanced features, add these in Cloudflare Pages settings:

| Variable | Value | Purpose |
|----------|-------|---------|
| `NODE_ENV` | `production` | Enable optimizations |
| `ENABLE_ANALYTICS` | `true` | Track usage (optional) |

---

## Update Workflow

### After GitHub Push

```bash
# Make changes to HTML files
git add .
git commit -m "Update content"
git push

# Cloudflare Pages auto-deploys from main branch
# Check deployment status in dashboard
```

---

## Quick Test Locally

Before deploying, test locally:

```bash
# Using Python
cd /Users/raghunandanask/Desktop/github-repo/random
python3 -m http.server 8000

# Visit http://localhost:8000/linux-learn-by-doing.html
```

---

## Troubleshooting

### CORS Issues
Cloudflare Pages serves from root. Ensure all asset paths are relative.

### Build Failures
Since these are static HTML files, no build process needed. Ensure:
- Build command is empty
- Output directory is `/`

### Cache Issues
After updates, Cloudflare may cache old versions. Add version query:
```html
<script src="app.js?v=1.0.1"></script>
```

Or purge cache in Cloudflare Dashboard → Caching → Configuration → Purge Everything.

---

## Estimated Cost

**Free Tier Includes:**
- 500 builds/month
- Unlimited static assets
- Unlimited requests
- 100 Cloudflare domains

**Pro Plan ($5/month):**
- Unlimited builds
- Analytics
- Instant rollback

---

## Success!

After deployment, share your learning tools at:
- `https://linux-learning.pages.dev/` (index redirects to first file)
- Or custom domain you configured

Your students can now access the Linux learning experience from anywhere!