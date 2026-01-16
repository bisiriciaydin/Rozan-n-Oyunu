import streamlit as st

def apply_ui_css():
    st.markdown("""
    <style>
    body { color:#111; font-weight:700; }

    .game-card{
        background:#fff;
        border-radius:18px;
        padding:18px;
        margin-bottom:12px;
        box-shadow:0 6px 16px rgba(0,0,0,.10);
        text-align:center;
    }
    .game-card h2{ font-size:26px; margin:0 0 6px 0; color:#111; }
    .game-card p{ font-size:18px; margin:0; color:#222; }

    /* BÜYÜK GERİ BİLDİRİM (ekranı doldurur) */
    .feedback{
        position:fixed;
        inset:0;
        background:rgba(255,255,255,.96);
        display:flex;
        align-items:center;
        justify-content:center;
        z-index:99999;
        text-align:center;
        padding:20px;
    }
    .feedback h1{ font-size:64px; margin:0 0 12px 0; }
    .feedback p{ font-size:28px; margin:0; }
    </style>
    """, unsafe_allow_html=True)

def set_feedback(kind: str, title: str, message: str):
    # kind: "ok", "try", "time"
    colors = {"ok": "#22c55e", "try": "#f97316", "time": "#ef4444"}
    st.session_state["feedback"] = {
        "title": title,
        "message": message,
        "color": colors.get(kind, "#111111")
    }

def render_feedback():
    fb = st.session_state.get("feedback")
    if not fb:
        return

    st.markdown(f"""
    <div class="feedback">
      <div>
        <h1 style="color:{fb["color"]};">{fb["title"]}</h1>
        <p>{fb["message"]}</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Devam butonu (mesajı kapatır)
    st.write("")
    if st.button("➡️ Devam", use_container_width=True):
        st.session_state["feedback"] = None
        st.rerun()

