import gradio as gr
import os
import json
import logging
from datetime import datetime
from components.chat_ui import create_chat_interface
from components.persona import create_persona_interface
from components.settings_ui import create_settings_interface

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Global state
app_state = {
    "api_connected": False,
    "current_model": None,
    "persona_saved": False
}

def create_main_interface():
    """Create the main tabbed interface for the AI companion app"""
    
    with gr.Blocks(
        title="AI Companion Studio",
        theme=gr.themes.Soft(),
        css="footer {visibility: hidden}"
    ) as demo:
        
        gr.Markdown("# 🤖 AI Companion Studio")
        gr.Markdown("*Build and interact with your AI companion using local models*")
        
        with gr.Tabs() as tabs:
            # Chat Tab
            with gr.TabItem("💬 Chat", id="chat"):
                chat_interface = create_chat_interface()
            
            # Persona Tab
            with gr.TabItem("🎭 Persona", id="persona"):
                persona_interface = create_persona_interface()
            
            # Settings Tab
            with gr.TabItem("⚙️ Settings", id="settings"):
                settings_interface = create_settings_interface()
            
            # Memory Tab
            with gr.TabItem("🧠 Memory", id="memory"):
                memory_interface = create_memory_interface()
        
        # Status indicator at the bottom
        with gr.Row():
            status_box = gr.Textbox(
                value="Ready",
                label="Status",
                interactive=False
            )
            
        # Connect all event handlers
        try:
            logging.debug("Connecting event handlers...")
            connect_event_handlers(chat_interface, persona_interface, settings_interface)
            status_box.value = "✅ Application initialized successfully"
        except Exception as e:
            logging.error(f"Failed to connect event handlers: {str(e)}")
            status_box.value = f"⚠️ Initialization error: {str(e)}"
            gr.Warning(f"Error initializing: {str(e)}")
    
    return demo

def create_memory_interface():
    """Create memory management interface"""
    
    gr.Markdown("## 📚 Memory Management")
    
    with gr.Row():
        with gr.Column(scale=2):
            with gr.Accordion("📖 Conversation History", open=True):
                history_display = gr.Textbox(
                    label="Recent Conversations",
                    value="[Placeholder] Previous conversations would appear here...",
                    lines=10,
                    interactive=False
                )
                
                with gr.Row():
                    clear_btn = gr.Button("🗑️ Clear History", variant="stop")
                    export_btn = gr.Button("💾 Export History")
                    refresh_btn = gr.Button("🔄 Refresh")
                    
                    # Add event handlers directly
                    def clear_history():
                        logging.debug("Clearing conversation history")
                        return "[History cleared]"
                    
                    def export_history(history_text):
                        logging.debug("Exporting conversation history")
                        try:
                            os.makedirs("data/exports", exist_ok=True)
                            export_path = f"data/exports/history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                            with open(export_path, "w", encoding="utf-8") as f:
                                f.write(history_text)
                            return "History exported to " + export_path
                        except Exception as e:
                            logging.error(f"Export error: {str(e)}")
                            return f"Export failed: {str(e)}"
                    
                    def refresh_history():
                        logging.debug("Refreshing conversation history")
                        # In a real app, this would load from storage
                        return "[Placeholder] Refreshed conversation history..."
                    
                    # Connect the handlers
                    clear_btn.click(fn=clear_history, outputs=history_display)
                    export_btn.click(fn=export_history, inputs=history_display, outputs=gr.Textbox(label="Export Status"))
                    refresh_btn.click(fn=refresh_history, outputs=history_display)
        
        with gr.Column(scale=1):
            with gr.Accordion("🎯 Memory Stats", open=True):
                gr.Markdown("""
                **Memory Usage:**
                - Total conversations: 42
                - Memory size: 1.2 MB
                - Last updated: 2 hours ago
                
                **Character Knowledge:**
                - Learned traits: 15
                - Preferences: 8
                - Important events: 3
                """)
            
            with gr.Accordion("🔧 Memory Settings", open=False):
                gr.Slider(
                    label="Memory Retention (days)",
                    minimum=1,
                    maximum=365,
                    value=30,
                    step=1
                )
                
                gr.Checkbox(
                    label="Auto-summarize old conversations",
                    value=True
                )
                
                gr.Checkbox(
                    label="Remember user preferences",
                    value=True
                )
    
    # Return the key components for event handling
    return history_display


def connect_event_handlers(chat_interface, persona_interface, settings_interface):
    """Connect event handlers to UI elements"""
    
    # Unpack the chat interface components (assuming they're returned in this order)
    try:
        chatbot, msg_input, send_btn = chat_interface
        
        # Connect chat send button
        def on_send_message(message, chat_history):
            """Handle sending a new chat message"""
            if not message:
                return chat_history, ""
            
            logging.debug(f"Sending message: {message}")
            
            try:
                # In a real app, this would call the LM Studio API
                bot_response = f"This is a placeholder response to: {message}"
                
                # Update chat history
                chat_history = chat_history + [
                    {"role": "user", "content": message},
                    {"role": "assistant", "content": bot_response}
                ]
                
                return chat_history, ""
            except Exception as e:
                logging.error(f"Error processing message: {str(e)}")
                gr.Warning(f"Error: {str(e)}")
                return chat_history, message
        
        # Connect the send button to the chat function
        send_btn.click(
            fn=on_send_message,
            inputs=[msg_input, chatbot],
            outputs=[chatbot, msg_input],
        )
        
        logging.debug("Chat event handlers connected successfully")
        
    except Exception as e:
        logging.error(f"Failed to connect chat event handlers: {str(e)}")
    
    # Connect persona interface handlers (if needed)
    try:
        if persona_interface:
            # Example (adapt based on your actual returned components)
            save_persona_btn = persona_interface.get("save_btn", None)
            if save_persona_btn:
                def save_persona():
                    """Save persona configuration"""
                    logging.debug("Saving persona")
                    app_state["persona_saved"] = True
                    return "✅ Persona saved!"
                
                save_persona_btn.click(fn=save_persona, outputs=gr.Textbox())
    except Exception as e:
        logging.error(f"Failed to connect persona event handlers: {str(e)}")
    
    # Connect memory interface handlers
    try:
        # Add memory-related event handlers here
        pass
    except Exception as e:
        logging.error(f"Failed to connect memory event handlers: {str(e)}")


def save_settings(server_url, model_name):
    """Save settings to config file"""
    logging.debug(f"Saving settings: {server_url}, {model_name}")
    config = {
        "server_url": server_url,
        "model_name": model_name,
        "timestamp": str(datetime.now())
    }
    
    try:
        os.makedirs("config", exist_ok=True)
        with open("config/settings.json", "w") as f:
            json.dump(config, f, indent=2)
        return "✅ Settings saved successfully"
    except Exception as e:
        logging.error(f"Error saving settings: {str(e)}")
        return f"❌ Error saving settings: {str(e)}"


def debug_info(message):
    """Log debug information"""
    logging.debug(message)
    return message


def test_lm_studio_connection(server_url):
    """Test connection to LM Studio server"""
    import requests
    
    logging.debug(f"Testing connection to LM Studio at {server_url}")
    
    try:
        # Use a 5-second timeout for the connection test
        response = requests.get(f"{server_url}/v1/models", timeout=5)
        
        if response.status_code == 200:
            models = response.json()
            logging.debug(f"Connection successful, available models: {models}")
            return "🟢 Connected", models
        else:
            error_msg = f"Error {response.status_code}: {response.text}"
            logging.error(f"Connection failed: {error_msg}")
            return f"🔴 Error: {error_msg}", None
    except requests.exceptions.ConnectionError:
        logging.error(f"Connection error: Could not connect to {server_url}")
        return "🔴 Error: Connection failed - Is LM Studio running?", None
    except requests.exceptions.Timeout:
        logging.error(f"Connection timeout: {server_url} is not responding")
        return "🔴 Error: Connection timed out", None
    except Exception as e:
        logging.error(f"Unexpected error testing connection: {str(e)}")
        return f"🔴 Error: {str(e)}", None


if __name__ == "__main__":
    try:
        logging.info("Starting AI Companion Studio application...")
        
        # Create data directories if they don't exist
        os.makedirs("data", exist_ok=True)
        os.makedirs("config", exist_ok=True)
        
        # Create main interface
        demo = create_main_interface()
        
        # Launch the Gradio app
        logging.info("Launching web interface on http://127.0.0.1:7860")
        demo.launch(
            server_name="127.0.0.1",
            server_port=7860,
            share=False,
            debug=True
        )
    except KeyboardInterrupt:
        logging.info("Application terminated by user")
    except Exception as e:
        logging.critical(f"Failed to start application: {str(e)}", exc_info=True)
        print(f"ERROR: {str(e)}")
        print("See app.log for more details.")