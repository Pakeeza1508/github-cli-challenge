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

## ✅ Overall Learning

These struggles improved my understanding of:

* Windows development environments
* Shell differences (Git Bash vs PowerShell)
* GitHub CLI ecosystem
* How Copilot CLI analyzes repositories

This setup phase strengthened my debugging and self-learning skills.