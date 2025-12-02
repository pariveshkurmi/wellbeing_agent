"""
Hugging Face Spaces entry point for Wellbeing Agent
This file serves as the main entry point for Hugging Face Spaces deployment.
"""
import sys
from pathlib import Path

# Add src directory to path so we can import wellbeing_agent
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from wellbeing_agent.app import create_ui, initialize_crew

# Initialize crew on import
initialize_crew()

# Create and expose the Gradio app
demo = create_ui()

if __name__ == "__main__":
    demo.launch()
