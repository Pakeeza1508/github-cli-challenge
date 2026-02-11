# 🏆 gh-focus: Hackathon Presentation Guide

**GitHub CLI Challenge 2026 Submission**

---

## Executive Summary

**Problem:** Developers lose 3+ hours daily to YouTube's algorithmic distraction.

**Solution:** gh-focus is a GitHub CLI extension that transforms YouTube into a productivity tool through intelligent curation and distraction elimination.

**Why It Matters:** Demonstrates how GitHub CLI can solve developer wellness problems, not just workflow automation.

---

## The Hackathon Angle (Critical)

### Why This IS a GitHub CLI Extension

Most judge think "GitHub CLI extension = GitHub automation tool"

**We're showing:**
- ✅ GitHub CLI can solve adjacent problems (developer wellness)
- ✅ Python scripting + questionary creates modern UX
- ✅ Local-first architecture (works offline)
- ✅ Easy to extend (Pomodoro timer, progress tracking, etc.)

**The pitch:** "GitHub CLI isn't just for GitHub. It's for developer quality of life."

---

## 2-Minute Demo Script

### Opening (15 seconds)
```
"Show of hands: Who's lost 3 hours to YouTube this week?"

[Pause for response]

"The algorithm isn't evil—it's just optimized for watch time, 
not learning outcomes. gh-focus fixes that."
```

### Demo (90 seconds)

**1. Show the problem** (30 seconds)
```bash
# Open YouTube in browser
# Show:
# - Sidebar with 'Up Next'
# - Recommendation algorithm
# - Comments section
# Say: "This is what kills focus."
```

**2. Show gh-focus in action** (45 seconds)
```bash
python gh-focus

# Select category: "coding"
# Show: [Fireship] Docker in 100 Seconds
# Explain: "Only content I whitelisted"

# Launch video
# Say: "Opens in MPV—distraction-free. No sidebar, no algorithm."

python gh-focus --stats
# Show: "3 videos, 30 minutes of learning"
# Say: "Tracks what you actually learned"
```

**3. Show the code** (15 seconds)
```
Point to `fetcher.py`:
"Uses YouTube RSS feeds, not the API. 
No quota limits. Simple. Clever."

Point to `focus_manager.py`:
"JSON config. Easy to customize.
Easy to extend."
```

### Closing (15 seconds)
```
"This is GitHub CLI doing what it should: 
improving developer quality of life.

Focus is a superpower. 🎯"
```

---

## Slide Deck (5 slides, 2 minutes)

### Slide 1: The Problem
**Title:** "The YouTube Time Sink"

Visual: Side-by-side comparison
- **Left:** Normal YouTube (sidebar, recommendations, comments)
- **Right:** gh-focus (clean video, no distractions)

**Text:**
```
"Average developer: 3+ hours/week lost to YouTube algorithm
Root cause: Recommendation sidebar = infinite context switching
Result: Broken focus sessions, lost productivity"
```

### Slide 2: The Solution
**Title:** "Introducing gh-focus"

**Key Points:**
- ✅ Channel whitelisting (curate YOUR content)
- ✅ Context categories (Coding/Business/Learning)
- ✅ Distraction-free players (MPV/VLC/Browser)
- ✅ Watch history tracking (see what you learned)
- ✅ GitHub CLI integration (one command)

### Slide 3: How It Works
**Title:** "Architecture: Smart, Simple"

```
Config (JSON)
    ↓
Fetch Videos (RSS feeds)
    ↓
Filter & Display (No algorithm)
    ↓
Open Player (MPV, distraction-free)
    ↓
Log Watch (Track learning)
```

**Bullet:**
```
• RSS feeds = no API key, no quota limits
• Python = lightweight, extensible
• Local-first = privacy-preserving
```

### Slide 4: GitHub CLI Challenge Fit
**Title:** "Why This is a Great CLI Extension"

1. **Solves Real Problem** - Developer wellness, not just automation
2. **Goes Beyond GitHub** - Shows CLI's broader potential
3. **Offline-First** - Works without constant API calls
4. **Extensible** - Easy to add: Pomodoro timer, progress tracking, etc.
5. **Clean Code** - Best practices: modularity, error handling, user feedback

### Slide 5: Roadmap & Impact
**Title:** "What's Next"

**Current:**
- ✅ Channel whitelisting
- ✅ Category filtering
- ✅ Watch history

**Soon:**
- 📋 Pomodoro timer integration
- 📊 Learning dashboard
- 🔗 Auto-channel ID extraction
- ☁️ Sync channels via GitHub Gists

**Impact:** "Could inspire a whole category of CLI tools for developer wellness, not just work automation."

---

## Q&A Prep

### Q: "Isn't this just a YouTube wrapper?"

**A:** "It's more about the philosophy. Most GitHub CLI extensions automate GitHub workflows. gh-focus shows CLI can improve developer *quality of life*. If it works for YouTube, it could work for focus timers, learning dashboards, or any wellness tool. That's the innovation."

### Q: "Why not just use YouTube's features?"

**A:** "YouTube doesn't have a 'distraction-free' mode. The sidebar can't be hidden. This is the only solution that truly removes the algorithm."

### Q: "How does it compare to other YouTube clients?"

**A:** "We're the only one that:
1. Doesn't require YouTube API key (uses RSS)
2. Integrates with developer workflow (GitHub CLI)
3. Tracks learning outcomes
4. Is designed specifically for developers"

### Q: "Will YouTube break this?"

**A:** "RSS feeds have existed since 2005. YouTube isn't going to kill RSS. Even if they did, the architecture is flexible—easy to add alternative feeds or backends."

### Q: "How is this different from just bookmarking channels?"

**A:** "Bookmarks don't:
- Filter shorts/distracting content
- Show stats on what you learned
- Offer distraction-free playback
- Integrate with developer workflow"

---

## Judging Criteria Alignment

### Innovation (9/10)
- Novel use of GitHub CLI for wellness (not just automation)
- Clever RSS-based approach (no API key needed)
- Creative problem-solving (algorithmic distraction is real)

### Code Quality (8/10)
- Clean architecture (fetcher, manager, main separated)
- Error handling and user feedback
- Extensible design
- Real-world use case

### User Experience (9/10)
- Beautiful Rich CLI interface
- Questionary for interactive selection
- Progress tracking and stats
- Offline-first design

### Completeness (7/10)
- Working MVP ✅
- Documentation (README + SETUP.md) ✅
- Config management ✅
- Missing: GitHub CLI extension packaging (can be added)

---

## Presentation Tips

### Do's ✅
- Show the problem first (3 hours/week lost to YouTube)
- Emphasize the GitHub CLI angle (judges care about that)
- Demo the interactive CLI (it's beautiful)
- Show `--stats` output (concrete proof it works)
- End with the bigger vision (developer wellness tools)

### Don'ts ❌
- Don't just talk code—show the UX
- Don't oversell (be honest about MVP status)
- Don't get lost in technical details (save for Q&A)
- Don't forget to mention the GitHub CLI challenge

### Tone
- **Confident** - You solved a real problem
- **Humble** - It's an MVP, but a solid one
- **Visionary** - Point to future use cases
- **Developer-focused** - Talk about productivity and focus

---

## The Close

**Final Message:**

> "GitHub CLI is for developers, by developers. But most extensions automate work tasks. gh-focus is different—it helps developers *live better*. A focused developer is a happy developer. A happy developer is a productive developer.
>
> That's why gh-focus matters. Not just for YouTube, but for the entire category of developer wellness tools we can build with GitHub CLI.
>
> Thank you. Questions?"

---

## One-Liner

**For the elevator pitch:**

"gh-focus is a GitHub CLI extension that eliminates YouTube's algorithmic distraction by curating content and offering distraction-free playback, helping developers reclaim focus and learning time."

---

## Demo Checklist

Before presenting:
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] config.json populated with channels
- [ ] Test running `python gh-focus` (exits cleanly)
- [ ] Test running `python gh-focus --stats`
- [ ] MPV or VLC installed (or browser ready)
- [ ] Slides prepared and tested
- [ ] Timer set for 2 minutes
- [ ] Terminal text size increased (judges need to see clearly)

---

**Good luck! 🚀**

Remember: You're not just presenting a tool. You're showing how GitHub CLI can expand beyond workflow automation into developer wellness. That's the story.
