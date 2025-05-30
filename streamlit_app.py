import requests
import streamlit as st
import json
from datetime import datetime
import time


st.set_page_config(
    page_title="Sohan's AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    
    .stTitle {
        text-align: center;
        color: #2E86AB;
        font-size: 3rem !important;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .chat-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 15px 15px 5px 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .assistant-message {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1rem;
        border-radius: 15px 15px 15px 5px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .stats-box {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .model-selector {
        background: rgba(255,255,255,0.9);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    .sidebar .element-container {
        margin-bottom: 1rem;
    }
    
    /* Animation for typing effect */
    @keyframes typing {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    .typing-animation {
        animation: typing 0.5s ease-in-out;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    

    st.markdown('<div class="model-selector">', unsafe_allow_html=True)
    model_options = {
        "Mixtral 8x7B": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "Llama 3 8B": "meta-llama/Llama-3-8b-chat-hf",
        "Llama 3 70B": "meta-llama/Llama-3-70b-chat-hf",
        "CodeLlama 34B": "codellama/CodeLlama-34b-Instruct-hf"
    }
    
    selected_model_name = st.selectbox(
        "🧠 Select Model",
        options=list(model_options.keys()),
        index=0
    )
    selected_model = model_options[selected_model_name]
    st.markdown('</div>', unsafe_allow_html=True)
    

    temperature = st.slider(
        "🌡️ Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Controls randomness in responses"
    )
    
    
    max_tokens = st.slider(
        "📝 Max Tokens",
        min_value=50,
        max_value=4000,
        value=1000,
        step=50,
        help="Maximum length of response"
    )
    
    st.markdown("---")
    

    if "messages" in st.session_state:
        total_messages = len(st.session_state.messages)
        user_messages = len([msg for msg in st.session_state.messages if msg["role"] == "user"])
        assistant_messages = len([msg for msg in st.session_state.messages if msg["role"] == "assistant"])
        
        st.markdown('<div class="stats-box">', unsafe_allow_html=True)
        st.markdown("### 📊 Chat Stats")
        st.write(f"**Total Messages:** {total_messages}")
        st.write(f"**Your Messages:** {user_messages}")
        st.write(f"**AI Responses:** {assistant_messages}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    

    if st.button("🗑️ Clear Chat", help="Clear all messages"):
        st.session_state.messages = []
        st.rerun()
    

    if "messages" in st.session_state and st.session_state.messages:
        if st.button("💾 Export Chat", help="Download chat history"):
            chat_data = {
                "timestamp": datetime.now().isoformat(),
                "model": selected_model_name,
                "messages": st.session_state.messages
            }
            st.download_button(
                label="Download JSON",
                data=json.dumps(chat_data, indent=2),
                file_name=f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )


st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <h1 style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
               -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
               font-size: 3.5rem; font-weight: bold; margin: 0;">
        🤖 Sohan's AI Assistant
    </h1>
    <p style="font-size: 1.2rem; color: #666; margin-top: 0.5rem;">
        Powered by Together.ai • built with 🤍 by <a href="https://www.linkedin.com/in/sohan-maity-26881a288/" target="_blank">Sohan Maity</a>
    </p>
</div>
""", unsafe_allow_html=True)


TOGETHERAI_API_KEY = st.secrets.get("TOGETHERAI_API_KEY", "")

if not TOGETHERAI_API_KEY:
    st.error("🔑 API Key not found! Please add TOGETHERAI_API_KEY to your Streamlit secrets.")
    st.stop()


if "messages" not in st.session_state:
    st.session_state.messages = []


if not st.session_state.messages:
    welcome_message = f"""
    👋 **Welcome to Sohan's AI Assistant!**
    
    I'm powered by **{selected_model_name}** and ready to help you with:
    - ❓ Answering questions
    - 💡 Creative writing
    - 🔧 Problem solving
    - 💻 Coding assistance
    - 📚 Learning support
    
    **What would you like to chat about today?**
    """
    
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(welcome_message)


for i, msg in enumerate(st.session_state.messages):
    avatar = "🤓" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])


prompt = st.chat_input("💬  Type your message here ...", key="chat_input")

if prompt:
    # user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # user message immediately displayed
    with st.chat_message("user", avatar="😚"):
        st.markdown(prompt)
    
    # Generate AI response
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        
        # typing indicator
        with st.spinner("🤔 Thinking..."):
            try:
                response = requests.post(
                    "https://api.together.xyz/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {TOGETHERAI_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": selected_model,
                        "messages": st.session_state.messages,
                        "temperature": temperature,
                        "max_tokens": max_tokens,
                        "stream": False
                    },
                    timeout=30
                )
                
                if response.status_code == 200:
                    reply = response.json()["choices"][0]["message"]["content"]
                    
                    # typing effect
                    typing_placeholder = st.empty()
                    for i in range(0, len(reply), 5):
                        typing_placeholder.markdown(reply[:i] + "▋")
                        time.sleep(0.01)
                    
                    # final message
                    message_placeholder.markdown(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                    
                else:
                    error_msg = f"❌ **Error {response.status_code}:** {response.text}"
                    message_placeholder.markdown(error_msg)
                    
            except requests.exceptions.Timeout:
                message_placeholder.markdown("⏰ **Request timed out.** Please try again.")
            except requests.exceptions.RequestException as e:
                message_placeholder.markdown(f"🌐 **Network error:** {str(e)}")
            except Exception as e:
                message_placeholder.markdown(f"💥 **Unexpected error:** {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>Built using Python LLM , Streamlit & Together.ai | by Sohan Maity ☺️
        <a href="https://github.com/sohan2311/Sohan-s-GPT-AI-Chatbot-Assistant" target="_blank">View Source Code in GitHub</a></p>
    </div>
    """, 
    unsafe_allow_html=True
)