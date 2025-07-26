# 🤖 AI Companion Studio

A local AI companion application built with Gradio and LM Studio for creating personalized AI chatbots with persistent memory and customizable personalities.

## ✨ Features

- 💬 **Interactive Chat Interface** - Real-time conversations with your AI companion
- 🎭 **Personality Customization** - Detailed personality traits and characteristics
- 🧠 **Memory Management** - Persistent conversation history and character development
- ⚙️ **Model Settings** - Easy integration with LM Studio local models
- 🎨 **Modern UI** - Clean, tabbed interface built with Gradio

## 🛠️ Technology Stack

- **Frontend**: Gradio (Python web UI framework)
- **Backend**: Python with modular architecture
- **AI Models**: LM Studio (local OpenAI-compatible API)
- **Memory**: JSON-based storage with future vector database support
- **UI Components**: Tabs, accordions, sliders, chat interface

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- LM Studio installed and running
- Git (for cloning)

### Installation

1. **Clone the repository**
   ```powershell
   git clone <repository-url>
   cd Gradiodev
   ```

2. **Set up virtual environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Start LM Studio**
   - Open LM Studio
   - Load your preferred model
   - Start the local server (default: http://localhost:1234)

5. **Run the application**
   ```powershell
   python app.py
   ```

6. **Open in browser**
   - Navigate to http://127.0.0.1:7860

## 📁 Project Structure

```
Gradiodev/
├── app.py                 # Main application entry point
├── components/
│   ├── chat_ui.py         # Chat interface components
│   ├── persona.py         # Personality configuration UI
│   └── settings_ui.py     # Settings and model configuration
├── data/                  # User data and conversations (git-ignored)
├── static/                # Static assets
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🎯 Usage

### Chat Tab
- Engage in conversations with your AI companion
- Adjust creativity and response length in real-time
- View conversation statistics and character status

### Persona Tab
- Customize personality traits using Big Five model
- Set interests, communication style, and background
- Preview changes in real-time

### Settings Tab
- Configure LM Studio connection
- Select and switch between models
- Adjust generation parameters

### Memory Tab
- View conversation history
- Manage memory retention settings
- Export/import conversation data

## 🔧 Configuration

The application connects to LM Studio on `http://localhost:1234` by default. You can modify this in the Settings tab or by editing the configuration.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Gradio](https://gradio.app/) for the excellent web UI framework
- [LM Studio](https://lmstudio.ai/) for local model hosting
- The open-source AI community for model development

## 📞 Support

If you encounter any issues or have questions:
- Check the [Issues](../../issues) page
- Create a new issue with detailed information
- Join our community discussions

---

*Created with ❤️ for local AI enthusiasts*
