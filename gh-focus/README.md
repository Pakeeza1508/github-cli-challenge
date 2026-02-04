# 🎯 gh-focus

> **A distraction-free YouTube CLI for intentional learning**

Stop doom-scrolling. Start learning with purpose.

## The Problem

You open YouTube to watch *one* Docker tutorial. Three hours later, you're watching shark tank compilations. YouTube's algorithm is engineered to keep you on the platform, not to help you learn.

## The Solution

`gh-focus` is a GitHub CLI extension that acts as your **Headless YouTube Client**:

- ✅ **Curated** - Only shows content from your whitelist
- ✅ **Context-Aware** - Switch between "Coding," "Business," or "Entertainment" modes
- ✅ **Distraction-Free** - Opens videos in embed mode with NO sidebar, NO comments, NO recommendations

## Installation

```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/gh-focus.git
cd gh-focus

# Install dependencies
pip install -r requirements.txt

# Install as GitHub CLI extension
gh extension install .
```

## Usage

```bash
# Launch the focus mode
gh focus

# The tool will:
# 1. Ask what you want to focus on (Coding/Business/Entertainment)
# 2. Fetch latest videos from YOUR whitelisted channels only
# 3. Let you select with arrow keys
# 4. Open in distraction-free mode (no sidebar, no recommendations)
```

## Quick Start

### Add Your First Channel

1. Run `gh focus`
2. Select `+ Add New Channel`
3. Choose a category (e.g., "coding")
4. Enter channel name (e.g., "Fireship")
5. Enter channel ID (e.g., "UCsBjURrPoezykLs9EqgamOA")

**How to find a Channel ID:**
1. Go to the YouTube channel
2. Right-click → View Page Source
3. Search for `"channelId"` or look at the URL if it contains `/channel/UC...`

### Sample Configuration

The tool stores your channels in `config.json`:

```json
{
    "coding": [
        { "name": "Fireship", "id": "UCsBjURrPoezykLs9EqgamOA" },
        { "name": "Traversy Media", "id": "UC29ju8bIPH5as8OGnQzwJyA" }
    ],
    "business": [
        { "name": "Y Combinator", "id": "UCcefcZRL2oaA_uBNeo5UOWg" }
    ],
    "entertainment": []
}
```

## Features

### 🎯 Focus Modes
Switch between different content categories based on your current goal.

### 🚫 Algorithm-Free
Uses YouTube RSS feeds instead of the API - no recommendations, no distractions.

### ⚡ Fast & Lightweight
Python-based CLI that runs locally. No server, no complex setup.

### 🎨 Beautiful UI
Powered by `rich` and `questionary` for a modern terminal experience.

## Tech Stack

- **Python 3.7+** - Core language
- **feedparser** - Fetch YouTube RSS feeds (no API key needed!)
- **questionary** - Interactive CLI prompts
- **rich** - Beautiful terminal formatting
- **webbrowser** - Open videos in your default browser

## Why This Matters

This project demonstrates:
- Real-world problem-solving (developer productivity)
- Creative use of RSS over API (no quota limits)
- Clean Python architecture
- User-focused design (arrow keys, not typing URLs)

## Roadmap

- [x] Basic channel whitelist
- [x] Category-based filtering
- [x] Distraction-free video player
- [ ] Pomodoro timer integration
- [ ] Learning progress tracker
- [ ] Automatic channel ID extraction from URL
- [ ] Export watch history

## Contributing

This is a GitHub CLI Challenge 2026 submission, but feel free to fork and improve!

## License

MIT

---

**Built for the GitHub CLI Challenge 2026** 🚀  
*Because focus is a superpower.*
