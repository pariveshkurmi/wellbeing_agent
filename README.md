# WellbeingAgent Crew

Welcome to the WellbeingAgent Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/wellbeing_agent/config/agents.yaml` to define your agents
- Modify `src/wellbeing_agent/config/tasks.yaml` to define your tasks
- Modify `src/wellbeing_agent/crew.py` to add your own logic, tools and specific args
- Modify `src/wellbeing_agent/main.py` to add custom inputs for your agents and tasks

## Running the Project

### Option 1: Web UI (Recommended)

To launch the beautiful web interface, run one of these commands from the project root:

**Windows:**
```bash
# Easiest: Double-click run_ui.bat or run in PowerShell:
.\run_ui.bat

# Or using uv run python directly:
uv run python -m wellbeing_agent.app
```

**Linux/Mac:**
```bash
# Make executable and run:
chmod +x run_ui.sh
./run_ui.sh

# Or using uv run python directly:
uv run python -m wellbeing_agent.app
```

**Note:** Make sure you're in the project root directory (`3_crew/community_contributions/wellbeing_agent`) when running these commands.

This will open a Gradio web interface in your browser at `http://localhost:7860` where you can chat with the wellbeing agent interactively.

### Option 2: Command Line Interface

To run the agent from the terminal:

```bash
$ crewai run
```

This command initializes the wellbeing_agent Crew, assembling the agents and assigning them tasks as defined in your configuration.

The agent will prompt you for input and provide wellbeing support for mood, stress, sleep, motivation, and general wellness questions.

## Understanding Your Crew

The wellbeing_agent Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the WellbeingAgent Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
