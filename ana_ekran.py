import streamlit as st

from ui import apply_ui_css, render_feedback
from veritabani import verileri_getir, tum_verileri_temizle
from tema import tema_secici

import matematik
import ingilizce
import turkce


def menu_ekrani():
    tema_secici()
    apply_ui_css()
    render_feedback()

    puanlar = verileri_getir()

    st.markdown("""
    <div class="hero">
        <h1>Canım Kızım Roza ❤️</h1>
        <p>Bugün hangi oyunu oynamak istersin? 🎮✨</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    🏆 Toplam Puan: **{puanlar["toplam_puan"]}**  
    🧮 Matematik: {puanlar["matematik_dogru"]}/10  
    🇬🇧 İngilizce: {puanlar["ingilizce_dogru"]}/10  
    📘 Türkçe: {puanlar["turkce_dogru"]}/10  
    """)

    colA, colB = st.columns([3, 1])
    with colB:
        if st.button("🗑️ Sıfırla", use_container_width=True):
            tum_verileri_temizle()
            st.rerun()

    st.write("")
    st.subheader("⭐ Oyunlar")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="game-card">
            <h2>🧮 Matematik</h2>
            <p>Çarpma sorularıyla hızlan!</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Başla", key="go_mat", use_container_width=True):
            st.session_state.page = "matematik"
            st.rerun()

    with c2:
        st.markdown("""
        <div class="game-card">
            <h2>🇬🇧 İngilizce</h2>
            <p>Kelimeleri öğren!</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Başla", key="go_ing", use_container_width=True):
            st.session_state.page = "ingilizce"
            st.rerun()

    with c3:
        st.markdown("""
        <div class="game-card">
            <h2>📘 Türkçe</h2>
            <p>Dil bilgisiyle güçlen!</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Başla", key="go_trk", use_container_width=True):
            st.session_state.page = "turkce"
            st.rerun()


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
