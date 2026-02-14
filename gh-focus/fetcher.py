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
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if result.returncode != 0:
            console.print(f"[yellow]⚠️  Resolution failed (maybe private channel?)[/yellow]")
            return None

        for line in result.stdout.splitlines():
            try:
                data = json.loads(line)
                if "channel_id" in data:
                    return data["channel_id"]
            except json.JSONDecodeError:
                continue
    except subprocess.TimeoutExpired:
        console.print(f"[red]❌ Timeout: couldn't reach YouTube[/red]")
        return None
    except Exception as e:
        console.print(f"[red]Error resolving ID: {e}[/red]")
        return None

    return None

def fetch_videos_yt_dlp(channel):
    """Fallback: Fetch videos using yt-dlp when RSS is disabled."""
    results = []
    try:
        # Try channel URL (safer than /videos which may be blocked)
        url = f"https://www.youtube.com/@{channel['name'].replace(' ', '')}/videos"
        
        cmd = [
            "yt-dlp",
            "--flat-playlist",
            "--playlist-end", "5",
            "--dump-json",
            "--no-warnings",
            "--skip-download",
            url
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        
        if result.returncode == 0 and result.stdout.strip():
            line_count = 0
            for line in result.stdout.splitlines():
                try:
                    data = json.loads(line)
                    if data.get("id"):
                        results.append({
                            "title": data.get("title", "Unknown"),
                            "link": f"https://www.youtube.com/watch?v={data['id']}",
                            "channel": channel['name'],
                            "published": data.get("upload_date", "N/A"),
                            "video_id": data['id']
                        })
                        line_count += 1
                except json.JSONDecodeError:
                    continue
            
            if line_count > 0:
                console.print(f"[green]✓ Fetched {line_count} videos from {channel['name']} (yt-dlp)[/green]")
                return results
        
        if result.stderr:
            console.print(f"[yellow]⚠️  {channel['name']}: {result.stderr[:100]}[/yellow]")
    except subprocess.TimeoutExpired:
        console.print(f"[yellow]⏱️  Timeout fetching {channel['name']}[/yellow]")
    except Exception as e:
        console.print(f"[yellow]❌ yt-dlp error for {channel['name']}: {str(e)[:80]}[/yellow]")
    
    return results


def fetch_single_channel(channel):
    """Fetch videos for a single channel."""
    rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel['id']}"
    results = []
    try:
        feed = feedparser.parse(rss_url)
        if not feed.entries:
            console.print(f"[cyan]ℹ️  {channel['name']}: Trying alternate fetch method...[/cyan]")
            return fetch_videos_yt_dlp(channel)
        for entry in feed.entries[:3]:
            results.append({
                "title": entry.title,
                "link": entry.link,
                "channel": channel['name'],
                "published": entry.published,
                "video_id": entry.yt_videoid
            })
    except Exception as e:
        console.print(f"[cyan]ℹ️  {channel['name']}: Trying alternate fetch method...[/cyan]")
        return fetch_videos_yt_dlp(channel)
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
