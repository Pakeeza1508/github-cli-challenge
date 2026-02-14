# Verified Channel IDs for Testing

If the auto-resolution fails, use these **working** Channel IDs directly.

## Coding Channels (Copy the ID)

| Channel | Handle | Channel ID |
|---------|--------|-----------|
| Fireship | @Fireship | `UCsBjURrPoezykLs9EqgamOA` |
| Traversy Media | @TraversyMedia | `UC29ju8bIPH5as8OGnQzwJyA` |
| Web Dev Simplified | @WebDevSimplified | `UCFbNIlppjreqWp0LoG4qLDg` |
| Linux Unplugged | @LinuxUnplugged | `UCTtoQeR6C-bjK01nA4gG0hg` |
| Computerphile | @Computerphile | `UC9-y-6csu5mg-rbJ1dL7V5A` |

## Business/Entrepreneurship Channels

| Channel | Channel ID |
|---------|-----------|
| Y Combinator | `UCcefcZRL2oaA_uBNeo5UOWg` |
| Ali Abdaal | `UCoOae5nYzcosPVc4DescXIQ` |

## Science/Learning Channels

| Channel | Channel ID |
|---------|-----------|
| 3Blue1Brown | `UCYO_jab_esuFRV4b0cTApqQ` |
| Kurzgesagt | `UCzIL6qFP00w10hgxZwplZww` |
| Veritasium | `UCHnyfMX85OO8dBj8dNrSQdA` |

---

## How to Test gh-focus

### 1. Run the app
```bash
cd C:\Users\Pakeeza\Desktop\github-cli-challenge\gh-focus
python gh-focus
```

### 2. Add a Channel
- Select `+ Add New Channel`
- Choose category: `coding`
- **Try Handle First:** Type `@Fireship` (auto-resolve)
  - ✅ If it works, you'll see "Found ID ..."
  - ❌ If it fails, press "Y" to enter ID manually
- **Fallback:** Enter the Channel ID directly: `UCsBjURrPoezykLs9EqgamOA`

### 3. View Added Channels
- Go back to main menu
- Select `👀 View Channels`
- You should see your added channels listed!

### 4. Try Fetching Videos
- Select the category you added (e.g., `coding`)
- App fetches videos (should be **fast** with parallel fetching)
- Select a video → "Stream" or "Save to Learning Log"

---

## Troubleshooting

**Q: Resolution fails even with @Fireship?**
- A: Use the fallback manual ID entry. Copy one from the table above.

**Q: Can't see my channels after adding?**
- A: Go to Main Menu → `👀 View Channels` to verify they're in config.json

**Q: Where is my data stored?**
- A: Check `gh-focus/config.json` (channels) and `gh-focus/watch_history.json` (video history)
