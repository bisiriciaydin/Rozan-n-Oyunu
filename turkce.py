# turkce.py
import streamlit as st
import random
import time

from tema import tema_uygula
from veritabani import verileri_getir, puan_artir, puan_dusur, puanlari_sifirla

SOUND_OK = "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"
SOUND_FAIL = "https://www.soundjay.com/misc/sounds/fail-trumpet-01.mp3"


ZIT_ANLAM = {
    # 1. Boyut ve Fiziksel Özellikler
    "Büyük": "Küçük",
    "Uzun": "Kısa",
    "Şişman": "Zayıf",
    "Geniş": "Dar",
    "Ağır": "Hafif",
    "Sert": "Yumuşak",
    "Hızlı": "Yavaş",
    "Yeni": "Eski",
    "Genç": "Yaşlı",
    "Kalın": "İnce",

    # 2. Durum ve Görünüş
    "İyi": "Kötü",
    "Güzel": "Çirkin",
    "Temiz": "Kirli",
    "Islak": "Kuru",
    "Açık": "Kapalı",
    "Dolu": "Boş",
    "Zengin": "Fakir",
    "Kolay": "Zor",
    "Doğru": "Yanlış",
    "Parlak": "Mat",

    # 3. Duygular ve Kişilik
    "Mutlu": "Üzgün",
    "Cesur": "Korkak",
    "Çalışkan": "Tembel",
    "Akıllı": "Akılsız",
    "Nazik": "Kaba",
    "Cömert": "Cimri",
    "Sakin": "Heyecanlı",
    "Dost": "Düşman",
    "Gülmek": "Ağlamak",
    "Sevinç": "Keder",

    # 4. Yer ve Yön Bilgisi
    "Aşağı": "Yukarı",
    "İç": "Dış",
    "Ön": "Arka",
    "Sağ": "Sol",
    "Alt": "Üst",
    "Uzak": "Yakın",
    "Giriş": "Çıkış",
    "İleri": "Geri",
    "Derin": "Sığ",
    "Tavan": "Taban",

    # 5. Zaman ve Diğer Kavramlar
    "Gündüz": "Gece",
    "Sabah": "Akşam",
    "Önce": "Sonra",
    "Erken": "Geç",
    "İlk": "Son",
    "Sıcak": "Soğuk",
    "Tatlı": "Acı",
    "Evet": "Hayır",
    "Varlı": "Yok",
    "Taze": "Bayat",
}

EMOJI = {
    # Fiziksel
    "Büyük": "🐘", "Küçük": "🐭",
    "Uzun": "📏", "Kısa": "✂️",
    "Şişman": "🍔", "Zayıf": "🥗",
    "Geniş": "↔️", "Dar": "↕️",
    "Ağır": "🏋️", "Hafif": "🪶",
    "Sert": "🪨", "Yumuşak": "🧸",
    "Hızlı": "⚡", "Yavaş": "🐢",
    "Yeni": "🆕", "Eski": "🕰️",
    "Genç": "🧒", "Yaşlı": "👵",
    "Kalın": "📚", "İnce": "📄",

    # Durum/görünüş
    "İyi": "👍", "Kötü": "👎",
    "Güzel": "🌸", "Çirkin": "🫥",
    "Temiz": "🧼", "Kirli": "🪣",
    "Islak": "💦", "Kuru": "🏜️",
    "Açık": "🔓", "Kapalı": "🔒",
    "Dolu": "🫙", "Boş": "🫗",
    "Zengin": "💰", "Fakir": "🪙",
    "Kolay": "😌", "Zor": "😵‍💫",
    "Doğru": "✅", "Yanlış": "❌",
    "Parlak": "✨", "Mat": "🌫️",

    # Duygu/kişilik
    "Mutlu": "😊", "Üzgün": "😢",
    "Cesur": "🦁", "Korkak": "😟",
    "Çalışkan": "💪", "Tembel": "🛋️",
    "Akıllı": "🧠", "Akılsız": "🤪",
    "Nazik": "🤝", "Kaba": "🙄",
    "Cömert": "🎁", "Cimri": "🪙",
    "Sakin": "🧘", "Heyecanlı": "🤩",
    "Dost": "🫶", "Düşman": "⚔️",
    "Gülmek": "😂", "Ağlamak": "😭",
    "Sevinç": "🎉", "Keder": "🌧️",

    # Yer/yön
    "Aşağı": "⬇️", "Yukarı": "⬆️",
    "İç": "📦", "Dış": "🌳",
    "Ön": "➡️", "Arka": "⬅️",
    "Sağ": "➡️", "Sol": "⬅️",
    "Alt": "⬇️", "Üst": "⬆️",
    "Uzak": "🛰️", "Yakın": "📍",
    "Giriş": "🚪➡️", "Çıkış": "⬅️🚪",
    "İleri": "⏩", "Geri": "⏪",
    "Derin": "🕳️", "Sığ": "🏖️",
    "Tavan": "🏠⬆️", "Taban": "⬇️🏠",

    # Zaman/diğer
    "Gündüz": "☀️", "Gece": "🌙",
    "Sabah": "🌅", "Akşam": "🌇",
    "Önce": "⏮️", "Sonra": "⏭️",
    "Erken": "⏰", "Geç": "🕘",
    "İlk": "🥇", "Son": "🏁",
    "Sıcak": "🔥", "Soğuk": "❄️",
    "Tatlı": "🍯", "Acı": "🌶️",
    "Evet": "✅", "Hayır": "❌",
    "Varlı": "✅", "Yok": "🚫",
    "Taze": "🥬", "Bayat": "🥖",
}


def _zit_sec():
    """Torba sistemi: bitene kadar tekrar etmez."""
    if "t_pool" not in st.session_state or not st.session_state.t_pool:
        havuz = list(ZIT_ANLAM.items())
        random.shuffle(havuz)
        st.session_state.t_pool = havuz
    return st.session_state.t_pool.pop()


def zit_anlam_oyunu():
    tema_uygula("yesil")

    if st.button("🔙 Ana Menüye Dön"):
        st.session_state.sayfa = "ana_ekran"
        for k in ["t_k", "t_d", "t_s", "t_zaman"]:
            st.session_state.pop(k, None)
        st.rerun()

    puanlar = verileri_getir()

    st.subheader("🎯 Hedef: 100 Puan")
    st.progress(min(1.0, puanlar["turkce_dogru"] / 100))
    st.caption(f"{puanlar['turkce_dogru']} / 100 puan")

    if puanlar["turkce_dogru"] >= 100:
        st.balloons()
        st.success("📚 TEBRİKLER! TÜRKÇE ŞAMPİYONU OLDUN! 🎉")
        st.audio(SOUND_OK, autoplay=True)
        if st.button("✨ YENİ OYUN ✨"):
            puanlari_sifirla("turkce")
            st.session_state.pop("t_pool", None)
            st.rerun()
        return

    # ⏱️ Sayaç
    if "t_zaman" not in st.session_state:
        st.session_state.t_zaman = time.time()

    kalan = max(0, int(20 - (time.time() - st.session_state.t_zaman)))
    st.progress(kalan / 20)
    st.write(f"⏱️ Kalan Süre: {kalan}")

    if kalan <= 0:
        puan_dusur("turkce")
        st.audio(SOUND_FAIL, autoplay=True)
        st.info("⏰ Süre doldu… Yeni soruya geçelim! 🌟")
        time.sleep(1.3)
        for k in ["t_k", "t_d", "t_s", "t_zaman"]:
            st.session_state.pop(k, None)
        st.rerun()

    # ❓ Soru oluştur
    if "t_k" not in st.session_state:
        k, d = _zit_sec()
        yanlislar = random.sample([v for v in ZIT_ANLAM.values() if v != d], 3)
        secenekler = yanlislar + [d]
        random.shuffle(secenekler)
        st.session_state.t_k, st.session_state.t_d, st.session_state.t_s = k, d, secenekler

    emoji = EMOJI.get(st.session_state.t_k, "⭐")
    st.markdown(f"<div style='font-size:84px; text-align:center'>{emoji}</div>", unsafe_allow_html=True)

    st.header(f'"{st.session_state.t_k}" zıt anlamlısı nedir?')

    cols = st.columns(2)
    secilen = None
    for i, cevap in enumerate(st.session_state.t_s):
        if cols[i % 2].button(cevap, key=f"t_{i}", use_container_width=True):
            secilen = cevap

    if secilen is not None:
        if secilen == st.session_state.t_d:
            puan_artir("turkce")
            st.audio(SOUND_OK, autoplay=True)
            st.success("✅ Harika! Doğru cevap! 🎉")
            st.balloons()
        else:
            puan_dusur("turkce")
            st.audio(SOUND_FAIL, autoplay=True)
            st.info("🙂 Sorun değil, birlikte öğreniyoruz!")

        time.sleep(1.3)
        for k in ["t_k", "t_d", "t_s", "t_zaman"]:
            st.session_state.pop(k, None)
        st.rerun()

    # Süre aksın diye otomatik yenile
    time.sleep(0.5)
    st.rerun()
