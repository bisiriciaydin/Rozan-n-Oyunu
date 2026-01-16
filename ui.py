# ui.py
import time
import streamlit as st


# =======================
# CSS (Mobil uyumlu + Kartlar + Büyük mesaj)
# =======================
def apply_ui_css():
    st.markdown("""
    <style>
    body { color:#111; font-weight:700; }

    /* Kart */
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

    /* Büyük geri bildirim (ekranı doldurur) */
    .feedback{
        position:fixed;
        inset:0;
        background:rgba(255,255,255,.96);
        display:flex;
        align-items:center;
        justify-content:center;
        z-index:99999;
        text-align:center;
        padding:24px;
    }
    .feedback .box{
        max-width:900px;
        width:100%;
    }
    .feedback h1{
        font-size:64px;
        line-height:1.05;
        margin:0 0 14px 0;
    }
    .feedback p{
        font-size:28px;
        margin:0;
        color:#111;
    }
    .feedback .hint{
        margin-top:14px;
        font-size:18px;
        color:#444;
    }

    @media (max-width: 768px){
        .feedback h1{ font-size:48px; }
        .feedback p{ font-size:22px; }
    }
    </style>
    """, unsafe_allow_html=True)


# =======================
# Feedback state
# =======================
def clear_feedback():
    st.session_state["feedback"] = None


def set_feedback(kind: str, title: str, message: str, ttl: float = 2.5):
    """
    kind: ok / try / time  (renk şablonları)
    ttl : kaç saniye görünsün (otomatik kapanır)
    """
    colors = {
        "ok": "#22c55e",    # yeşil
        "try": "#f97316",   # turuncu
        "time": "#ef4444",  # kırmızı
    }
    st.session_state["feedback"] = {
        "title": title,
        "message": message,
        "color": colors.get(kind, "#111111"),
        "shown_at": time.time(),
        "ttl": float(ttl),
    }


def render_feedback():
    """
    Sayfanın en başında çağır:
    apply_ui_css()
    render_feedback()
    """
    fb = st.session_state.get("feedback")
    if not fb:
        return

    # Süre dolduysa otomatik kapat
    if time.time() - fb.get("shown_at", 0) >= fb.get("ttl", 2.5):
        clear_feedback()
        st.rerun()

    # Tam ekran mesaj
    st.markdown(f"""
    <div class="feedback">
      <div class="box">
        <h1 style="color:{fb["color"]};">{fb["title"]}</h1>
        <p>{fb["message"]}</p>
        <div class="hint">(Birazdan devam edecek…)</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # İstersen dokunarak kapatabilsin diye altta buton da bırakıyoruz
    # (Overlay yüzünden bazen tıklanmaz; ama otomatik kapanma zaten garanti)
    st.write("")
    if st.button("➡️ Devam", use_container_width=True):
        clear_feedback()
        st.rerun()
