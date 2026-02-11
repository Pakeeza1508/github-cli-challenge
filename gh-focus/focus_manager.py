import json
import os
from datetime import datetime

# Where we store data
CONFIG_FILE = "config.json"
HISTORY_FILE = "watch_history.json"

# Default structure
DEFAULT_CONFIG = {
    "coding": [],
    "business": [],
    "entertainment": []
}

def load_config():
    """Load configuration from JSON file, create if doesn't exist."""
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG
    
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(data):
    """Save configuration to JSON file."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_channel(category, name, channel_id):
    """Add a channel to a specific category."""
    data = load_config()
    if category not in data:
        data[category] = []
    
    # Avoid duplicates
    for ch in data[category]:
        if ch['id'] == channel_id:
            return False
            
    data[category].append({"name": name, "id": channel_id})
    save_config(data)
    return True

def get_channels(category):
    """Get all channels in a specific category."""
    data = load_config()
    return data.get(category, [])

def list_all_channels():
    """List all channels across all categories."""
    data = load_config()
    return data
def log_watch(video_title, channel_name, video_id, category):
    """Log a watched video to history."""
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []
    
    history.append({
        "title": video_title,
        "channel": channel_name,
        "video_id": video_id,
        "category": category,
        "timestamp": datetime.now().isoformat()
    })
    
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def get_watch_history():
    """Get all watched videos."""
    if not os.path.exists(HISTORY_FILE):
        return []
    
    with open(HISTORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def get_watch_stats():
    """Get learning statistics."""
    history = get_watch_history()
    if not history:
        return {"total_videos": 0, "total_time": "0h 0m", "categories": {}}
    
    categories = {}
    for video in history:
        cat = video.get("category", "Unknown")
        categories[cat] = categories.get(cat, 0) + 1
    
    # Assume average video is 10 minutes for demo purposes
    total_minutes = len(history) * 10
    hours = total_minutes // 60
    minutes = total_minutes % 60
    
    return {
        "total_videos": len(history),
        "total_time": f"{hours}h {minutes}m",
        "categories": categories,
        "recent": history[-5:] if len(history) > 5 else history
    }