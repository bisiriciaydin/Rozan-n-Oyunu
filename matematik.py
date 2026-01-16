import streamlit as st
import random
import time

from tema import tema_uygula
from veritabani import verileri_getir, puan_artir, puan_dusur, puanlari_sifirla

SOUND_OK = "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"
SOUND_FAIL = "https://www.soundjay.com/misc/sounds/fail-trumpet-01.mp3"


def carpma_oyunu():
    tema_uygula("mavi")

    if st.button("🔙 Ana Menüye Dön"):
        st.session_state.sayfa = "ana_ekran"
        for k in ["s1", "s2", "dogru", "secenekler", "m_zaman"]:
            st.session_state.pop(k, None)
        st.rerun()

    puanlar = verileri_getir()

    st.subheader("🎯 Hedef: 100 Puan")
    st.progress(min(1.0, puanlar["matematik_dogru"] / 100))
    st.caption(f"{puanlar['matematik_dogru']} / 100 puan")

    if puanlar["matematik_dogru"] >= 100:
        st.balloons()
        st.success("🏆 MATEMATİK ŞAMPİYONU OLDUN!")
        st.audio(SOUND_OK, autoplay=True)
        if st.button("✨ YENİ OYUN ✨"):
            puanlari_sifirla("matematik")
            st.rerun()
        return

    if "m_zaman" not in st.session_state:
        st.session_state.m_zaman = time.time()

    kalan = max(0, int(20 - (time.time() - st.session_state.m_zaman)))
    st.progress(kalan / 20)
    st.write(f"⏱️ Kalan: {kalan}")

    if kalan <= 0:
        puan_dusur("matematik")
        st.audio(SOUND_FAIL, autoplay=True)
        st.info("⏰ Süre doldu… Yeni soruya geçiyoruz! 🌟")
        time.sleep(1.3)
        for k in ["s1", "s2", "dogru", "secenekler", "m_zaman"]:
            st.session_state.pop(k, None)
        st.rerun()

    if "s1" not in st.session_state:
        st.session_state.s1 = random.randint(2, 9)
        st.session_state.s2 = random.randint(2, 9)
        st.session_state.dogru = st.session_state.s1 * st.session_state.s2

        yanlislar = random.sample(
            [x for x in range(4, 82) if x != st.session_state.dogru], 3
        )
        st.session_state.secenekler = yanlislar + [st.session_state.dogru]
        random.shuffle(st.session_state.secenekler)

    st.header(f"{st.session_state.s1} x {st.session_state.s2} = ?")

    cols = st.columns(4)
    secilen = None
    for i, deger in enumerate(st.session_state.secenekler):
        if cols[i].button(str(deger), key=f"m_{i}", use_container_width=True):
            secilen = deger

    if secilen is not None:
        if secilen == st.session_state.dogru:
            puan_artir("matematik")
            st.audio(SOUND_OK, autoplay=True)
            st.success("✅ Süper! Doğru cevap! 🎉")
            st.balloons()
        else:
            puan_dusur("matematik")
            st.audio(SOUND_FAIL, autoplay=True)
            st.info("🙂 Sorun değil, birlikte öğreniyoruz!")

        time.sleep(1.3)
        for k in ["s1", "s2", "dogru", "secenekler", "m_zaman"]:
            st.session_state.pop(k, None)
        st.rerun()

    time.sleep(0.5)
    st.rerun()
