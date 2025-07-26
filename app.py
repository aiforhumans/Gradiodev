import gradio as gr
from components.chat_ui import create_chat_interface
from components.persona import create_persona_interface
from components.settings_ui import create_settings_interface

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
                create_memory_interface()
    
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
                    gr.Button("🗑️ Clear History", variant="stop")
                    gr.Button("💾 Export History")
                    gr.Button("🔄 Refresh")
        
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

if __name__ == "__main__":
    demo = create_main_interface()
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        debug=True
    )