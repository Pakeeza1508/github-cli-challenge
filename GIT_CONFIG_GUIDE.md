# Git Configuration Guide

## What's In .gitignore

### Root Level (.gitignore)

Excludes from all directories:

```
# Python-related
__pycache__/
*.pyc
*.egg-info/
venv/
.venv
env/

# IDE & Editor
.vscode/
.idea/
*.swp

# OS files
.DS_Store
Thumbs.db

# Environment variables
.env
.env.local
```

### Project Level (gh-focus/.gitignore)

Excludes specific to gh-focus:

```
# Virtual Environment
venv/

# Python cache
__pycache__/
*.pyc

# User-specific files (NOT tracked)
config.json          # Each user customizes
watch_history.json   # Generated during use

# Large executable files
mpv.exe              # Too large (114+ MB)
vlc.exe              # Too large
*.exe                # Any executables
```

---

## What Gets Pushed to GitHub

### ✅ Tracked (Will Be on GitHub)

```
├── README.md
├── SETUP.md
├── HACKATHON_GUIDE.md
├── QUICK_REFERENCE.md
├── PRESENTATION_PACKAGE.md
├── SUBMISSION_SUMMARY.md
├── PRESENTATION_CHECKLIST.md
├── INDEX.md
├── .gitignore
├── .github/
│   └── copilot-instructions.md
└── gh-focus/
    ├── gh-focus              # Main executable
    ├── focus_manager.py      # Python module
    ├── fetcher.py            # Python module
    ├── requirements.txt      # Dependencies
    ├── config.json.sample    # Sample config
    ├── README.md
    ├── GITHUB_CLI_CHALLENGE.md
    └── .gitignore
```

### ❌ NOT Tracked (Local Only)

```
├── venv/                     # Virtual environment
├── config.json               # User's channels
├── watch_history.json        # Generated history
├── __pycache__/              # Python cache
├── gh-focus/mpv.exe          # Large executable
└── .vscode/                  # IDE settings
```

---

## Why This Setup?

### Security
- ✅ `config.json` not shared (user-specific channels)
- ✅ `.env` not shared (no API keys exposed)
- ✅ `watch_history.json` not shared (user privacy)

### Size
- ✅ `mpv.exe` not tracked (114+ MB, exceeds GitHub limit)
- ✅ `venv/` not tracked (redundant, can be recreated)
- ✅ `__pycache__/` not tracked (build artifacts)

### Collaboration
- ✅ Users can have different configs
- ✅ Users can set up their own environment
- ✅ Users can choose their own players (MPV, VLC, browser)

---

## How Users Clone & Set Up

```bash
# Clone from GitHub (small, no mpv.exe)
git clone https://github.com/Pakeeza1508/github-cli-challenge.git
cd github-cli-challenge/gh-focus

# Create environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create their own config
cp config.json.sample config.json
# Edit config.json with their channels

# Run
python gh-focus
```

**GitHub repo size:** ~5 MB (just code + docs)  
**vs with mpv.exe:** ~115 MB (would exceed limits)

---

## If User Wants MPV Support

They can:

1. **Install globally** (recommended)
   ```bash
   winget install mpv
   ```

2. **Or download portable** 
   - Download from: https://mpv.io/installation/
   - Extract to project folder
   - Tool will automatically find it

3. **Or use VLC** (fallback)
   ```bash
   winget install vlc
   ```

---

## Git Commands Users Might Need

### First-time setup
```bash
git clone <repo>
cd github-cli-challenge/gh-focus
cp config.json.sample config.json
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python gh-focus
```

### Keep fork updated
```bash
git fetch origin
git pull origin master
```

### Create local changes (won't affect repo)
```bash
# Edit config.json
python gh-focus

# Run stats
python gh-focus --stats

# Your watch_history.json is local only
```

---

## About .gitignore

### Two-level approach:

**Root .gitignore:**
- Global Python/IDE/OS patterns
- Applies to entire project

**gh-focus/.gitignore:**
- Project-specific patterns
- User config files
- Large executables

### Both are tracked (go to GitHub)
- Users get both when they clone
- Ensures consistent ignore patterns
- Protects their config files

---

## Summary

✅ **GitHub Repo Gets:**
- All Python code
- All documentation
- All configuration samples
- .gitignore files (to protect users)

❌ **GitHub Repo Does NOT Get:**
- Virtual environments (too large, recreatable)
- User config (sensitive, personal)
- Watch history (privacy)
- Executable files (size limits)
- IDE settings (.vscode/, .idea/)

This is the standard Python project setup. Users expect this pattern.

---

## Next Steps

1. Remove mpv.exe from git: `git rm --cached gh-focus/mpv.exe`
2. Stage changes: `git add .gitignore`
3. Commit: `git commit -m "Add .gitignore, remove large files"`
4. Push: `git push`

Then your repo is clean and ready for submission!
