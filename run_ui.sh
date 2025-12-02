#!/bin/bash
# Shell script to run the Wellbeing Agent UI
cd "$(dirname "$0")"
echo "Starting Wellbeing Agent UI..."
uv run python -m wellbeing_agent.app

