# matematik.py
import random
import time
import streamlit as st

from ui import apply_ui_css, render_feedback, set_feedback

# Projendeki veritabanı fonksiyonları (varsa bunları kullanır)
try:
    from veritabani import puan_artir, puan_dusur, verileri_getir
except Exception:
    puan_artir = None
    puan_dusur = None
    verileri_getir = None


# -----------------------
# Yardımcılar
# -----------------------
def _yeni_soru_uret():
    s1 = random.randint(2, 9)
    s2 = random.randint(2, 9)
    dogru = s1 * s2

    yanlislar = set()
    while len(yanlislar) < 3:
        aday = random.randint(4, 81)
        if aday != dogru:
            yanlislar.add(aday)

    secenekler = list(yanlislar) + [dogru]
    random.shuffle(secenekler)

    st.session_state.s1 = s1
    st.session_state.s2 = s2
    st.session_state.dogru = dogru
    st.session_state.secenekler = secenekler
    st.session_state.soru_baslangic = time.time()


def _soru_var_mi():
    return all(k in st.session_state for k in ["s1", "s2", "dogru", "secenekler", "soru_baslangic"])


def _soruyu_sifirla():
    for k in ["s1", "s2", "dogru", "secenekler", "soru_baslangic"]:
        st.session_state.pop(k, None)


def _puan_guncelle(dogru_mu: bool):
    # Senin projende bu fonksiyonlar varsa kullanır
    if dogru_mu and callable(puan_artir):
        puan_artir("matematik")
    elif (not dogru_mu) and callable(puan_dusur):
        puan_dusur("matematik")


def _puan_100_kontrol():
    if callable(verileri_getir):
        try:
            puanlar = verileri_getir()
            return int(puanlar.get("toplam_puan", 0)) >= 100
        except Exception:
            return False
    return False


# -----------------------
# Oyun
# -----------------------
def carpma_oyunu():
    apply_ui_css()
    render_feedback()

    st.title("🧮 Çarpma Oyunu")
    st.caption("Doğru seçeneğe tıkla! Hazırsan başlayalım 🌟")

    col_top = st.columns([1, 1, 1])
    with col_top[0]:
        if st.button("🏠 Ana Menü", use_container_width=True):
            st.switch_page("ana_ekran.py")
    with col_top[1]:
        if st.button("🔄 Yeni Soru", use_container_width=True):
            _soruyu_sifirla()
            st.rerun()
    with col_top[2]:
        pass

    st.divider()

    # Soru yoksa üret
    if not _soru_var_mi():
        _yeni_soru_uret()

    # Süre ayarı
    SURE_SANIYE = 10
    gecen = time.time() - st.session_state.soru_baslangic
    kalan = max(0.0, SURE_SANIYE - gecen)

    # Süre göstergesi
    st.progress(int(((SURE_SANIYE - kalan) / SURE_SANIYE) * 100))
    st.markdown(f"⏳ Kalan süre: **{kalan:.1f} saniye**")

    # Süre bitti mi?
    if kalan <= 0:
        _puan_guncelle(False)
        set_feedback("time", "⏰ Süre Bitti", "Ama denediğin için çok iyisin 👏")
        _soruyu_sifirla()
        st.rerun()

    # Soru
    st.markdown(
        f"<h2 style='text-align:center; font-size:42px; margin: 10px 0;'>"
        f"{st.session_state.s1} × {st.session_state.s2} = ?</h2>",
        unsafe_allow_html=True
    )

    st.write("")

    # Seçenekler
    cols = st.columns(2)
    secilen = None

    for i, deger in enumerate(st.session_state.secenekler):
        with cols[i % 2]:
            if st.button(f"{deger}", key=f"opt_{i}", use_container_width=True):
                secilen = deger

    # Seçim yapıldıysa değerlendir
    if secilen is not None:
        if secilen == st.session_state.dogru:
            _puan_guncelle(True)

            # 100 puan olduysa özel kutlama
            if _puan_100_kontrol():
                set_feedback("ok", "🎉 100 PUAN!", "Harikasın! Büyük başarı 🌟")
            else:
                set_feedback("ok", "🎉 TEBRİKLER!", "Harika bir cevap verdin 🌟")

            _soruyu_sifirla()
            st.rerun()
        else:
            _puan_guncelle(False)
            set_feedback("try", "🙂 Olsun!", "Bir dahaki soruda başarabilirsin 💪")
            _soruyu_sifirla()
            st.rerun()

    # Süreyi akıcı güncellemek için küçük yenileme
    time.sleep(0.15)
    st.rerun()


if __name__ == "__main__":
    carpma_oyunu()
