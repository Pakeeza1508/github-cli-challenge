import feedparser
from rich.console import Console

console = Console()

def get_videos(channel_list):
    """
    Fetch latest videos from YouTube channels using RSS feeds.
    No API key required!
    """
    videos = []
    
    with console.status("[bold green]Fetching latest intentional content..."):
        for channel in channel_list:
            # The Magic URL (No API Key needed)
            rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel['id']}"
            
            try:
                feed = feedparser.parse(rss_url)
                
                # Get the last 3 videos from this channel
                for entry in feed.entries[:3]:
                    videos.append({
                        "title": entry.title,
                        "link": entry.link,
                        "channel": channel['name'],
                        "published": entry.published,
                        "video_id": entry.yt_videoid  # Feedparser extracts this for us
                    })
            except Exception as e:
                console.print(f"[red]Error fetching from {channel['name']}: {e}[/red]")
                continue
    
    # Sort by newest first (simplified for now)
    return videos

def extract_channel_id(channel_url):
    """
    Extract channel ID from a YouTube channel URL.
    Supports formats:
    - youtube.com/channel/UC...
    - youtube.com/@username
    """
    # This is a placeholder - in Phase 2 we can add proper extraction
    # For now, users will paste the ID directly
    if "channel/" in channel_url:
        return channel_url.split("channel/")[-1].split("/")[0]
    return None
