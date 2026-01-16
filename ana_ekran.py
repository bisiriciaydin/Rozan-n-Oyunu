# ana_ekran.py
import streamlit as st

from veritabani import verileri_getir, tum_verileri_temizle
from matematik import carpma_oyunu
from ingilizce import ingilizce_oyunu
from turkce import zit_anlam_oyunu
from ui import apply_ui_css, render_feedback

def buyuk_basari_kontrol(puanlar):
    """
    Üç oyunda da 100 puana ulaşınca ana ekranda 1 kere kutlama videosu gösterir.
    """
    if "buyuk_kutlama_yapildi" not in st.session_state:
        st.session_state.buyuk_kutlama_yapildi = False

    tumu_bitti = (
        puanlar.get("matematik_dogru", 0) >= 100
        and puanlar.get("ingilizce_dogru", 0) >= 100
        and puanlar.get("turkce_dogru", 0) >= 100
    )

    if tumu_bitti and not st.session_state.buyuk_kutlama_yapildi:
        st.session_state.buyuk_kutlama_yapildi = True

        st.balloons()
        st.snow()

        st.markdown("## 🏆 MUHTEŞEMSİN! 🏆")
        st.markdown("### 🎉 TÜM OYUNLARI TAMAMLADIN! 🎉")

        st.video(
            "https://cdn.pixabay.com/vimeo/458212215/confetti-41932.mp4",
            autoplay=True,
            loop=True,
        )

        st.audio(
            "https://www.soundjay.com/human/sounds/applause-01.mp3",
            autoplay=True,
        )

        st.success("🌟 Sen bir **SÜPER ÖĞRENCİSİN**! 🌟")
        st.stop()  # kutlama gösterilirken aşağısı çizilmesin



def tema_secici():
    if "tema" not in st.session_state:
        st.session_state.tema = "pembe"

    secim = st.radio(
        "🎨 Tema Seç",
        ["🌸 Pembe Yıldız", "🌊 Mavi Dalga", "🌿 Yeşil Nokta"],
        horizontal=True,
    )

    if secim == "🌸 Pembe Yıldız":
        st.session_state.tema = "pembe"
    elif secim == "🌊 Mavi Dalga":
        st.session_state.tema = "mavi"
    else:
        st.session_state.tema = "yesil"


def _stil():
    tema = st.session_state.get("tema", "pembe")

    if tema == "pembe":
        arka_plan = """
        background:
          radial-gradient(circle at 10% 20%, rgba(255, 182, 213, 0.55) 10%, transparent 11%),
          radial-gradient(circle at 80% 30%, rgba(255, 182, 213, 0.45) 10%, transparent 11%),
          radial-gradient(circle at 50% 80%, rgba(255, 182, 213, 0.35) 10%, transparent 11%),
          linear-gradient(135deg, #fff0f6, #ffe6f2);
        """
        hero_bg = "linear-gradient(90deg, #ff7aa2 0%, #ffb6d5 55%, #ffd6e8 100%)"
    elif tema == "mavi":
        arka_plan = """
        background:
          repeating-linear-gradient(
            45deg,
            rgba(190, 215, 255, 0.45),
            rgba(190, 215, 255, 0.45) 10px,
            rgba(220, 235, 255, 0.65) 10px,
            rgba(220, 235, 255, 0.65) 20px
          ),
          linear-gradient(135deg, #eaf4ff, #f6fbff);
        """
        hero_bg = "linear-gradient(90deg, #7aa7ff 0%, #9cc5ff 55%, #d6ecff 100%)"
    else:  # yesil
        arka_plan = """
        background:
          radial-gradient(circle, rgba(170, 255, 210, 0.45) 20%, transparent 21%) 0 0 / 42px 42px,
          linear-gradient(135deg, #f2fff7, #eafff0);
        """
        hero_bg = "linear-gradient(90deg, #47d18c 0%, #7affc4 55%, #dfffee 100%)"

    st.markdown(
        f"""
        <style>
        .stApp {{
            {arka_plan}
        }}

        .hero {{
            padding: 16px 18px;
            border-radius: 18px;
            background: {hero_bg};
            color: #ffffff;
            box-shadow: 0 10px 24px rgba(0,0,0,0.10);
            margin-bottom: 12px;
        }}
        .hero h1 {{ margin: 0; font-size: 34px; line-height: 1.05; }}
        .hero p  {{ margin: 6px 0 0 0; font-size: 16px; opacity: .95; }}

        .panel {{
            border-radius: 18px;
            padding: 14px;
            background: rgba(255,255,255,0.75);
            border: 1px solid rgba(255,255,255,0.85);
            box-shadow: 0 10px 22px rgba(0,0,0,0.06);
        }}

        .card {{
            border-radius: 18px;
            padding: 14px 14px 12px 14px;
            box-shadow: 0 10px 24px rgba(0,0,0,0.08);
            border: 1px solid rgba(255,255,255,0.7);
            margin-bottom: 10px;
            background: rgba(255,255,255,0.88);
        }}
        .card-title {{
            display:flex;
            align-items:center;
            gap:10px;
            font-size: 22px;
            font-weight: 900;
            margin-bottom: 6px;
        }}
        .card-desc {{
            font-size: 14px;
            opacity: .85;
            margin-bottom: 10px;
        }}
        .chip {{
            display:inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 800;
            background: rgba(255,255,255,0.6);
        }}

        .stButton>button {{
            border-radius: 14px !important;
            padding: 0.7rem 0.9rem !important;
            font-weight: 900 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def ana_menu():
    apply_ui_css()
    render_feedback()


    tema_secici()
    _stil()

    puanlar = verileri_getir()
    buyuk_basari_kontrol(puanlar)

    st.markdown(
        """
        <div class="hero">
            <h1>Canım Kızım Roza ❤️</h1>
            <p>Bugün hangi oyunu oynamak istersin? 🎮✨</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    colA, colB = st.columns([3, 1])
    with colA:
        st.markdown(
            f"""
            <div class="panel">
                <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap;">
                    <span class="chip">🏆 Toplam Puan: {puanlar["toplam_puan"]}</span>
                    <span class="chip">🧮 Matematik: {puanlar["matematik_dogru"]//10} doğru</span>
                    <span class="chip">🇬🇧 İngilizce: {puanlar["ingilizce_dogru"]//10} doğru</span>
                    <span class="chip">📚 Türkçe: {puanlar["turkce_dogru"]//10} doğru</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with colB:
        if st.button("🗑️ Sıfırla", use_container_width=True):
            tum_verileri_temizle()
            st.rerun()

    st.write("")
    st.subheader("🌟 Oyun Kartları")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="card" style="background: linear-gradient(135deg, rgba(255,241,168,0.95) 0%, rgba(255,209,242,0.95) 100%);">
                <div class="card-title">🧮 Matematik</div>
                <div class="card-desc">Çarpma sorularıyla hızlanalım!</div>
                <span class="chip">⚡ 20 saniye</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("✖️ Çarpma Oyununa Başla", use_container_width=True):
            st.session_state.sayfa = "matematik"
            st.rerun()

    with c2:
        st.markdown(
            """
            <div class="card" style="background: linear-gradient(135deg, rgba(200,255,241,0.95) 0%, rgba(200,215,255,0.95) 100%);">
                <div class="card-title">🇬🇧 İngilizce</div>
                <div class="card-desc">Kelimeleri emojilerle öğrenelim!</div>
                <span class="chip">🎯 100 puan hedef</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("🇬🇧 İngilizce Oyununa Başla", use_container_width=True):
            st.session_state.sayfa = "ingilizce"
            st.rerun()

    with c3:
        st.markdown(
            """
            <div class="card" style="background: linear-gradient(135deg, rgba(231,255,184,0.95) 0%, rgba(184,255,247,0.95) 100%);">
                <div class="card-title">📚 Türkçe</div>
                <div class="card-desc">Zıt anlamları bul, yıldızları topla!</div>
                <span class="chip">🌈 Eğlenceli</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("↔️ Zıt Anlam Oyununa Başla", use_container_width=True):
            st.session_state.sayfa = "turkce"
            st.rerun()

    st.write("")
    st.subheader("📊 Başarı Tablon")
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.success(f"🧮 Matematik: ✅ {puanlar['matematik_dogru']//10} Doğru | ❌ {puanlar['matematik_yanlis']} Yanlış")
    st.info(f"🇬🇧 İngilizce: ✅ {puanlar['ingilizce_dogru']//10} Doğru | ❌ {puanlar['ingilizce_yanlis']} Yanlış")
    st.info(f"📚 Türkçe: ✅ {puanlar['turkce_dogru']//10} Doğru | ❌ {puanlar['turkce_yanlis']} Yanlış")
    st.warning(f"🏆 Toplam Puanın: {puanlar['toplam_puan']}")

    st.markdown("</div>", unsafe_allow_html=True)


# ---- Sayfa Yönetimi ----
if "sayfa" not in st.session_state:
    st.session_state.sayfa = "ana_ekran"

if st.session_state.sayfa == "ana_ekran":
    ana_menu()
elif st.session_state.sayfa == "matematik":
    carpma_oyunu()
elif st.session_state.sayfa == "ingilizce":
    ingilizce_oyunu()
elif st.session_state.sayfa == "turkce":
    zit_anlam_oyunu()
else:
    st.session_state.sayfa = "ana_ekran"
    st.rerun()
