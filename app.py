import streamlit as st
import requests
import time

# --- Setup ---
API_URL = "http://localhost:8000/query"

st.set_page_config(
    page_title="AI Power | Chat Bot",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom Styling (The "Orb" Design) ---
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at top right, #fdf4f7, #f5f7ff, #ffffff);
    }
    
    /* Ensure sidebar toggle is visible but keep the rest of the header clean */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.6) !important;
        backdrop-filter: blur(25px);
        border-right: 1px solid rgba(255, 255, 255, 0.4);
        min-width: 300px !important;
    }

    .orb-container {
        display: flex;
        justify-content: center;
        padding: 50px 0;
    }

    .orb {
        width: 160px;
        height: 160px;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #ffd1ff, #d1e5ff 40%, #ff89d6 70%, #7dbdff 100%);
        box-shadow: 0 0 60px rgba(255, 137, 214, 0.4), inset -10px -10px 40px rgba(0,0,0,0.1);
        animation: float 6s ease-in-out infinite, rotate 10s linear infinite;
        position: relative;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }

    .headline {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 40px;
        color: #1a1a1a;
    }
    .headline span {
        background: linear-gradient(90deg, #ff4b91, #7dbdff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Message Bubbles */
    div[data-testid="stChatMessageUser"] .stMarkdown {
        background: #ff4b91 !important;
        color: white !important;
        border-radius: 20px 20px 4px 20px !important;
        box-shadow: 0 4px 15px rgba(255, 75, 145, 0.3) !important;
    }

    div[data-testid="stChatMessageAssistant"] .stMarkdown {
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.8) !important;
        border-radius: 20px 20px 20px 4px !important;
    }

    div[data-testid="stChatMessageAvatarAssistant"], div[data-testid="stChatMessageAvatarUser"] {
        display: none;
    }

    .stChatInputContainer {
        border-radius: 30px !important;
        background: rgba(255, 255, 255, 0.8) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 75, 145, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #ff4b91;'>🔮 AI HUB</h2>", unsafe_allow_html=True)
    st.divider()
    st.button("✨ New Chat", use_container_width=True)
    st.button("📁 Documents", use_container_width=True)
    st.button("⚙️ Settings", use_container_width=True)

# --- State Management ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Initial Hero View ---
if not st.session_state.messages:
    st.markdown("""
        <div class="orb-container">
            <div class="orb"></div>
        </div>
        <div class="headline">Personalized <span> Chat Bot </span> For <br> You </div>
    """, unsafe_allow_html=True)

# --- Chat Rendering ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat Input ---
if prompt := st.chat_input("Ask me anything..."):
    # Clear hero manually isn't needed, Streamlit reruns
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("🔍 Searching*")
        
        try:
            # Call FastAPI Backend
            response = requests.post(API_URL, json={"query": prompt})
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer found.")
                
                # Typing effect
                full_text = ""
                for char in answer:
                    full_text += char
                    placeholder.markdown(full_text + "▌")
                    time.sleep(0.005)
                placeholder.markdown(full_text)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                placeholder.error("Backend error. Make sure main.py is running.")
        except Exception as e:
            placeholder.error(f"Connection failed: {e}")
