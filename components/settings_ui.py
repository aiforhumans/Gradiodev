import gradio as gr

def create_settings_interface():
    """Create application settings interface"""
    
    gr.Markdown("## ⚙️ Application Settings")
    
    with gr.Row():
        with gr.Column():
            create_model_settings()
        
        with gr.Column():
            create_app_settings()
    
    with gr.Row():
        create_advanced_settings()

def create_model_settings():
    """Create model configuration settings"""
    
    with gr.Accordion("🤖 Model Configuration", open=True):
        # LM Studio connection
        gr.Markdown("**LM Studio Connection:**")
        
        server_url = gr.Textbox(
            label="Server URL",
            value="http://localhost:1234",
            placeholder="http://localhost:1234"
        )
        
        connection_status = gr.Textbox(
            label="Connection Status",
            value="🟢 Connected",
            interactive=False,
            container=False
        )
        
        gr.Button("🔄 Test Connection", variant="secondary", size="sm")
        
        gr.Markdown("---")
        
        # Model selection
        model_select = gr.Dropdown(
            label="Available Models",
            choices=[
                "llama-3.2-3b-instruct",
                "phi-3.5-mini-instruct",
                "mistral-7b-instruct-v0.3",
                "codellama-7b-instruct",
                "neural-chat-7b-v3"
            ],
            value="llama-3.2-3b-instruct",
            info="Select model from LM Studio"
        )
        
        # Model parameters
        gr.Markdown("**Generation Parameters:**")
        
        system_temp = gr.Slider(
            label="Default Temperature",
            minimum=0.1,
            maximum=2.0,
            value=0.7,
            step=0.1
        )
        
        top_p = gr.Slider(
            label="Top-p (nucleus sampling)",
            minimum=0.1,
            maximum=1.0,
            value=0.9,
            step=0.05
        )
        
        max_context = gr.Slider(
            label="Max Context Length",
            minimum=1024,
            maximum=32768,
            value=8192,
            step=1024
        )

def create_app_settings():
    """Create application-level settings"""
    
    with gr.Accordion("🎨 Interface Settings", open=True):
        
        theme_select = gr.Dropdown(
            label="Theme",
            choices=["Soft", "Default", "Monochrome", "Glass"],
            value="Soft"
        )
        
        chat_bubble_style = gr.Radio(
            label="Chat Bubble Style",
            choices=["Rounded", "Square", "Minimal"],
            value="Rounded"
        )
        
        font_size = gr.Slider(
            label="Font Size",
            minimum=12,
            maximum=20,
            value=14,
            step=1
        )
        
        auto_scroll = gr.Checkbox(
            label="Auto-scroll chat",
            value=True
        )
        
        show_timestamps = gr.Checkbox(
            label="Show message timestamps",
            value=False
        )
    
    with gr.Accordion("💾 Data & Privacy", open=True):
        
        save_conversations = gr.Checkbox(
            label="Save conversations locally",
            value=True
        )
        
        auto_backup = gr.Checkbox(
            label="Auto-backup persona data",
            value=True
        )
        
        data_location = gr.Textbox(
            label="Data Storage Location",
            value="./data/",
            placeholder="Path to data folder"
        )
        
        gr.Button("📂 Browse...", size="sm")
        gr.Button("🗑️ Clear All Data", variant="stop", size="sm")

def create_advanced_settings():
    """Create advanced configuration options"""
    
    with gr.Accordion("🔧 Advanced Settings", open=False):
        
        with gr.Row():
            with gr.Column():
                gr.Markdown("**Performance:**")
                
                enable_streaming = gr.Checkbox(
                    label="Enable response streaming",
                    value=True
                )
                
                batch_size = gr.Number(
                    label="Batch processing size",
                    value=1,
                    minimum=1,
                    maximum=10
                )
                
                memory_limit = gr.Slider(
                    label="Memory usage limit (MB)",
                    minimum=100,
                    maximum=2000,
                    value=500,
                    step=50
                )
            
            with gr.Column():
                gr.Markdown("**Logging & Debug:**")
                
                log_level = gr.Dropdown(
                    label="Log Level",
                    choices=["DEBUG", "INFO", "WARNING", "ERROR"],
                    value="INFO"
                )
                
                save_logs = gr.Checkbox(
                    label="Save debug logs",
                    value=False
                )
                
                verbose_output = gr.Checkbox(
                    label="Verbose console output",
                    value=False
                )
        
        with gr.Row():
            gr.Button("💾 Save Settings", variant="primary")
            gr.Button("🔄 Reset to Defaults", variant="secondary")
            gr.Button("📤 Export Settings")
            gr.Button("📥 Import Settings")