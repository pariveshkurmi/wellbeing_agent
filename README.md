---
title: Wellbeing Agent
emoji: 🌿
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
short_description: Wellbeing companion powered by CrewAI + Gemini
---

# 🌿 Wellbeing Agent

Welcome to the Wellbeing Agent project, powered by [crewAI](https://crewai.com) and deployed with [Gradio](https://www.gradio.app/). This app brings together multiple specialized wellbeing agents—covering mood, stress, sleep, motivation, and general knowledge—to provide supportive, actionable guidance.

## Features

- **Intent Routing**: A router agent classifies the user’s request and picks the right specialist.
- **Dedicated Agents**: Mood, Stress, Sleep, Motivation, and Knowledge agents each have tailored prompts and goals.
- **Gradio Chat UI**: Beautiful, responsive chat interface with copy-friendly bubbles and helpful tips.
- **Thread-Safe Crew Init**: The CrewAI crew is initialized once and reused across requests.

## Local Installation

1. Ensure Python `>=3.10,<3.14` is installed.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your environment variable(s):

```bash
export GOOGLE_API_KEY="your-google-api-key"
```

4. Run the Gradio UI:

```bash
python app.py
```

This launches the UI at `http://localhost:7860`.

## Project Scripts

`pyproject.toml` exposes several helpful entry points via `uv run` or `python -m`:

- `run_ui` / `wellbeing_agent.app:main` – start the Gradio interface
- `run_crew` / `wellbeing_agent.main:run` – CLI runner for CrewAI
- `train`, `replay`, `test`, `run_with_trigger` – scaffolding for advanced workflows

On Windows you can also double-click `run_ui.bat`; on Linux/macOS, use `run_ui.sh`.

## Hugging Face Spaces Deployment

This repository is ready for Spaces:

1. Upload (or push via Git) the entire repo to your Space.
2. Ensure `requirements.txt` lives at the repo root.
3. Keep this `README.md` with the YAML front matter so Spaces renders metadata.
4. Set the `GOOGLE_API_KEY` secret in **Settings → Variables and secrets**.

For detailed instructions, see `DEPLOYMENT.md`.

## Support & Customization

- Modify `src/wellbeing_agent/config/agents.yaml` to tweak agent personas or models.
- Update `src/wellbeing_agent/config/tasks.yaml` to adjust task prompts and outputs.
- Extend `src/wellbeing_agent/tools/` for custom tool integrations.
- Documentation: [crewAI Docs](https://docs.crewai.com)

Let’s build supportive, empathetic agents together. 💚
