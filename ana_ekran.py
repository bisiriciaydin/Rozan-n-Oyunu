import streamlit as st

from ui import apply_ui_css, render_feedback
from veritabani import verileri_getir, tum_verileri_temizle
from tema import tema_secici

import matematik
import ingilizce
import turkce


# -----------------------------
# Mobil (iPhone) odaklı ayarlar
# -----------------------------
st.set_page_config(
    page_title="Roza'nın Oyunu",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def mobil_css():
    """iPhone için tek sütun, büyük butonlar, okunabilir yazı."""
    st.markdown(
        """
        <style>
        /* Sayfayı daralt, iPhone gibi görün */
        .block-container{
            max-width: 520px;
            padding-top: 0.75rem;
            padding-bottom: 2.5rem;
        }

        /* Başlıklar */
        h1, h2, h3 { letter-spacing: -0.2px; }

        /* Büyük butonlar (dokunmatik) */
        div.stButton > button {
            width: 100%;
            min-height: 52px;
            border-radius: 16px;
            font-size: 18px;
            font-weight: 700;
        }

        /* Kart görünümü */
        .roza-card{
            background: rgba(255,255,255,0.9);
            border: 1px solid rgba(0,0,0,0.06);
            border-radius: 18px;
            padding: 14px 14px;
            box-shadow: 0 8px 22px rgba(0,0,0,0.06);
            margin-bottom: 12px;
        }

        .roza-hero{
            border-radius: 18px;
            padding: 14px 14px;
            background: linear-gradient(135deg, rgba(255,77,166,0.12), rgba(59,130,246,0.10));
            border: 1px solid rgba(0,0,0,0.05);
            margin-bottom: 12px;
        }

        .roza-small{
            opacity: 0.8;
            font-size: 14px;
        }

        /* Sidebar daraltma (mobilde daha iyi) */
        section[data-testid="stSidebar"] { width: 280px !important; }
        </style>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Sayfa yönetimi (tek kaynak)
# -----------------------------
def init_state():
    if "page" not in st.session_state:
        st.session_state.page = "menu"


def sayfaya_git(hedef: str):
    st.session_state.page = hedef
    st.rerun()


# -----------------------------
# Kutlama (100 puan)
# -----------------------------
def kutlama_ekrani(puanlar: dict):
    st.balloons()
    st.markdown(
        f"""
        <div class="roza-card">
            <h1>🎉 Yaşasın Roza!</h1>
            <h3>100 puana ulaştın! ⭐</h3>
            <p class="roza-small">Toplam Puan: <b>{puanlar.get("toplam_puan", 0)}</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.button("🏠 Ana Menüye Dön", use_container_width=True, on_click=lambda: sayfaya_git("menu"))

    st.markdown("### ✨ İstersen yeni bir oyun seçelim!")
    st.button("🧮 Matematik Oyna", use_container_width=True, on_click=lambda: sayfaya_git("matematik"))
    st.button("📘 Türkçe Oyna", use_container_width=True, on_click=lambda: sayfaya_git("turkce"))
    st.button("🌍 İngilizce Oyna", use_container_width=True, on_click=lambda: sayfaya_git("ingilizce"))


# -----------------------------
# Ana Menü (iPhone)
# -----------------------------
def menu_ekrani():
    tema_secici()        # sidebar tema seçimi (istersen kapatırız)
    apply_ui_css()       # senin mevcut UI stilin
    mobil_css()          # iPhone dokunuşu
    render_feedback()

    puanlar = verileri_getir()
    toplam = puanlar.get("toplam_puan", 0)

    st.markdown(
        """
        <div class="roza-hero">
            <h1>Canım Kızım Roza 💖</h1>
            <p class="roza-small">Bugün hangi oyunu oynamak istersin? 🎮✨</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="roza-card">
            <h3>🏆 Puan Tablosu</h3>
            <p>Toplam Puan: <b>{toplam}</b></p>
            <p class="roza-small">
                🧮 Matematik: {puanlar.get("matematik_dogru", 0)}/10 &nbsp; | &nbsp;
                🌍 İngilizce: {puanlar.get("ingilizce_dogru", 0)}/10 &nbsp; | &nbsp;
                📘 Türkçe: {puanlar.get("turkce_dogru", 0)}/10
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 100 puan yakalandıysa kutlama sayfasına geçir
    if toplam >= 100:
        st.session_state.page = "kutlama"
        st.rerun()

    st.markdown("### 🎮 Oyun Seç")
    st.button("🧮 Matematik (Çarpma Oyunu)", use_container_width=True, on_click=lambda: sayfaya_git("matematik"))
    st.button("📘 Türkçe", use_container_width=True, on_click=lambda: sayfaya_git("turkce"))
    st.button("🌍 İngilizce", use_container_width=True, on_click=lambda: sayfaya_git("ingilizce"))

    st.markdown("---")

    # Sıfırlama (mobilde yanlış basılmasın diye uyarı)
    with st.expander("⚙️ Ayarlar"):
        st.caption("Puanları sıfırlamak istersen buradan yapabilirsin.")
        if st.button("🧼 Puanları Sıfırla", use_container_width=True):
            tum_verileri_temizle()
            st.session_state.page = "menu"
            st.rerun()


# -----------------------------
# Router
# -----------------------------
def app_router():
    init_state()

    # Her sayfada mobil görünüm + tema + feedback uygulanabilir
    # (İstersen sadece menüde uygularız)
    try:
        mobil_css()
    except Exception:
        pass

    puanlar = verileri_getir()
    toplam = puanlar.get("toplam_puan", 0)

    # Kutlama eşiği
    if toplam >= 100 and st.session_state.page != "kutlama":
        st.session_state.page = "kutlama"

    if st.session_state.page == "menu":
        menu_ekrani()

    elif st.session_state.page == "kutlama":
        kutlama_ekrani(puanlar)

    elif st.session_state.page == "matematik":
        # Mevcut fonksiyon adını bozmayalım
        matematik.carpma_oyunu()

        # Modül içinde ana menü butonu yoksa, altta güvenli geri dönüş:
        st.button("🏠 Ana Menü", use_container_width=True, on_click=lambda: sayfaya_git("menu"))

    elif st.session_state.page == "turkce":
        turkce.turkce_oyunu()
        st.button("🏠 Ana Menü", use_container_width=True, on_click=lambda: sayfaya_git("menu"))

    elif st.session_state.page == "ingilizce":
        ingilizce.ingilizce_oyunu()
        st.button("🏠 Ana Menü", use_container_width=True, on_click=lambda: sayfaya_git("menu"))

    else:
        st.session_state.page = "menu"
        st.rerun()


app_router()
