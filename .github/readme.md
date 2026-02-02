# Developer CLI Challenge

## Challenges Faced & Setup
While setting up the GitHub Copilot CLI extension on Windows, I encountered a dependency error.

**The Error:**
When running `gh copilot` or `/init`, the process crashed with:
`Error: Command failed: pwsh.exe --version. 'pwsh.exe' is not recognized`

**The Cause:**
The Copilot CLI extension requires **PowerShell Core (pwsh)** to execute background tasks. Although I was running commands in Git Bash, the extension still needed the underlying `pwsh` executable, which is different from the standard Windows PowerShell.

**The Fix:**
I had to manually install PowerShell 7+ using Winget:
`winget install Microsoft.PowerShell`

After a restart of the terminal, the `/init` command worked successfully.