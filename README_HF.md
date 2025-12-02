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
---

# 🌿 Wellbeing Agent

Your personal wellbeing companion powered by CrewAI and Gradio. Get support for mood, stress, sleep, motivation, and general wellness questions through an interactive chat interface.

Your personal wellbeing companion powered by CrewAI and Gradio. Get support for mood, stress, sleep, motivation, and general wellness questions through an interactive chat interface.

## Features

- **Mood Support**: Get help reflecting on emotions and finding balance
- **Stress Management**: Receive grounding, breathing, and relaxation practices
- **Sleep Guidance**: Improve sleep habits and bedtime routines
- **Motivation**: Get encouragement with small achievable wellbeing goals
- **Knowledge Base**: Ask general wellbeing-related questions

## How to Use

1. Start chatting by typing your question or concern
2. The agent will automatically route your message to the appropriate specialist
3. Receive personalized, empathetic responses with actionable suggestions

## Setup

### Environment Variables

This app requires a Google API key for Gemini models. Set the following environment variable in your Hugging Face Space:

- `GOOGLE_API_KEY`: Your Google API key for Gemini models

You can set this in your Space settings under "Repository secrets" or "Variables and secrets".

### Local Development

To run locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export GOOGLE_API_KEY=your_key_here

# Run the app
python app.py
```

## Technology Stack

- **CrewAI**: Multi-agent AI framework
- **Gradio**: Web interface
- **Google Gemini**: LLM backend
- **Python**: Core language

## License

MIT License

