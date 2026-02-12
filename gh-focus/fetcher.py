import feedparser
import concurrent.futures
import json
import subprocess
from rich.console import Console

console = Console()

def resolve_channel_id(user_input):
    """
    Resolve a YouTube handle or URL to a channel ID using yt-dlp.
    """
    print(f"[cyan]🔍 Resolving ID for '{user_input}'...[/cyan]")

    if not user_input.startswith("http"):
        if not user_input.startswith("@"):
            user_input = f"@{user_input}"
        url = f"https://www.youtube.com/{user_input}"
    else:
        url = user_input

    cmd = [
        "yt-dlp",
        "--playlist-end", "1",
        "--dump-json",
        "--flat-playlist",
        url
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            return None

        for line in result.stdout.splitlines():
            try:
                data = json.loads(line)
                if "channel_id" in data:
                    return data["channel_id"]
            except json.JSONDecodeError:
                continue
    except Exception as e:
        console.print(f"[red]Error resolving ID: {e}[/red]")
        return None

    return None

def fetch_single_channel(channel):
    """Fetch videos for a single channel."""
    rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel['id']}"
    results = []
    try:
        feed = feedparser.parse(rss_url)
        for entry in feed.entries[:3]:
            results.append({
                "title": entry.title,
                "link": entry.link,
                "channel": channel['name'],
                "published": entry.published,
                "video_id": entry.yt_videoid
            })
    except Exception as e:
        console.print(f"[red]Error fetching from {channel['name']}: {e}[/red]")
    return results

def get_videos(channel_list):
    """
    Fetch latest videos from YouTube channels using RSS feeds.
    No API key required!
    """
    videos = []

    with console.status("[bold green]Fetching content (Parallel Mode)...[/bold green]"):
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(fetch_single_channel, ch) for ch in channel_list]
            for future in concurrent.futures.as_completed(futures):
                videos.extend(future.result())

    return videos

def extract_channel_id(channel_url):
    """Back-compat wrapper for old code paths."""
    return resolve_channel_id(channel_url)
