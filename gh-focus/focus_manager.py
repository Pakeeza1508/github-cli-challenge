import json
import os

# Where we store data
CONFIG_FILE = "config.json"

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
