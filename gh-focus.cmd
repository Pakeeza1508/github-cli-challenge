@echo off
REM GitHub CLI extension entry point for Windows
REM This script runs the Python CLI

setlocal

REM Get the directory where the extension is installed
set "EXTENSION_DIR=%~dp0"

REM Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: Python is required but not found.
    echo Please install Python 3.7+ from https://www.python.org/downloads/
    exit /b 1
)

REM Check if virtual environment exists, create if not
if not exist "%EXTENSION_DIR%gh-focus\venv" (
    echo Setting up gh-focus for first time...
    python -m venv "%EXTENSION_DIR%gh-focus\venv"
    call "%EXTENSION_DIR%gh-focus\venv\Scripts\activate.bat"
    pip install -q -r "%EXTENSION_DIR%gh-focus\requirements.txt"
    echo Setup complete!
)

REM Activate virtual environment
call "%EXTENSION_DIR%gh-focus\venv\Scripts\activate.bat"

REM Run the actual Python script
cd /d "%EXTENSION_DIR%gh-focus"
python gh-focus %*
