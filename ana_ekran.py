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
def kutlam
