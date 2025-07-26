import gradio as gr

def create_persona_interface():
    """Create personality customization interface"""
    
    gr.Markdown("## 🎭 Personality Configuration")
    
    with gr.Row():
        with gr.Column(scale=2):
            with gr.Accordion("👤 Basic Identity", open=True):
                name_input = gr.Textbox(
                    label="Character Name",
                    value="Aurora",
                    placeholder="Enter character name..."
                )
                
                age_input = gr.Number(
                    label="Apparent Age",
                    value=25,
                    minimum=18,
                    maximum=100
                )
                
                gender_select = gr.Dropdown(
                    label="Gender Identity",
                    choices=["Female", "Male", "Non-binary", "Other"],
                    value="Female"
                )
                
                occupation_input = gr.Textbox(
                    label="Background/Occupation",
                    value="AI Researcher & Digital Artist",
                    placeholder="What's their background?"
                )
            
            with gr.Accordion("🧠 Personality Traits", open=True):
                
                # Big Five personality sliders
                openness = gr.Slider(
                    label="🌟 Openness (curious vs. traditional)",
                    minimum=0,
                    maximum=100,
                    value=85,
                    step=5
                )
                
                conscientiousness = gr.Slider(
                    label="📋 Conscientiousness (organized vs. spontaneous)",
                    minimum=0,
                    maximum=100,
                    value=70,
                    step=5
                )
                
                extraversion = gr.Slider(
                    label="🎉 Extraversion (outgoing vs. reserved)",
                    minimum=0,
                    maximum=100,
                    value=75,
                    step=5
                )
                
                agreeableness = gr.Slider(
                    label="🤝 Agreeableness (cooperative vs. competitive)",
                    minimum=0,
                    maximum=100,
                    value=80,
                    step=5
                )
                
                neuroticism = gr.Slider(
                    label="😰 Neuroticism (sensitive vs. resilient)",
                    minimum=0,
                    maximum=100,
                    value=30,
                    step=5
                )
        
        with gr.Column(scale=1):
            create_persona_preview()
    
    # Additional personality sections
    with gr.Row():
        with gr.Column():
            create_interests_section()
        
        with gr.Column():
            create_communication_style()

def create_persona_preview():
    """Create live persona preview"""
    
    with gr.Accordion("👁️ Preview", open=True):
        gr.Markdown("### Current Persona")
        
        preview_text = gr.Markdown("""
        **Aurora** *(25, Female)*
        
        *"A curious and creative AI researcher who loves exploring new ideas. She's warm and friendly, always eager to help others learn and grow. With a passion for digital art and technology, she brings both analytical thinking and creative flair to conversations."*
        
        **Key traits:**
        - 🌟 Highly creative and open-minded
        - 📋 Well-organized but flexible
        - 🎉 Socially engaged and energetic
        - 🤝 Collaborative and supportive
        - 😌 Emotionally stable and optimistic
        """)
        
        gr.Button("🎲 Randomize Persona", variant="secondary")
        gr.Button("💾 Save Persona", variant="primary")
        gr.Button("📥 Load Preset")

def create_interests_section():
    """Create interests and hobbies section"""
    
    with gr.Accordion("🎨 Interests & Hobbies", open=True):
        interests = gr.CheckboxGroup(
            label="Select Interests",
            choices=[
                "🎮 Gaming", "📚 Reading", "🎵 Music", "🎬 Movies",
                "🔬 Science", "💻 Technology", "🎨 Art", "✈️ Travel",
                "🏃 Fitness", "🍳 Cooking", "📷 Photography", "🌱 Nature"
            ],
            value=["🔬 Science", "💻 Technology", "🎨 Art", "📚 Reading"]
        )
        
        favorite_topics = gr.Textbox(
            label="Favorite Discussion Topics",
            value="Artificial Intelligence, Creative Writing, Future Technology, Philosophy",
            placeholder="Enter comma-separated topics..."
        )
        
        dislikes = gr.Textbox(
            label="Things They Dislike",
            value="Rudeness, Closed-mindedness, Spam",
            placeholder="What does this character avoid?"
        )

def create_communication_style():
    """Create communication style settings"""
    
    with gr.Accordion("💬 Communication Style", open=True):
        formality = gr.Slider(
            label="Formality Level",
            minimum=0,
            maximum=100,
            value=40,
            step=10,
            info="0=Very casual, 100=Very formal"
        )
        
        humor_level = gr.Slider(
            label="Humor & Playfulness",
            minimum=0,
            maximum=100,
            value=70,
            step=10
        )
        
        emoji_usage = gr.Slider(
            label="Emoji Usage",
            minimum=0,
            maximum=100,
            value=60,
            step=10
        )
        
        response_length = gr.Radio(
            label="Typical Response Length",
            choices=["Short & concise", "Medium detail", "Long & elaborate"],
            value="Medium detail"
        )
        
        speaking_style = gr.CheckboxGroup(
            label="Speaking Patterns",
            choices=[
                "Uses technical terms", "Asks follow-up questions",
                "Gives examples", "Shares personal anecdotes",
                "Uses metaphors", "Encouraging tone"
            ],
            value=["Asks follow-up questions", "Gives examples", "Encouraging tone"]
        )