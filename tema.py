# tema.py
import streamlit as st

TEMALAR = {
    "Pembe 🌸": {"bg": "#fff5fb", "card": "#ffffff", "text": "#2b2b2b", "accent": "#ff4da6"},
    "Mavi 🌈":  {"bg": "#f0f7ff", "card": "#ffffff", "text": "#1f2a37", "accent": "#3b82f6"},
    "Yeşil 🍀": {"bg": "#f3fff5", "card": "#ffffff", "text": "#1f2a37", "accent": "#22c55e"},
}

def tema_secici():
    """Sidebar'dan tema seçtirir ve seçimi session_state'e yazar."""
    if "tema_adi" not in st.session_state:
        st.session_state.tema_adi = "Pembe 🌸"

    st.sidebar.markdown("### 🎨 Tema Seç")
    secim = st.sidebar.selectbox("Bir tema seç:", list(TEMALAR.keys()), index=list(TEMALAR.keys()).index(st.session_state.tema_adi))
    st.session_state.tema_adi = secim
    return TEMALAR[secim]

def tema_uygula(tema: dict):
    """Seçilen temayı CSS ile uygular."""
    css = f"""
    <style>
      .stApp {{ background: {tema["bg"]}; color: {tema["text"]}; }}
      .roza-card {{
        background: {tema["card"]};
        border-radius: 16px;
        padding: 16px;
        border: 2px solid {tema["accent"]}22;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
      }}
      .roza-accent {{ color: {tema["accent"]}; font-weight: 700; }}
      div.stButton > button {{
        background: {tema["accent"]};
        color: white;
        border-radius: 14px;
        border: none;
        padding: 10px 14px;
        font-weight: 700;
      }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
