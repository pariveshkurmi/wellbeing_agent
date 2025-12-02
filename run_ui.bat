@echo off
REM Windows batch script to run the Wellbeing Agent UI
cd /d "%~dp0"
echo Starting Wellbeing Agent UI...
echo.
uv run python -m wellbeing_agent.app
if errorlevel 1 (
    echo.
    echo Error occurred. Make sure you're in the project root directory.
    pause
)

