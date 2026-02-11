# 🚀 Installation Guide for gh-focus

Complete setup instructions for Windows, macOS, and Linux.

---

## Prerequisites

- **Python 3.7+** - [Download](https://www.python.org/downloads/)
- **GitHub CLI** (optional, for full CLI integration) - [Download](https://cli.github.com)
- **pip** - Usually comes with Python

### Check Your Setup

```bash
python --version    # Should be 3.7 or higher
pip --version       # Should work without errors
```

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/github-cli-challenge.git
cd github-cli-challenge/gh-focus
```

### Step 2: Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Expected output:
```
Successfully installed feedparser-6.0.10 questionary-1.10.0 rich-13.3.1
```

### Step 4: Copy Sample Config (Optional)

```bash
# Windows
copy config.json.sample config.json

# macOS/Linux
cp config.json.sample config.json
```

---

## Running gh-focus

### Interactive Mode (Main)

```bash
python gh-focus
```

The tool will:
1. Show a welcome banner
2. Ask what you want to focus on (Coding/Business/Learning)
3. Fetch latest videos from your channels
4. Let you select a video
5. Open it in your chosen player

### View Statistics

```bash
python gh-focus --stats
```

Shows:
- Total videos watched
- Total learning time
- Breakdown by category
- Recent videos

### Get Help

```bash
python gh-focus --help
```

---

## Setting Up Your Video Player

The tool supports three players (in order of preference):

### Option 1: MPV (Recommended - Best Experience)

**Why MPV?**
- Lightweight and distraction-free
- Fast startup
- Works with YouTube through yt-dlp
- Best performance

**Windows:**
```powershell
winget install mpv
```

Or download from: https://mpv.io/installation/

**macOS:**
```bash
brew install mpv
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install mpv
```

**Verify Installation:**
```bash
mpv --version
```

### Option 2: VLC (Fallback)

If MPV is unavailable, the tool falls back to VLC.

**Windows:**
```powershell
winget install vlc
```

**macOS:**
```bash
brew install vlc
```

**Linux:**
```bash
sudo apt-get install vlc
```

### Option 3: Browser (Default Fallback)

If no players are found, videos open in your default browser.

---

## Adding Your First Channel

### Method 1: Interactive CLI

```bash
python gh-focus
# Select "+ Add New Channel"
# Enter category, channel name, and channel ID
```

### Method 2: Edit config.json Directly

```json
{
    "coding": [
        {
            "name": "Fireship",
            "id": "UCsBjURrPoezykLs9EqgamOA"
        }
    ]
}
```

### Finding Channel IDs

**Option A: YouTube URL**
- Visit the channel page
- URL format: `https://www.youtube.com/@channelname` or `https://www.youtube.com/channel/UC...`
- Copy the ID after `/channel/` or search for it in the page source

**Option B: View Page Source**
1. Right-click on the channel page → "View Page Source"
2. Press Ctrl+F and search for `"channelId":"UC`
3. Copy the full ID (starts with UC)

**Option C: Use Python Helper (Future)**
```bash
python -c "from fetcher import extract_channel_id; print(extract_channel_id('https://youtube.com/@fireship'))"
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'questionary'"

**Solution:** Virtual environment not activated or dependencies not installed.

```bash
# Activate virtual environment
Windows: .\venv\Scripts\Activate.ps1
macOS/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Issue: Videos open in browser instead of MPV

**Why:** MPV is not installed or not in PATH.

**Solutions:**
1. Install MPV (see above)
2. Or copy `mpv.exe` directly into the gh-focus folder
3. Use VLC as fallback

### Issue: "No recent videos found"

**Possible causes:**
- Channel hasn't posted in a while
- Channel ID is incorrect
- YouTube RSS is temporarily down

**Fix:**
- Try adding a different channel
- Verify channel ID is correct (starts with UC)
- Check internet connection

### Issue: "Error fetching from channel"

**Possible causes:**
- Invalid channel ID
- Channel marked as private
- Network timeout

**Fix:**
- Double-check channel ID
- Use a public channel
- Try again later

---

## Advanced Setup

### Creating an Alias (Optional)

**Windows (PowerShell):**
```powershell
# Add to PowerShell profile
notepad $PROFILE

# Add this line:
function gh-focus { python C:\Users\YOUR_USERNAME\github-cli-challenge\gh-focus\gh-focus }
```

**macOS/Linux:**
```bash
# Add to ~/.bashrc or ~/.zshrc
echo 'alias gh-focus="python ~/github-cli-challenge/gh-focus/gh-focus"' >> ~/.bashrc
source ~/.bashrc
```

Then run anywhere:
```bash
gh-focus
```

### GitHub CLI Integration (Coming Soon)

Once GitHub CLI extension support is finalized:

```bash
gh extension install https://github.com/YOUR_USERNAME/github-cli-challenge
gh focus
```

---

## Next Steps

1. **Add your favorite channels** to `config.json`
2. **Run `python gh-focus`** and try it out
3. **View your stats** with `python gh-focus --stats`
4. **Star the repo** if you find it useful! ⭐

---

## Getting Help

- Check the [README.md](README.md) for feature overview
- Review [config.json.sample](config.json.sample) for examples
- Open an issue on GitHub with the error message

---

**Enjoy distraction-free learning! 🎯**
