import streamlit as st

from ui import apply_ui_css, render_feedback
from veritabani import verileri_getir, tum_verileri_temizle
from tema import tema_secici

import matematik
import ingilizce
import turkce
# ---- SAYFA DURUMU ----
if "sayfa" not in st.session_state:
    st.session_state.sayfa = "menu"

def sayfaya_git(hedef):
    st.session_state.sayfa = hedef
    st.rerun()

def menu_ekrani():
    tema_secici()
    apply_ui_css()
    render_feedback()

    puanlar = verileri_getir()

    st.markdown("""
    <div class="hero">
        <h1>Canım Kızım Roza 💖</h1>
        <p>Bugün hangi oyunu oynamak istersin 🎮✨</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    🏆 Toplam Puan: **{puanlar["toplam_puan"]}**
    🧮 Matematik: {puanlar["matematik_dogru"]}/10
    📘 İngilizce: {puanlar["ingilizce_dogru"]}/10
    📗 Türkçe: {puanlar["turkce_dogru"]}/10
    """)

    # ⬇⬇⬇ İŞTE BU KISIM (GİRİNTİ ŞART)
    st.markdown("### 🎮 Oyunlar")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button(
            "🧮 Matematik",
            use_container_width=True,
            on_click=lambda: sayfaya_git("matematik")
        )

    with col2:
        st.button(
            "📘 Türkçe",
            use_container_width=True,
            on_click=lambda: sayfaya_git("turkce")
        )

    with col3:
        st.button(
            "🌍 İngilizce",
            use_container_width=True,
            on_click=lambda: sayfaya_git("ingilizce")
        )


def app_router():
    if "page" not in st.session_state:
        st.session_state.page = "menu"

    if st.session_state.page == "menu":
        menu_ekrani()
    elif st.session_state.page == "matematik":
        matematik.carpma_oyunu()
    elif st.session_state.page == "ingilizce":
        ingilizce.ingilizce_oyunu()
    elif st.session_state.page == "turkce":
        turkce.turkce_oyunu()
    else:
        st.session_state.page = "menu"
        st.rerun()


app_router()
