@echo off
REM GitHub CLI extension entry point for Windows
REM This allows "gh focus" to work from anywhere

setlocal enabledelayedexpansion

REM Get the directory where this script is located
set "SCRIPT_DIR=%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is required but not found.
    echo Please install Python 3.7+ from https://www.python.org/downloads/
    exit /b 1
)

REM Change to the script directory
cd /d "%SCRIPT_DIR%"

REM Run the Python script with all arguments passed through
python gh-focus %*
exit /b %errorlevel%
