#!/usr/bin/env python3
"""
gh-focus: A distraction-free YouTube CLI for focused learning
GitHub CLI Extension for the 2026 Challenge
"""

import sys
import webbrowser
import subprocess
import shutil
import os
import re
import questionary
from rich import print
from rich.panel import Panel
from rich.columns import Columns
from rich.table import Table
from focus_manager import load_config, add_channel, log_watch, get_watch_stats, get_gist_id, save_gist_id, remove_channel, remove_category
from fetcher import get_videos, resolve_channel_id

# Tracks whether GitHub CLI is available for Gist sync features.
GH_INSTALLED = False

def check_dependencies():
    """Ensure yt-dlp is installed for ID resolution."""
    import importlib.util
    import subprocess
    
    # Check if yt_dlp library is importable in Python
    if importlib.util.find_spec("yt_dlp") is None:
        print(Panel("[yellow]⚙️  First Run Setup: Installing dependencies...[/yellow]", border_style="yellow"))
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
            print("[green]✓ Dependencies installed![/green]")
        except Exception as e:
            print(f"[red]❌ Failed to install yt-dlp. Please run: pip install yt-dlp[/red]")
            sys.exit(1)

def check_gh_auth():
    """Checks if gh CLI is available (non-blocking)."""
    global GH_INSTALLED
    try:
        subprocess.run(
            ["gh", "--version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        GH_INSTALLED = True
        return True
    except Exception:
        GH_INSTALLED = False
        return False

def save_to_learning_log(video_title, video_url):
    """Append the video to a shared learning log Gist."""
    if not check_gh_auth():
        return

    print("[bold yellow]🐱 Syncing with GitHub...[/bold yellow]")

    gist_id = get_gist_id()
    filename = "focus_learning_log.md"
    new_entry = f"- [ ] **{video_title}** - [Watch]({video_url})\n"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    temp_path = os.path.join(script_dir, filename)

    if not gist_id:
        print("[cyan]Creating new Learning Log Gist...[/cyan]")
        description = "My Developer Learning Path (Created by gh-focus)"

        with open(temp_path, "w", encoding="utf-8") as f:
            f.write(f"# My Intentional Learning Log 🧠\n\n{new_entry}")

        try:
            subprocess.run(
                ["gh", "gist", "create", temp_path, "--desc", description, "--public"],
                check=True
            )

            res = subprocess.run(
                ["gh", "gist", "list", "--limit", "1"],
                capture_output=True,
                text=True,
                check=True
            )
            new_id = res.stdout.split()[0]
            save_gist_id(new_id)
            print(f"[bold green]✅ Created & Saved to Gist ID: {new_id}[/bold green]")
        except subprocess.CalledProcessError as exc:
            print("[bold red]❌ Failed to create the Learning Log Gist.[/bold red]")
            if exc.stderr:
                print(exc.stderr)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
    else:
        print(f"[cyan]Updating Gist {gist_id}...[/cyan]")
        try:
            res = subprocess.run(
                ["gh", "gist", "view", gist_id, "--filename", filename],
                capture_output=True,
                text=True,
                check=True
            )
            current_content = res.stdout
            updated_content = current_content + new_entry

            with open(temp_path, "w", encoding="utf-8") as f:
                f.write(updated_content)

            subprocess.run(["gh", "gist", "edit", gist_id, temp_path], check=True)
            print(f"[bold green]✅ Added '{video_title}' to your Learning Log![/bold green]")
        except subprocess.CalledProcessError as exc:
            print("[bold red]❌ Failed to update the Learning Log Gist.[/bold red]")
            if exc.stderr:
                print(exc.stderr)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

def open_safe_mode(video_id):
    """
    Opens video using available players. Priority: MPV > VLC > Browser (with setup guide)
    """
    url = f"https://www.youtube.com/watch?v={video_id}"
    
    # 1. Check for mpv.exe in the SAME folder as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    local_mpv = os.path.join(script_dir, "mpv.exe")
    
    if os.path.exists(local_mpv):
        print(f"[bold green]🚀 Launching Portable MPV (Ad-Free)...[/bold green]")
        subprocess.run([local_mpv, url])
        return

    # 2. Check for System MPV (Global install) - RECOMMENDED
    if shutil.which("mpv"):
        print(f"[bold green]🚀 Launching System MPV (Ad-Free Distraction-Free Experience)...[/bold green]")
        subprocess.run(["mpv", url])
        return

    # 3. Check for VLC (Backup player)
    vlc_path = shutil.which("vlc")
    if not vlc_path:
        # Check standard Windows paths
        paths = [
            r"C:\Program Files\VideoLAN\VLC\vlc.exe",
            r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
        ]
        for p in paths:
            if os.path.exists(p):
                vlc_path = p
                break
    
    if vlc_path:
        print(f"[bold cyan]🎬 Launching VLC (Ad-Free)...[/bold cyan]")
        subprocess.run([vlc_path, url, "--play-and-exit"])
        return

    # 4. No player found - provide setup instructions
    print()
    print(Panel(
        "[bold yellow]⚠️  No Distraction-Free Player Detected[/bold yellow]\n\n"
        "[yellow]To enable ad-free video playback:[/yellow]\n\n"
        "[bold]Option 1: Install MPV (Recommended)[/bold]\n"
        "[green]winget install io.mpv.mpv[/green]\n\n"
        "[bold]Option 2: Install VLC[/bold]\n"
        "[green]winget install VideoLAN.VLC[/green]\n\n"
        "[dim]After installation, restart gh focus and it will work automatically![/dim]",
        title="🎯 Setup Required for Ad-Free Mode",
        border_style="yellow",
        padding=(1, 2)
    ))
    print()
    
    # Fallback to browser (not ideal, but works)
    print("[cyan]Opening in browser (with ads)...[/cyan]")
    webbrowser.open(url)

def show_banner():
    """Display welcome banner."""
    banner = Panel.fit(
        "[bold white]🎯 YouTube Focus Mode[/bold white]\n[cyan]Curated • Intentional • Focused[/cyan]",
        border_style="cyan",
        padding=(1, 2)
    )
    print(banner)

def normalize_category_name(raw_name):
    """Normalize a user-provided category into a safe key."""
    if not raw_name:
        return None
    cleaned = raw_name.strip().lower()
    cleaned = re.sub(r"\s+", "_", cleaned)
    cleaned = re.sub(r"[^a-z0-9_]", "", cleaned)
    cleaned = cleaned.strip("_")
    return cleaned or None

def is_valid_channel_id(raw_id):
    """Basic validation for YouTube channel IDs (UC...)."""
    if not raw_id:
        return False
    return re.match(r"^UC[0-9A-Za-z_-]{20,}$", raw_id.strip()) is not None

def is_valid_handle_or_url(user_input):
    """Accept a handle (@...), URL, or UC... ID."""
    if not user_input:
        return False
    trimmed = user_input.strip()
    return trimmed.startswith("@") or trimmed.startswith("http") or trimmed.startswith("UC")

def view_channels():
    """Display all configured channels by category with rich tables."""
    config = load_config()
    categories = [key for key, value in config.items() if isinstance(value, list)]
    
    if not categories:
        print(Panel("[yellow]⚠️  No categories found.[/yellow]", title="📋 Channels", border_style="yellow"))
        return
    
    print()
    for cat in categories:
        channels = config[cat]
        if channels:
            table = Table(title=f"[bold cyan]{cat.upper()}[/bold cyan]", show_header=True, header_style="bold magenta")
            table.add_column("Channel Name", style="cyan", no_wrap=False)
            table.add_column("Channel ID", style="dim", no_wrap=True)
            
            for ch in channels:
                table.add_row(ch['name'], ch['id'][:12] + "..." if len(ch['id']) > 12 else ch['id'])
            
            print(table)
            print()
        else:
            print(f"[dim]{cat.upper()} (empty)[/dim]")
    print()

def open_channel_from_list():
    """Prompt user to pick a channel and open it in the browser."""
    config = load_config()
    categories = [key for key, value in config.items() if isinstance(value, list)]

    if not categories:
        print("[yellow]No categories found.[/yellow]")
        return

    category_choices = categories + ["Back"]
    selected_category = questionary.select(
        "Choose a category:",
        choices=category_choices
    ).ask()

    if selected_category == "Back":
        return

    channels = config.get(selected_category, [])
    if not channels:
        print("[yellow]No channels in this category yet.[/yellow]")
        return

    channel_choices = [f"{ch['name']} → {ch['id']}" for ch in channels]
    channel_choices.append("Back")
    selected_channel = questionary.select(
        "Open which channel?",
        choices=channel_choices
    ).ask()

    if selected_channel == "Back":
        return

    channel_id = selected_channel.split("→")[-1].strip()
    webbrowser.open(f"https://www.youtube.com/channel/{channel_id}")

def remove_channel_menu():
    """Remove a channel from a category."""
    config = load_config()
    categories = [key for key, value in config.items() if isinstance(value, list)]

    if not categories:
        print("[yellow]No categories found.[/yellow]")
        return

    category_choices = categories + ["Back"]
    selected_category = questionary.select(
        "Choose category to remove from:",
        choices=category_choices
    ).ask()

    if selected_category == "Back":
        return

    channels = config.get(selected_category, [])
    if not channels:
        print("[yellow]No channels in this category.[/yellow]")
        return

    channel_choices = [ch['name'] for ch in channels]
    channel_choices.append("Back")
    selected_channel = questionary.select(
        "Remove which channel?",
        choices=channel_choices
    ).ask()

    if selected_channel == "Back":
        return

    # Find the channel ID
    channel_id = None
    for ch in channels:
        if ch['name'] == selected_channel:
            channel_id = ch['id']
            break

    if channel_id and remove_channel(selected_category, channel_id):
        print(f"[green]✓ Removed {selected_channel} from {selected_category}[/green]")
    else:
        print(f"[red]Failed to remove channel[/red]")

def remove_category_menu():
    """Remove an entire category."""
    config = load_config()
    categories = [key for key, value in config.items() if isinstance(value, list)]

    if not categories:
        print("[yellow]No categories found.[/yellow]")
        return

    category_choices = categories + ["Back"]
    selected_category = questionary.select(
        "Remove which category?",
        choices=category_choices
    ).ask()

    if selected_category == "Back":
        return

    confirm = questionary.confirm(
        f"Are you sure you want to remove '{selected_category}' and all its channels?"
    ).ask()

    if confirm and remove_category(selected_category):
        print(f"[green]✓ Removed category '{selected_category}'[/green]")
    elif confirm:
        print(f"[red]Failed to remove category[/red]")

def show_dashboard():
    """Display a professional analytics dashboard."""
    stats = get_watch_stats()
    
    if stats.get('total_videos', 0) == 0:
        print(Panel(
            "[dim]📽️  No videos watched yet\n\nStart watching to build your learning dashboard![/dim]",
            title="📊 Your Dashboard",
            border_style="cyan",
            padding=(1, 2)
        ))
        return
    
    # Stats table
    stats_table = Table(show_header=False, box=None, padding=(0, 2))
    stats_table.add_column("", style="bold yellow", width=20)
    stats_table.add_column("", style="bold white")
    
    stats_table.add_row("🎥 Videos Watched", str(stats['total_videos']))
    stats_table.add_row("⏱️  Focus Time (est)", stats['total_time'])
    
    if stats['categories']:
        top_cat = max(stats['categories'], key=stats['categories'].get)
        top_count = stats['categories'][top_cat]
        stats_table.add_row("🔥 Top Focus", f"[cyan]{top_cat}[/cyan] ({top_count})")
    
    # Category breakdown
    cat_table = Table(title="[bold cyan]Category Breakdown[/bold cyan]", show_header=True, header_style="bold magenta")
    cat_table.add_column("Category", style="cyan")
    cat_table.add_column("Videos", justify="right", style="yellow")
    
    for cat, count in sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True):
        cat_table.add_row(cat, str(count))
    
    # Recent activity
    recent_table = Table(title="[bold cyan]Recent Learning[/bold cyan]", show_header=True, header_style="bold magenta")
    recent_table.add_column("Category", style="cyan", width=15)
    recent_table.add_column("Video Title", style="white", no_wrap=False)
    
    if stats.get('recent'):
        for vid in reversed(stats['recent'][-5:]):
            title_short = vid['title'][:35]
            cat = vid.get('category', '?')
            recent_table.add_row(cat, title_short + ("..." if len(vid['title']) > 35 else ""))
    
    print(Panel(
        stats_table,
        title="[bold cyan]📊 Your Progress[/bold cyan]",
        border_style="green",
        padding=(1, 2)
    ))
    print()
    print(cat_table)
    print()
    print(recent_table)

def show_stats():
    """Display detailed learning statistics."""
    stats = get_watch_stats()
    
    print(Panel(
        f"[bold cyan]📊 Your Learning Stats[/bold cyan]\n"
        f"[green]Videos Watched:[/green] {stats['total_videos']}\n"
        f"[green]Total Time:[/green] {stats['total_time']}\n"
        f"[green]Categories:[/green] {', '.join([f'{k} ({v})' for k, v in stats['categories'].items()]) if stats['categories'] else 'None'}",
        border_style="cyan"
    ))
    
    if stats['recent']:
        print("\n[bold cyan]📺 Recent Videos:[/bold cyan]")
        for video in reversed(stats['recent']):
            date = video.get('timestamp', '').split('T')[0]
            print(f"  ✓ {video['title'][:50]}... ({date})")

def view_learning_log():
    """Fetch and display the Learning Log from Gist with interactive playback."""
    if not GH_INSTALLED:
        print(Panel(
            "[yellow]⚠️  GitHub CLI not available. Cannot access Learning Log.[/yellow]",
            border_style="yellow"
        ))
        return
    
    gist_id = get_gist_id()
    
    if not gist_id:
        print(Panel(
            "[yellow]📚 No Learning Log found yet.[/yellow]\n\n"
            "Save your first video to create one!",
            border_style="yellow",
            title="Learning Log"
        ))
        return
    
    # Fetch gist content
    filename = "focus_learning_log.md"
    try:
        result = subprocess.run(
            ["gh", "gist", "view", gist_id, "--filename", filename],
            capture_output=True,
            text=True,
            check=True
        )
        content = result.stdout
        
        # Parse learning log entries
        import re
        entries = []
        for line in content.split('\n'):
            # Match: - [ ] or - [x] **Title** - [Watch](URL)
            match = re.match(r'^- \[([ x])\] \*\*(.+?)\*\* - \[Watch\]\((.+?)\)$', line)
            if match:
                checked, title, url = match.groups()
                video_id = url.split('v=')[-1] if 'v=' in url else None
                entries.append({
                    'title': title,
                    'url': url,
                    'video_id': video_id,
                    'completed': checked == 'x'
                })
        
        if not entries:
            print(Panel(
                "[yellow]Your Learning Log is empty.[/yellow]",
                border_style="yellow"
            ))
            return
        
        # Interactive menu loop
        while True:
            # Create choices with status icons
            choices = []
            for i, entry in enumerate(entries):
                status = "✓" if entry['completed'] else "○"
                display = f"{status} {entry['title'][:60]}"
                choices.append(display)
            
            choices.extend(["", "🌐 Open Full List in Browser", "🔙 Go Back"])
            
            # Show stats
            completed = sum(1 for e in entries if e['completed'])
            total = len(entries)
            
            selected = questionary.select(
                f"📚 Your Learning Queue ({completed}/{total} completed):",
                choices=choices
            ).ask()
            
            if not selected or selected == "🔙 Go Back":
                break
                
            if selected == "🌐 Open Full List in Browser":
                gist_url = f"https://gist.github.com/{gist_id}"
                webbrowser.open(gist_url)
                print("[green]✓ Opened in browser[/green]")
                input("Press Enter to continue...")
                continue
            
            if selected == "":
                continue
            
            # Find which entry was selected
            selected_index = choices.index(selected)
            if selected_index >= len(entries):
                continue
                
            entry = entries[selected_index]
            
            # Action menu for selected video
            action = questionary.select(
                f"📺 {entry['title'][:50]}...",
                choices=["▶️  Watch Now", "✓ Mark as Complete" if not entry['completed'] else "○ Mark as Incomplete", "🔙 Cancel"]
            ).ask()
            
            if action == "▶️  Watch Now":
                if entry['video_id']:
                    print(f"\n[bold yellow]🎬 {entry['title']}[/bold yellow]")
                    open_safe_mode(entry['video_id'])
                    print("\n[green]✓ Playback finished[/green]")
                    input("[dim]Press Enter to continue...[/dim]")
                else:
                    webbrowser.open(entry['url'])
                    input("Press Enter when done...")
                    
            elif "Mark as" in action:
                # Toggle completion status
                new_status = "x" if not entry['completed'] else " "
                try:
                    # Read current content
                    new_content = content.replace(
                        f"- [{'x' if entry['completed'] else ' '}] **{entry['title']}**",
                        f"- [{new_status}] **{entry['title']}**"
                    )
                    
                    # Update gist
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    temp_path = os.path.join(script_dir, filename)
                    with open(temp_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    
                    subprocess.run(["gh", "gist", "edit", gist_id, temp_path], check=True)
                    print("[green]✓ Updated![/green]")
                    
                    # Update local cache
                    entry['completed'] = not entry['completed']
                    content = new_content
                    
                    if os.path.exists(temp_path):
                        os.remove(temp_path)
                        
                except Exception as e:
                    print(f"[red]❌ Failed to update: {e}[/red]")
                
                input("Press Enter to continue...")
            
    except subprocess.CalledProcessError:
        print("[red]❌ Failed to fetch Learning Log[/red]")
    except Exception as e:
        print(f"[red]Error: {e}[/red]")

def main():
    check_dependencies()  # Auto-install yt-dlp on first run
    
    # Handle command-line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--stats":
            show_banner()
            show_dashboard()
            return
        elif sys.argv[1] == "--help":
            print("[cyan]Usage:[/cyan]")
            print("  python gh-focus          Start interactive mode")
            print("  python gh-focus --stats  Show dashboard & statistics")
            print("  python gh-focus --help   Show this help message")
            return
    
    show_banner()
    show_dashboard()

    if not check_gh_auth():
        print(Panel(
            "[yellow]⚠️  GitHub CLI not found. 'Save to Gist' is disabled.[/yellow]",
            border_style="yellow"
        ))

    script_dir = os.path.dirname(os.path.abspath(__file__))
    local_mpv = os.path.join(script_dir, "mpv.exe")
    
    # Check if user has a player installed
    has_player = os.path.exists(local_mpv) or shutil.which("mpv") or shutil.which("vlc")
    
    if not has_player:
        print(Panel(
            "[bold cyan]🎯 First Time Setup: Enable Ad-Free Mode[/bold cyan]\n\n"
            "[yellow]Install MPV for distraction-free learning:[/yellow]\n\n"
            "[bold green]winget install io.mpv.mpv[/bold green]\n\n"
            "[dim]Or use VLC: winget install VideoLAN.VLC[/dim]\n"
            "[dim]Then restart gh focus to activate![/dim]",
            border_style="cyan",
            padding=(1, 2)
        ))
        print()
    
    # MAIN LOOP: Keeps the app running
    while True:
        config = load_config()
        
        categories = [key for key, value in config.items() if isinstance(value, list)]
        
        # Print colored header
        print()
        print("[bold cyan]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold cyan]")
        print("[bold cyan]📚 YOUR LEARNING CATEGORIES[/bold cyan]")
        print("[bold cyan]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold cyan]")
        
        # Build categories menu with separator
        categories_menu = []
        if categories:
            categories_menu = categories.copy()
            categories_menu.append(questionary.Separator())
        
        # Tools menu
        tools_menu = [
            "📊 View Stats",
            "📺 View Learning Log",
            "👀 View Channels",
            "🔎 Open Channel",
            "+ Add New Channel",
            "🗑️  Remove Channel",
            "🗑️  Remove Category",
            questionary.Separator(),
            "Exit"
        ]
        
        # Combine menus
        menu_items = categories_menu + tools_menu
        
        choice = questionary.select(
            "Select an option:",
            choices=menu_items,
            style=questionary.Style([('answer', 'fg:cyan bold')])
        ).ask()
        
        # Handle Main Menu Exits
        if choice == "Exit":
            print("[bold red]Stay focused! Goodbye. 👋[/bold red]")
            sys.exit()
        
        if choice == "📊 View Stats":
            show_dashboard()
            questionary.confirm("Press Enter to continue...").ask()
            continue
        
        if choice == "📺 View Learning Log":
            view_learning_log()
            questionary.confirm("Press Enter to continue...").ask()
            continue
        
        if choice == "👀 View Channels":
            view_channels()
            questionary.confirm("Press Enter to continue...").ask()
            continue

        if choice == "🔎 Open Channel":
            open_channel_from_list()
            questionary.confirm("Press Enter to continue...").ask()
            continue
        
        if choice == "🗑️  Remove Channel":
            remove_channel_menu()
            questionary.confirm("Press Enter to continue...").ask()
            continue
        
        if choice == "🗑️  Remove Category":
            remove_category_menu()
            questionary.confirm("Press Enter to continue...").ask()
            continue
            
        if choice == "+ Add New Channel":
            category_choices = categories + ["+ New Category", "Back"]
            selected_category = questionary.select(
                "Which category?",
                choices=category_choices
            ).ask()

            if selected_category == "Back":
                continue

            if selected_category == "+ New Category":
                raw_name = questionary.text(
                    "New category name (e.g., data science):"
                ).ask()
                cat = normalize_category_name(raw_name)
                if not cat:
                    print("[red]Invalid category name. Try again with letters or numbers.[/red]")
                    questionary.confirm("Press Enter to continue...").ask()
                    continue
            else:
                cat = selected_category
            
            user_input = questionary.text(
                "Channel handle (e.g., @Fireship), URL, or Channel ID (UC...):"
            ).ask()

            if not is_valid_handle_or_url(user_input):
                print("[red]Please enter a handle (@...), full URL, or Channel ID (UC...).[/red]")
                questionary.confirm("Press Enter to continue...").ask()
                continue

            # Check if user entered a UC... ID directly
            if user_input.strip().startswith("UC"):
                c_id = user_input.strip()
                if not is_valid_channel_id(c_id):
                    print("[red]Invalid channel ID. It should start with UC and be at least 22 chars.[/red]")
                    questionary.confirm("Press Enter to continue...").ask()
                    continue
                name = questionary.text("Enter a display name for this channel:").ask()
                if not name or not name.strip():
                    print("[red]Channel name cannot be empty.[/red]")
                    questionary.confirm("Press Enter to continue...").ask()
                    continue
                if add_channel(cat, name, c_id):
                    print(f"[green]✓ Added {name} to {cat}![/green]")
                else:
                    print(f"[yellow]Channel already exists in {cat}[/yellow]")
            else:
                # Try to resolve handle or URL
                c_id = resolve_channel_id(user_input)
                if c_id:
                    name = questionary.text(f"[bold cyan]✓ Found ID {c_id}\n\nEnter display name:[/bold cyan]").ask()
                    if not name or not name.strip():
                        print(Panel("[red]❌ Channel name cannot be empty[/red]", border_style="red"))
                        questionary.confirm("Press Enter to continue...").ask()
                        continue
                    if add_channel(cat, name, c_id):
                        success = Panel(
                            f"[green]✓ Added [bold white]{name}[/bold white] to [bold cyan]{cat}[/bold cyan][/green]",
                            border_style="green",
                            padding=(1, 2)
                        )
                        print(success)
                    else:
                        print(Panel(f"[yellow]⚠️  Channel already exists in {cat}[/yellow]", border_style="yellow", padding=(1, 2)))
                else:
                    print(Panel("[yellow]⚠️  Resolution failed. Try entering the Channel ID manually.[/yellow]", border_style="yellow", padding=(1, 2)))
                    use_manual = questionary.confirm("Enter Channel ID manually (UC...)?").ask()
                    if use_manual:
                        c_id = questionary.text("Channel ID (e.g., UCsBjURrPoezykLs9EqgamOA):").ask()
                        if not is_valid_channel_id(c_id):
                            print(Panel("[red]❌ Invalid channel ID. Must start with UC and be 22+ chars.[/red]", border_style="red", padding=(1, 2)))
                            questionary.confirm("Press Enter to continue...").ask()
                            continue
                        name = questionary.text("Channel name (e.g., Fireship):").ask()
                        if not name or not name.strip():
                            print(Panel("[red]❌ Channel name cannot be empty[/red]", border_style="red"))
                            questionary.confirm("Press Enter to continue...").ask()
                            continue
                        if add_channel(cat, name, c_id):
                            success = Panel(
                                f"[green]✓ Added [bold white]{name}[/bold white] to [bold cyan]{cat}[/bold cyan][/green]",
                                border_style="green",
                                padding=(1, 2)
                            )
                            print(success)
                        else:
                            print(Panel(f"[yellow]⚠️  Channel already exists in {cat}[/yellow]", border_style="yellow", padding=(1, 2)))
            questionary.confirm("Press Enter to continue...").ask()
            continue  # Go back to start of loop

        # 2. Fetch Videos for that category
        channels = config[choice]
        if not channels:
            empty_msg = Panel(
                "[yellow]📭 No channels in this category yet\n\n[dim]Select '[bold]+ Add New Channel[/bold]' to get started[/dim][/yellow]",
                border_style="yellow",
                padding=(1, 2)
            )
            print(empty_msg)
            questionary.confirm("Press Enter to continue...").ask()
            continue

        # INNER LOOP: Stay in this category until user goes back
        while True:
            videos = get_videos(channels)

            if not videos:
                print(Panel("[yellow]⚠️  No recent videos found.[/yellow]", border_style="yellow"))
                break

            # 3. Create the Selection List
            video_choices = []
            video_map = {}
            video_info = {}
            
            for v in videos:
                # 🚫 BLOCK SHORTS: Skip short-form content
                if "#shorts" in v['title'].lower() or "short" in v['title'].lower():
                    continue
                
                # Clean up title for display
                display_text = f"[{v['channel']}] {v['title'][:50]}"
                video_choices.append(display_text)
                video_map[display_text] = v['video_id']
                video_info[display_text] = v
            
            if not video_choices:
                print(Panel("[yellow]⚠️  No full-length videos found (only Shorts).[/yellow]", border_style="yellow"))
                break
            
            # Add Navigation with separators
            video_choices.append(questionary.Separator("━" * 50))
            video_choices.append("🔙 Go Back")
            video_choices.append("❌ Exit App")
            
            selected_text = questionary.select(
                f"[bold cyan]📺 {choice.upper()}[/bold cyan]\n[dim]Select a video to watch:[/dim]",
                choices=video_choices,
                style=questionary.Style([('answer', 'fg:cyan bold')])
            ).ask()
            
            # Navigation Logic
            if selected_text == "❌ Exit App":
                print("[bold red]Stay focused! Goodbye. 👋[/bold red]")
                sys.exit()
                
            if selected_text == "🔙 Go Back":
                break  # Breaks inner loop, goes back to Main Menu
                
            # Choose action for the selected video
            video_id = video_map[selected_text]
            video_data = video_info[selected_text]
            
            # Display selected video info
            print()
            info_table = Table(show_header=False, box=None, padding=(0, 1))
            info_table.add_column("", style="dim", width=12)
            info_table.add_column("", style="white")
            info_table.add_row("📺 Channel:", video_data['channel'])
            info_table.add_row("🎯 Title:", video_data['title'][:60])
            info_table.add_row("📅 Published:", video_data['published'][:10] if len(video_data['published']) > 10 else video_data['published'])
            print(Panel(info_table, title="[bold cyan]Video Details[/bold cyan]", border_style="green", padding=(1, 2)))
            print()
            
            # ACTION LOOP: Allow user to watch AND save without reselecting video
            while True:
                action_options = ["📺 Stream (Watch Now)"]
                if GH_INSTALLED:
                    action_options.append("💾 Save to Learning Log")
                
                action_options.append(questionary.Separator())
                action_options.append("🔙 Back to Videos")

                action = questionary.select(
                    "[bold cyan]What would you like to do?[/bold cyan]",
                    choices=action_options,
                    style=questionary.Style([('answer', 'fg:cyan bold')])
                ).ask()

                # Handle cancellation or None return
                if not action or action == "🔙 Back to Videos":
                    break  # Go back to video list
                    
                elif action == "📺 Stream (Watch Now)":
                    info_msg = Panel(
                        f"[bold cyan]{selected_text}[/bold cyan]\n\n[dim]YouTube will open. Close when done.[/dim]",
                        title="[bold cyan]🚀 Launching Video[/bold cyan]",
                        border_style="green",
                        padding=(1, 2)
                    )
                    print(info_msg)

                    log_watch(
                        video_data['title'],
                        video_data['channel'],
                        video_id,
                        choice
                    )

                    open_safe_mode(video_id)
                    
                    # Give terminal a moment to stabilize after player closes
                    print("\n")
                    success_msg = Panel(
                        "[green]✓ Video watched and logged to your history![/green]",
                        border_style="green",
                        padding=(0, 2)
                    )
                    print(success_msg)
                    print()
                    questionary.confirm("Press Enter to continue...").ask()
                    # Loop continues - user can now save it too
                    
                elif action == "💾 Save to Learning Log":
                    clean_title = selected_text.split("] ")[-1]
                    full_url = f"https://www.youtube.com/watch?v={video_id}"
                    save_to_learning_log(clean_title, full_url)
                    print()
                    questionary.confirm("Press Enter to continue...").ask()
                    # Loop continues - user can watch it too

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[bold red]Force Exit. Stay focused! 👋[/bold red]")
        sys.exit(0)
    except Exception as e:
        print(f"[red]Error: {e}[/red]")
        sys.exit(1)
