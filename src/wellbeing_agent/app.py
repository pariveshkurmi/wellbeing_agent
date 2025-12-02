import gradio as gr
from wellbeing_agent.crew import WellbeingCrew
import threading

# Initialize the crew once
crew = None
crew_lock = threading.Lock()

def initialize_crew():
    """Initialize the crew in a thread-safe manner"""
    global crew
    with crew_lock:
        if crew is None:
            crew = WellbeingCrew()
    return crew

def process_message(message, history):
    """Process user message and return response"""
    if not message.strip():
        return history, ""
    
    # Check for exit commands
    if message.lower().strip() in ["exit", "quit", "bye", "goodbye"]:
        history.append({"role": "user", "content": message})
        history.append({
            "role": "assistant", 
            "content": "Take care! See you soon. Feel free to come back anytime you need support. 💚"
        })
        return history, ""
    
    # Initialize crew if needed
    if crew is None:
        initialize_crew()
    
    # Add user message to history
    history.append({"role": "user", "content": message})
    
    try:
        # Step 1: Classify intent
        classify_task = crew.classify_intent(message)
        intent_result = crew.get_crew([classify_task]).kickoff(inputs={"user_input": message})
        
        # Step 2: Respond based on intent
        agent_key = str(intent_result).strip().lower()
        if f"handle_{agent_key}" in crew.tasks_config["tasks"]:
            response_task = crew.respond_to_intent(agent_key, message)
        else:
            response_task = crew.respond_to_intent("knowledge", message)
        
        response = crew.get_crew([response_task]).kickoff(inputs={"user_input": message})
        
        # Add assistant response to history
        history.append({"role": "assistant", "content": str(response)})
        
    except Exception as e:
        error_msg = f"I apologize, but I encountered an error: {str(e)}. Please try again."
        history.append({"role": "assistant", "content": error_msg})
    
    return history, ""

def create_ui():
    """Create the Gradio UI"""
    custom_css = """
    .gradio-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        max-width: 900px;
        margin: 0 auto;
    }
    .main-header {
        text-align: center;
        padding: 30px 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.5em;
        font-weight: 600;
    }
    .main-header p {
        margin: 10px 0 0 0;
        font-size: 1.1em;
        opacity: 0.95;
    }
    .chat-container {
        min-height: 500px;
        border-radius: 10px;
    }
    .footer {
        margin-top: 20px;
        padding: 15px;
        background: #f8f9fa;
        border-radius: 10px;
    }
    """
    
    with gr.Blocks(
        title="Wellbeing Agent",
        css=custom_css
    ) as demo:
        
        # Header
        gr.Markdown(
            """
            <div class="main-header">
                <h1>🌿 Wellbeing Agent 🌿</h1>
                <p>Your personal wellbeing companion for mood, stress, sleep, motivation, and general wellness support</p>
            </div>
            """,
            elem_classes=["main-header"]
        )
        
        # Chat interface
        chatbot = gr.Chatbot(
            label="Chat",
            height=500,
            type="messages",
            show_copy_button=True,
            bubble_full_width=False
        )
        
        # Input area
        with gr.Row():
            msg = gr.Textbox(
                label="",
                placeholder="How are you feeling today? Ask me about mood, stress, sleep, motivation, or general wellness...",
                scale=9,
                show_label=False,
                container=False
            )
            submit_btn = gr.Button("Send", variant="primary", scale=1, min_width=100)
        
        # Clear button
        clear_btn = gr.Button("Clear Chat", variant="secondary")
        
        # Event handlers
        msg.submit(process_message, [msg, chatbot], [chatbot, msg])
        submit_btn.click(process_message, [msg, chatbot], [chatbot, msg])
        clear_btn.click(lambda: ([], ""), outputs=[chatbot, msg])
        
        # Footer
        gr.Markdown(
            """
            <div style="text-align: center; padding: 20px; color: #666;">
                <p>💡 <strong>Tips:</strong> Try asking about your mood, stress levels, sleep habits, motivation, or any wellness questions</p>
                <p style="font-size: 0.9em; margin-top: 10px;">Type 'exit' or 'quit' to end the conversation</p>
            </div>
            """,
            elem_classes=["footer"]
        )
    
    return demo

def main():
    """Main entry point for the UI"""
    # Initialize crew on startup
    initialize_crew()
    
    # Create and launch UI
    demo = create_ui()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        inbrowser=True
    )

# For Hugging Face Spaces compatibility
if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

