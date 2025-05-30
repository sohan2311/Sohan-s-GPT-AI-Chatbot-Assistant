# 🤖 Sohan's GPT - AI Chat Assistant

<div align="center">

[Sohan's AI Chatbot Assistant](https://github.com/sohan2311/Sohan-s-GPT-AI-Chatbot-Assistant/blob/3cbf332caafc7b6579a40b3f2053e045599701c0/streamlit_app.py)



**A Beautiful, Feature-Rich AI Chat Interface Powered by Together.ai**



[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Together.ai](https://img.shields.io/badge/Together.ai-FF6B35?style=for-the-badge&logo=ai&logoColor=white)](https://together.ai/)

</div>


---

## 📸 Screenshots

<div align="center">

### Main Chat Interface
![Chat Interface](https://github.com/sohan2311/Sohan-s-GPT-AI-Chatbot-Assistant/blob/901ad3046fe21a50a569d04758f6b350fe5596c1/Chatbot%20Model%20Images/Sohan's%20AI%20Assistant.png)

### Model Selection & Configuration
![Configuration Panel](https://github.com/sohan2311/Sohan-s-GPT-AI-Chatbot-Assistant/blob/901ad3046fe21a50a569d04758f6b350fe5596c1/Chatbot%20Model%20Images/Model%20Selection.png)

### Chat Statistics & Export
![Chat Stats](https://github.com/sohan2311/Sohan-s-GPT-AI-Chatbot-Assistant/blob/7812253b2fd4b4135d956bad5b043ff224ed8fc2/Chatbot%20Model%20Images/Chat%20Stats.png)
![Chatbot model](https://github.com/sohan2311/Sohan-s-GPT-AI-Chatbot-Assistant/blob/d1aa00184300c015d896cc5a603ee10adb4fca9e/Chatbot%20Model%20Images/Chatbot%20Model.png)
![Chat Stats and Export to Json Button](https://github.com/sohan2311/Sohan-s-GPT-AI-Chatbot-Assistant/blob/1e7c7ebcda874b56f6708b6bd331918214a63105/Chatbot%20Model%20Images/Chat%20Stats%20and%20Export%20button.png)

</div>

---

## ✨ Features

### 🎨 **Beautiful UI/UX**
- **Gradient Design**: Modern gradient backgrounds and smooth animations
- **Responsive Layout**: Optimized for desktop and mobile devices
- **Typing Animation**: Real-time typing effect for AI responses
- **Custom Styling**: Hand-crafted CSS for premium look and feel

### 🧠 **Multiple AI Models**
- **Mixtral 8x7B**: High-performance instruction-following model
- **Llama 3 8B/70B**: Meta's latest language models
- **CodeLlama 34B**: Specialized for code generation and assistance

### ⚙️ **Advanced Configuration**
- **Temperature Control**: Adjust creativity (0.0 - 2.0)
- **Token Limit**: Customize response length (50 - 4000 tokens)
- **Real-time Settings**: Change models and parameters on-the-fly

### 📊 **Smart Features**
- **Chat Statistics**: Track message counts and conversation metrics
- **Export Functionality**: Download chat history as JSON
- **Session Management**: Persistent chat history during session
- **Error Handling**: Robust error handling with user-friendly messages

### 🔧 **Technical Excellence**
- **Streaming Support**: Fast response delivery
- **Timeout Protection**: 30-second request timeout
- **API Integration**: Seamless Together.ai API integration
- **State Management**: Efficient Streamlit session state handling

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Together.ai API Key
- Streamlit

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sohan2311/Sohan-s-GPT-AI-Chatbot-Assistant.git
   cd Sohan-s-GPT-AI-Chatbot-Assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment**
   ```bash
   # Create .streamlit/secrets.toml
   mkdir .streamlit
   echo 'TOGETHERAI_API_KEY = "your-api-key-here"' > .streamlit/secrets.toml
   ```

4. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Open your browser**
   ```
   http://localhost:8501
   ```

## 📋 Requirements

Create a `requirements.txt` file:

```txt
streamlit>=1.28.0
requests>=2.31.0
python-dateutil>=2.8.2
```

## 🔑 API Configuration

### Getting Together.ai API Key

1. Visit [Together.ai](https://together.ai/)
2. Sign up for an account
3. Navigate to API section
4. Generate your API key
5. Add it to your Streamlit secrets

### Environment Setup

**Option 1: Streamlit Secrets (Recommended)**
```toml
# .streamlit/secrets.toml
TOGETHERAI_API_KEY = "your-together-ai-api-key"
```

**Option 2: Environment Variables**
```bash
export TOGETHERAI_API_KEY="your-together-ai-api-key"
```

## 🎯 Usage Examples

### Basic Chat
```python
# Simply type your message and get AI responses
"Hello, how are you today?"
```

### Code Assistance
```python
# Ask for programming help
"Write a Python function to calculate fibonacci numbers"
```

### Creative Writing
```python
# Get creative assistance
"Write a short story about a robot learning to paint"
```

## 🏗️ Architecture

```mermaid
graph TD
    A[User Input] --> B[Streamlit Frontend]
    B --> C[Session State Management]
    C --> D[Together.ai API]
    D --> E[AI Model Processing]
    E --> F[Response Generation]
    F --> G[Typing Animation]
    G --> H[Display to User]
```

## 🛠️ Customization

### Adding New Models

```python
model_options = {
    "Your Model Name": "model-id-from-together-ai",
    # Add more models here
}
```

### Styling Modifications

Edit the CSS in the `st.markdown()` section to customize:
- Colors and gradients
- Animations and transitions
- Layout and spacing
- Typography and fonts

### Feature Extensions

The codebase is modular and extensible:
- Add new AI providers
- Implement conversation memory
- Add file upload capabilities
- Create custom chat themes

---

## 📊 Performance

- **Response Time**: < 3 seconds average
- **Concurrent Users**: Supports multiple simultaneous sessions
- **Memory Usage**: Optimized session state management
- **API Efficiency**: Smart request batching and error handling

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Add tests if applicable**
5. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

---

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to functions
- Test your changes locally
- Update documentation as needed

---

## 🙏 Acknowledgments

- **[Together.ai](https://together.ai/)** - For providing excellent AI model APIs
- **[Streamlit](https://streamlit.io/)** - For the amazing web app framework
- **[Meta](https://ai.meta.com/)** - For Llama models
- **[Mistral AI](https://mistral.ai/)** - For Mixtral models

## 📞 Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/sohan2311/Sohan-s-GPT-AI-Chatbot-Assistant/issues)
- **Email**: [sohan.maity2311@gmail.com](mailto:sohan.maity2311@gmail.com)
- **LinkedIn**: [Connect with me on LinkedIn](https://www.linkedin.com/in/sohan-maity-26881a288/)

## 🔄 Version History

- **v1.0.0** - Initial release with core features
- **v1.1.0** - Added multiple model support
- **v1.2.0** - Enhanced UI/UX with animations
- **v1.3.0** - Added export functionality and statistics

## 🎯 Roadmap

- [ ] **Voice Chat**: Add speech-to-text and text-to-speech
- [ ] **File Upload**: Support document and image uploads
- [ ] **Custom Themes**: Multiple UI themes
- [ ] **Conversation Memory**: Long-term chat history
- [ ] **Multi-language**: Support for multiple languages
- [ ] **Mobile App**: Native mobile application

---

<div align="center">

**Built with ❤️ by [Sohan Maity](https://github.com/sohan2311)**

⭐ **Star this repository if you found it helpful!** ⭐

</div>
