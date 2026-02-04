# Developer CLI Challenge

## ⚠️ Setup & Environment Challenges (Browser + Local Machine)

### 1. GitHub Copilot CLI Requires PowerShell 6+ (pwsh)

**Issue:**
When running:

```bash
gh copilot /init
```

I repeatedly received errors like:

```
'pwsh.exe' is not recognized as an internal or external command
PowerShell 6+ (pwsh) is not available
```

**Cause:**
GitHub Copilot CLI internally uses PowerShell 6+ (`pwsh`) on Windows, but only Windows PowerShell (`powershell.exe`) was installed on my system.

**Impact:**
Copilot CLI could not:

* List repository files
* Create `.github` directory
* Generate `copilot-instructions.md`

**Workaround / Learning:**

* Understood that installing PowerShell 6+ is required **or**
* Manually create the `.github` folder and `copilot-instructions.md` file.

---

### 2. Repository Appeared Empty After Initialization

**Issue:**
After running:

```bash
git init
```

Copilot CLI reported:

```
The repository appears to be empty except for the .git directory
```

**Cause:**
No project files existed yet—only the `.git` folder.

**Impact:**
Copilot CLI could not infer project type or generate smart instructions.

**Workaround / Learning:**

* Learned that at least one file (README, source file, or instructions) should exist before running Copilot initialization.

---

### 3. Git Bash vs PowerShell Command Compatibility

**Issue:**
Copilot CLI attempted to run PowerShell-style commands inside Git Bash:

```
Get-ChildItem
dir /a
```

These failed inside Git Bash.

**Cause:**
Copilot CLI assumes PowerShell environment on Windows, while I was using Git Bash.

**Impact:**
Automatic repository scanning failed.

**Workaround / Learning:**

* Learned to either:

  * Use Windows Terminal with PowerShell 6+, or
  * Perform file creation manually in Git Bash.

---

### 4. Copilot Instructions File Not Auto-Created

**Issue:**
Even after running `/init`, the file:

```
.github/copilot-instructions.md
```

was not created.

**Cause:**
Both:

* Missing PowerShell 6+
* Empty repository

**Workaround / Learning:**
Manually created:

```bash
mkdir .github
touch .github/copilot-instructions.md
```

and added basic instructions.

---

### 5. Understanding Copilot CLI Command Flow

**Issue:**
Initially unclear what:

```
gh copilot
/init
```

actually do.

**Learning Outcome:**

* `gh copilot` opens Copilot CLI mode
* `/init` initializes project-specific Copilot behavior
* Copilot relies heavily on repository context

This clarified how Copilot integrates with local projects.

---

### 6. Windows PATH & Tooling Awareness

**Issue:**
Some commands failed because required tools were not present in PATH.

**Learning Outcome:**

* Learned importance of verifying installed tools:

  ```bash
  git --version
  gh --version
  pwsh --version
  ```
* Better understanding of environment configuration on Windows.

---

### 7. Copilot Agent vs Interactive CLI Scripts (The "Bad Middleman" Problem)

**Issue:**
When asking GitHub Copilot to run the `gh-focus` CLI tool via agent, it would:
- Start the script
- The script displays the interactive menu (arrow keys, selection prompts)
- Copilot agent hangs or terminates the process
- Error: "The application exited unexpectedly"

```
Script started, waiting for user input (arrow keys)...
✗ Copilot Agent: "Hmm, nothing's happening. Killing process..."
Exit code: 1
```

**Root Cause:**
The fundamental limitation of Copilot agents:

* **Fire-and-Forget Design** - Agents expect: `command → output → exit`
* **Interactive Scripts Need Persistence** - `gh-focus` requires: `command → await input → process input → loop`
* **Keyboard Hijacking** - Interactive CLI tools take over STDIN/STDOUT and wait for keypresses (↑, ↓, Enter)
* **Agent Timeout** - Copilot agents don't understand "waiting for input" and assume the process hung

**Technical Breakdown:**
```
Normal Command:           Interactive CLI:
python script.py ──────→ Output ──────→ Exit    ✓ Works
                (Copilot happy)

gh-focus ──────→ Show Menu ──────→ Waiting for keys... (Copilot confused)
                            ↑↓ INPUT NEEDED
                            (Agent kills process)
                            ✗ Fails
```

**Impact:**
* Could not demonstrate the tool interactively via Copilot chat
* Had to manually run the tool in the terminal
* Revealed architectural understanding about CLI design patterns

**Workaround / Learning:**

* **Manual Execution** - Click into VS Code's Terminal panel and run:
  ```bash
  python gh-focus
  ```
  Then use physical keyboard arrow keys to interact.

* **Key Insight**: Copilot agents are great for:
  - ✅ Running scripts that output and exit
  - ✅ Build commands (`npm run build`)
  - ✅ Package installation (`pip install`)
  - ❌ NOT for: Interactive TUIs, games, prompts requiring realtime input

* **CLI Design Lesson**: When building GitHub CLI extensions:
  - Interactive tools must be **run manually** by the user
  - Provide clear documentation about how to invoke them
  - The extension itself shouldn't rely on agent execution
  - This is actually a feature, not a bug!

**Why This Matters:**
This limitation actually makes sense from an architecture perspective. GitHub CLI extensions are meant to be **user-facing tools** that you invoke directly, not agent-mediated tasks. Understanding this difference is crucial for CLI design.

---

## ✅ Overall Learning

These struggles improved my understanding of:

* Windows development environments
* Shell differences (Git Bash vs PowerShell)
* GitHub CLI ecosystem
* How Copilot CLI analyzes repositories
* The distinction between **CLI agents** vs **interactive terminal applications**
* Architectural design patterns for developer tools

This setup phase strengthened my debugging, problem-solving, and system design thinking.