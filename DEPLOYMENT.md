# 🚀 Deployment Guide: gh-focus

## Current Status

Your repository: `github-cli-challenge`  
GitHub CLI requirement: Extensions must have repos named `gh-*`

## Deployment Options

### Option 1: Rename Repository (Recommended for GitHub CLI Extension)

1. Go to: https://github.com/Pakeeza1508/github-cli-challenge/settings
2. Scroll to "Repository name"  
3. Change to: `gh-focus`
4. Click "Rename"

**Then users can install with:**
```bash
gh extension install Pakeeza1508/gh-focus
```

### Option 2: Keep Current Name (Hackathon Submission)

Keep `github-cli-challenge` as-is and provide manual installation.

**Users install with:**
```bash
# Clone the repo
git clone https://github.com/Pakeeza1508/github-cli-challenge.git
cd github-cli-challenge/gh-focus

# Setup
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt

# Run
python gh-focus
```

---

## Testing Installation (Current Method)

Since the repo isn't named `gh-*` yet, test manually:

```powershell
# Navigate to project
cd C:\Users\Pakeeza\github-cli-challenge\gh-focus

# Activate environment
.\venv\Scripts\Activate.ps1

# Run
python gh-focus
```

**Expected output:**
```
╭────────────────────────────────╮
│ 🎯 YouTube Focus Mode          │
│ Curated. Intentional. Focused. │
╰────────────────────────────────╯
? What is your focus right now?
```

---

## For Hackathon: What to Tell Judges

**Current Installation (Manual):**
```bash
git clone https://github.com/Pakeeza1508/github-cli-challenge.git
cd github-cli-challenge/gh-focus
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
python gh-focus
```

**Future Vision (After Rename):**
```bash
gh extension install Pakeeza1508/gh-focus
gh focus
```

Tell judges: "We're keeping the challenge repo name for submission. After the hackathon, this will be renamed to `gh-focus` and installable via `gh extension install`."

---

## Deployment Checklist

### Pre-Hackathon (Current)
- ✅ Code works locally
- ✅ Documentation complete
- ✅ Pushed to GitHub
- ✅ Ready to demo

### Post-Hackathon (If You Win/Want to Publish)
- [ ] Rename repo to `gh-focus`
- [ ] Test `gh extension install`
- [ ] Add to gh extension marketplace
- [ ] Update all documentation links
- [ ] Announce on social media

---

## Quick Test Commands

```powershell
# Test the app works
cd C:\Users\Pakeeza\github-cli-challenge\gh-focus
python gh-focus

# Test stats work
python gh-focus --stats

# Test help works
python gh-focus --help
```

---

## Installation Instructions for README

Add this to your README.md:

```markdown
## Installation

### Manual Installation (Current)

\`\`\`bash
git clone https://github.com/Pakeeza1508/github-cli-challenge.git
cd github-cli-challenge/gh-focus
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp config.json.sample config.json
python gh-focus
\`\`\`

### GitHub CLI Extension (Coming Soon)

After the hackathon:
\`\`\`bash
gh extension install Pakeeza1508/gh-focus
gh focus
\`\`\`
```

---

## Summary

**For Hackathon Submission:**
- Keep current name `github-cli-challenge`
- Provide manual installation
- Show it works perfectly
- Mention future `gh extension` support

**After Hackathon:**
- Rename to `gh-focus`
- Enable `gh extension install`
- Publish to marketplace

**Right Now:**
Your project is **deployed** (on GitHub) and **installable** (manually). That's sufficient for hackathon judging!

---

## Try It Now

```powershell
gh extension install https://github.com/Pakeeza1508/github-cli-challenge
```

This might work even without the `gh-` prefix. Let's see!
