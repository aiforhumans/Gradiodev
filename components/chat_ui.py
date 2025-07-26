import gradio as gr

def create_chat_interface():
    """Create the main chat interface with controls"""
    
    with gr.Row():
        with gr.Column(scale=4):
            # Main chat interface
            chatbot = gr.Chatbot(
                value=[
                    {"role": "user", "content": "Hello! How are you today?"},
                    {"role": "assistant", "content": "Hi there! I'm doing great, thanks for asking. How can I help you today?"},
                    {"role": "user", "content": "Tell me about yourself"},
                    {"role": "assistant", "content": "I'm an AI companion designed to have engaging conversations. I have a customizable personality that you can adjust in the Persona tab. What would you like to talk about?"}
                ],
                type="messages",
                height=500,
                show_label=False,
                container=True,
                bubble_full_width=False
            )
            
            with gr.Row():
                msg_input = gr.Textbox(
                    placeholder="Type your message here...",
                    container=False,
                    scale=4,
                    show_label=False
                )
                send_btn = gr.Button("📤 Send", variant="primary", scale=1)
        
        with gr.Column(scale=1, min_width=250):
            create_chat_controls()
    
    return chatbot, msg_input, send_btn

def create_chat_controls():
    """Create chat control panel"""
    
    with gr.Accordion("🎮 Chat Controls", open=True):
        # Quick actions
        gr.Button("🗑️ Clear Chat", variant="stop", size="sm")
        gr.Button("💾 Save Conversation", size="sm")
        gr.Button("🔄 Regenerate Last", size="sm")
        
        gr.Markdown("---")
        
        # Response settings
        gr.Markdown("**Response Settings:**")
        
        temperature = gr.Slider(
            label="🌡️ Creativity",
            minimum=0.1,
            maximum=2.0,
            value=0.8,
            step=0.1,
            info="Higher = more creative"
        )
        
        max_tokens = gr.Slider(
            label="📝 Response Length",
            minimum=50,
            maximum=2000,
            value=500,
            step=50,
            info="Maximum tokens per response"
        )
        
        # Character state
        gr.Markdown("---")
        gr.Markdown("**Character Status:**")
        
        mood_display = gr.Textbox(
            label="Current Mood",
            value="😊 Cheerful",
            interactive=False,
            container=False
        )
        
        energy_display = gr.Textbox(
            label="Energy Level",
            value="⚡ High Energy",
            interactive=False,
            container=False
        )
    
    with gr.Accordion("📊 Conversation Stats", open=False):
        gr.Markdown("""
        **This Session:**
        - Messages: 12
        - Duration: 15 minutes
        - Topics: AI, Technology, Hobbies
        
        **Overall:**
        - Total conversations: 45
        - Favorite topics: Science, Gaming
        - Average session: 22 minutes
        """)