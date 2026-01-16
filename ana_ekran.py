import streamlit as st
from veritabani import verileri_getir, tum_verileri_temizle
from tema import tema_secici

# =======================
# GLOBAL CSS
# =======================
def apply_css():
    st.markdown("""
    <style>
    body {
        font-weight: 600;
        color: #111;
    }

    .hero {
        background: linear-gradient(135deg, #fbcfe8, #fef3c7);
        padding: 24px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 20px;
    }

    .game-card {
        background: white;
        border-radius: 18px;
        padding: 20px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 10px;
    }

    .game-card h2 {
        font-size: 26px;
        margin-bottom: 8px;
    }

    .game-card p {
        font-size: 18px;
    }

    button {
        font-size: 20px !important;
        font-weight: 700 !important;
        padding: 14px !important;
        border-radius: 14px !important;
    }

    /* BÜYÜK GERİ BİLDİRİM */
    .feedback {
        position: fixed;
        inset: 0;
        background: rgba(255,255,255,0.96);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
        text-align: center;
    }

    .feedback h1 {
        font-size: 64px;
        margin-bottom: 16px;
    }

    .feedback p {
        font-size: 28px;
    }
    </style>
    """, unsafe_allow_html=True)


# =======================
# ANA MENÜ
# =======================
def ana_menu():
    tema_secici()
    apply_css()

    puanlar = verileri_getir()

    # HERO
    st.markdown("""
    <div class="hero">
        <h1>Canım Kızım Roza ❤️</h1>
        <p>Bugün hangi oyunu oynamak istersin? 🎮✨</p>
    </div>
    """, unsafe_allow_html=True)

    # PUAN PANELİ
    st.markdown(f"""
    🏆 Toplam Puan: **{puanlar["toplam_puan"]}**  
    🧮 Matematik: {puanlar["matematik_dogru"]}/10  
    🇬🇧 İngilizce: {puanlar["ingilizce_dogru"]}/10  
    📘 Türkçe: {puanlar["turkce_dogru"]}/10  
    """)

    if st.button("🗑️ Puanları Sıfırla"):
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

        if st.button("Başla", key="mat"):
            st.switch_page("matematik.py")

    with c2:
        st.markdown("""
        <div class="game-card">
            <h2>🇬🇧 İngilizce</h2>
            <p>Kelimeleri öğren!</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Başla", key="ing"):
            st.switch_page("ingilizce.py")

    with c3:
        st.markdown("""
        <div class="game-card">
            <h2>📘 Türkçe</h2>
            <p>Dil bilgisiyle güçlen!</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Başla", key="trk"):
            st.switch_page("turkce.py")


if __name__ == "__main__":
    ana_menu()
