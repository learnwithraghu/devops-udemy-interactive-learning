# Linux Interactive Learning

Learn Linux through hands-on terminal exercises and real-world debugging challenges.

## Quick Start

Visit the deployed site: [https://linux-interactive-learning.pages.dev/](https://linux-interactive-learning.pages.dev/)

## Challenges

### 1. Linux Learn by Doing
**File:** `challenges/linux-learn-by-doing.html`

Learn Linux filesystem through guided terminal commands. 10 stages covering:
- `ls`, `pwd`, `cd`
- Exploring root directories (`/etc`, `/var`, `/home`)
- Understanding directory structure

**Run locally:**
```bash
python3 -m http.server 8000
# Visit http://localhost:8000/challenges/linux-learn-by-doing.html
```

### 2. Server Rescue Challenge
**File:** `challenges/linux-server-rescue.html`

Debug a production server outage. 10-step guided challenge:
- Analyze processes with `top`, `ps`
- Investigate network connections with `ss`, `netstat`
- Read logs to find root cause
- Take corrective action

**Run locally:**
```bash
python3 -m http.server 8000
# Visit http://localhost:8000/challenges/linux-server-rescue.html
```

## Repository Structure

```
linux-interactive-learning/
├── challenges/          # Interactive learning challenges
│   ├── linux-learn-by-doing.html
│   └── linux-server-rescue.html
├── docs/               # Documentation
│   ├── README.md
│   └── DEPLOY.md
└── assets/             # Shared assets (images, icons)
```

## Adding New Challenges

1. Create your HTML file in `challenges/`
2. Follow the naming convention: `challenge-name.html`
3. Update this README with the new challenge
4. Push to deploy

## Deployment

See [docs/DEPLOY.md](docs/DEPLOY.md) for Cloudflare Pages deployment instructions.

## License

MIT License - Feel free to use and modify for educational purposes.