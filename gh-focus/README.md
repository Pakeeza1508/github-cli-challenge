# 🎯 gh-focus

> **GitHub CLI Extension for Distraction-Free Learning**

A GitHub CLI extension that transforms YouTube into a productivity tool by curating content and eliminating algorithmic distractions.

![GitHub CLI](https://img.shields.io/badge/Built%20For-GitHub%20CLI-white?logo=github&style=for-the-badge)
![Python](https://img.shields.io/badge/Made%20With-Python%20%2B%20Rich-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🏆 GitHub CLI Challenge 2026

**Challenge:** Build a GitHub CLI extension that solves a real-world problem for developers.

**Our Solution:** A learning-focused YouTube client that prevents context-switching and algorithmic distraction while working.

### Why This Matters for GitHub CLI Ecosystem

Most GitHub CLI extensions are workflow-automation tools. **gh-focus** is different—it's a **developer wellness extension** that:

- ✅ Keeps you focused on intentional learning (not doom-scrolling)
- ✅ Works offline after initial setup (uses local config)
- ✅ Integrates seamlessly with developer workflow (`gh focus` = quick context switch)
- ✅ Demonstrates creative use of GitHub CLI for non-traditional use cases

---

## The Problem

**The Developer's Dilemma:**
- You open YouTube to watch a Docker tutorial
- 30 minutes in, the algorithm recommends a 2-hour conference talk
- 3 hours later, you're watching "Top 10 Programming Fails" compilation
- Your focus session is destroyed

**Why YouTube's Algorithm is Evil for Developers:**
- Designed to maximize watch time (not learning outcomes)
- Recommendation sidebar = constant context switching
- Comments section = distraction goldmine
- Shorts feed = attention fragmentation

---

## The Solution: gh-focus

A GitHub CLI extension that acts as your **Personal Learning Curator**:

```bash
$ gh focus
? What is your focus right now? Coding
? 📺 CODING - Select video: [Fireship] Docker in 100 Seconds
🛡️ Opening in MPV (Safe Mode)...
```

### Key Features

| Feature | How It Helps |
|---------|-------------|
| **Channel Whitelisting** | Only see content from creators YOU trust |
| **Context Categories** | Switch between Coding/Business/Learning modes |
| **No Algorithm** | RSS feeds, not API recommendations |
| **Distraction-Free Player** | MPV → VLC → Browser (all remove sidebars) |
| **Learning Log (Gist Sync)** | Save great videos to a single GitHub Gist checklist |
| **Watch History** | Track what you learned and when |
| **Local-First** | Config stored locally, no tracking |

---

## Installation

### Prerequisites
- GitHub CLI installed (`gh --version`)
- Logged in to GitHub (`gh auth login`)
- Python 3.7+
- pip

### Install as a GitHub CLI Extension (Recommended)

```bash
gh extension install Pakeeza1508/gh-focus
gh focus
```

**First Run Setup:**
The app will show you how to install MPV for ad-free playback (one command, run once!).

### Quick Setup (Local Development)

**Windows:**
```powershell
# Clone the repo
git clone https://github.com/Pakeeza1508/github-cli-challenge.git
cd github-cli-challenge/gh-focus

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run directly
python gh-focus.py
```

**macOS/Linux:**
```bash
git clone https://github.com/Pakeeza1508/github-cli-challenge.git
cd github-cli-challenge/gh-focus

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python gh-focus.py
```

---

## 🎬 Enable Ad-Free Video Playback (CRITICAL)

**Why This Matters:** Without a player, videos open in YouTube browser (full ads, distractions). With MPV, you get distraction-free playback.

### ⭐ Install MPV (One-Time Setup)

**Windows (Recommended - easiest):**
```powershell
winget install io.mpv.mpv
```

**Alternative on Windows:**
```powershell
# Using Chocolatey
choco install mpv
```

**macOS:**
```bash
brew install mpv
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install mpv
```

**After installation:**
```bash
gh focus  # Restart the app
```

The app automatically detects MPV and activates **Ad-Free Distraction-Free Mode**! ✨

### Option B: Use VLC Instead

If MPV doesn't work for you:

**Windows:**
```powershell
winget install VideoLAN.VLC
```

**macOS:**
```bash
brew install vlc
```

**Linux:**
```bash
sudo apt-get install vlc
```

---

## Video Player Priority

The app tries these players in order (stops at first found):

1. **MPV** (Recommended) - Lightweight, blazing fast, zero ads
2. **VLC** - Popular, reliable fallback  
3. **Browser** (Fallback only) - Full YouTube experience with ads

If none are installed, you'll see setup instructions on first run.

### Optional: Install MPV (Recommended)

**Windows:**
```powershell
winget install mpv
```

**macOS:**
```bash
brew install mpv
```

**Linux:**
```bash
sudo apt-get install mpv
```

---

## How to Use

### 1. Add Your First Channel

```bash
$ python gh-focus
? What is your focus right now? + Add New Channel
? Which category? coding
? Channel Name: Fireship
? Channel ID: UCsBjURrPoezykLs9EqgamOA
✓ Added Fireship to coding!
```

**Finding Channel IDs:**
1. Visit the YouTube channel
2. Right-click → View Page Source
3. Search for `"channelId":"UC..."`

### 2. Select & Watch

```bash
? 📺 CODING - Select video: [Fireship] Docker in 100 Seconds
🛡️ Opening in MPV (Safe Mode)...
```

### 3. View Your Stats

```bash
$ python gh-focus --stats
📊 Watch History:
  ✓ Docker in 100 Seconds (2025-02-11)
  ✓ Git Tutorial (2025-02-10)
  ✓ Python Tips (2025-02-09)
Total learned: 3h 45m
```

### 4. Save to Learning Log (Gist Sync)

```bash
? Action for: Docker in 100 Seconds
    📺 Stream (Watch Now)
    💾 Save to Learning Log
    🔙 Cancel
```

When you save, `gh-focus` appends the video to a single GitHub Gist named `focus_learning_log.md` so your watch list follows you across machines.

---

## Pre-Configured Channels

The tool comes with a sample config (`config.json.sample`):

```json
{
    "coding": [
        { "name": "Fireship", "id": "UCsBjURrPoezykLs9EqgamOA" },
        { "name": "Traversy Media", "id": "UC29ju8bIPH5as8OGnQzwJyA" },
        { "name": "Web Dev Simplified", "id": "UCFbNIlppjreqWp0LoG4qLDg" }
    ],
    "business": [
        { "name": "Y Combinator", "id": "UCcefcZRL2oaA_uBNeo5UOWg" },
        { "name": "Ali Abdaal", "id": "UCoOae5nYzcosPVc4DescXIQ" }
    ],
    "learning": [
        { "name": "3Blue1Brown", "id": "UCYO_jab_esuFRV4b0cTApqQ" },
        { "name": "Kurzgesagt", "id": "UCzIL6qFP00w10hgxZwplZww" }
    ]
}
```

Copy to `config.json` and customize!

---

## Tech Stack

- **Python 3.7+** - Core language
- **feedparser** - YouTube RSS feeds (no API key required!)
- **questionary** - Beautiful interactive CLI
- **rich** - Terminal formatting
- **subprocess** - Player integration (MPV/VLC)
- **json** - Config persistence

### Why This Stack?

- **No API Key:** YouTube RSS feeds work forever, no quota limits
- **Lightweight:** Single Python file, minimal dependencies
- **User-Friendly:** Rich UI feels modern and responsive
- **Extensible:** Easy to add new players, categories, features

---

## Architecture

```
gh-focus/
├── gh-focus           # Main CLI (focus manager logic)
├── fetcher.py        # Fetch videos from RSS feeds
├── focus_manager.py  # Config/category management
├── config.json       # User's channel whitelist
└── requirements.txt  # Dependencies
```

### How It Works

1. **Load Config** → Read user's whitelisted channels
2. **Fetch Videos** → Parse YouTube RSS feeds (real-time, no API)
3. **Filter & Display** → Show latest videos from whitelist only
4. **Launch Player** → Open in MPV/VLC/Browser (no sidebar)
5. **Log Watch** → Track view in history
6. **Sync Learning Log** → Append to a shared Gist via GitHub CLI

---

## Why This is a Great GitHub CLI Extension

### 1. **Solves Real Developer Problem**
GitHub CLI extensions should enhance developer workflow. This one prevents distraction—a critical issue in knowledge work.

### 2. **Goes Beyond Automation**
Most CLI extensions automate GitHub operations. This demonstrates CLI can solve adjacent problems (learning, focus).

### 3. **Offline-First Design**
After setup, works completely offline. No dependency on external APIs or services.

### 4. **Clean Python Implementation**
Shows best practices: modularity, error handling, user feedback, config management.

### 5. **Extensible Architecture**
Easy to add: Pomodoro timer, progress tracking, channel auto-discovery, etc.

---

## Roadmap

- [x] Basic channel whitelist
- [x] Category-based filtering  
- [x] Multiple player support (MPV, VLC, Browser)
- [x] Beautiful CLI interface
- [x] Watch history tracking
- [x] Learning stats dashboard
- [x] Learning Log Gist sync
- [ ] Pomodoro timer integration
- [ ] Auto-extract channel IDs from URLs
- [ ] Sync channels via GitHub Gists
- [ ] Browser extension for direct integration

---

## Demo Scenario (For Hackathon Judging)

**Time: 2 minutes**

1. **Show the problem** (30 seconds)
   - Open YouTube → Show algorithmic chaos
   - "This is why developers lose 3 hours daily"

2. **Show gh-focus** (60 seconds)
   - Run `python gh-focus`
   - Select "coding" category
   - Show curated list (no distractions)
   - Open video in MPV
   - "Notice: no sidebar, no comments, no algorithm"

3. **Show the code** (30 seconds)
   - Point to `fetcher.py` → "RSS feeds, no API key"
   - Point to `focus_manager.py` → "Simple JSON config"
   - "Easy to extend, easy to customize"

**Closing:** "GitHub CLI isn't just for GitHub operations. It's for developer wellness."

---

## Contributing

This is a GitHub CLI Challenge 2026 submission. Community contributions welcome!

---

## License

MIT - Feel free to fork and build on this!

---

**🚀 GitHub CLI Challenge 2026 Submission**

*Built for developers who value their focus.*
