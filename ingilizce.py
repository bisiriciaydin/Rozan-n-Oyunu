import streamlit as st
import random
import time

from tema import tema_uygula
from veritabani import verileri_getir, puan_artir, puan_dusur, puanlari_sifirla

SOUND_OK = "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"
SOUND_FAIL = "https://www.soundjay.com/misc/sounds/fail-trumpet-01.mp3"


SOZLUK = {
    "hello": "merhaba",
    "hi": "selam",
    "good morning": "günaydın",
    "good night": "iyi geceler",
    "goodbye": "hoşça kal",
    "yes": "evet",
    "no": "hayır",
    "please": "lütfen",
    "thank you": "teşekkür ederim",
    "sorry": "özür dilerim",

    "one": "bir",
    "two": "iki",
    "three": "üç",
    "four": "dört",
    "five": "beş",
    "six": "altı",
    "seven": "yedi",
    "eight": "sekiz",
    "nine": "dokuz",
    "ten": "on",

    "red": "kırmızı",
    "blue": "mavi",
    "yellow": "sarı",
    "green": "yeşil",
    "black": "siyah",
    "white": "beyaz",
    "orange_color": "turuncu",
    "pink": "pembe",
    "purple": "mor",
    "brown": "kahverengi",

    "cat": "kedi",
    "dog": "köpek",
    "bird": "kuş",
    "fish": "balık",
    "lion": "aslan",
    "monkey": "maymun",
    "rabbit": "tavşan",
    "duck": "ördek",
    "bee": "arı",
    "elephant": "fil",

    "apple": "elma",
    "banana": "muz",
    "milk": "süt",
    "water": "su",
    "bread": "ekmek",
    "egg": "yumurta",
    "cheese": "peynir",
    "cake": "pasta",
    "orange_fruit": "portakal",
    "ice cream": "dondurma",

    "school": "okul",
    "teacher": "öğretmen",
    "student": "öğrenci",
    "book": "kitap",
    "pencil": "kalem",
    "eraser": "silgi",
    "bag": "çanta",
    "notebook": "defter",
    "chair": "sandalye",
    "table": "masa",

    "mother": "anne",
    "father": "baba",
    "brother": "erkek kardeş",
    "sister": "kız kardeş",
    "baby": "bebek",
    "grandmother": "büyükanne",
    "grandfather": "büyükbaba",
    "family": "aile",
    "friend": "arkadaş",
    "child": "çocuk",

    "eye": "göz",
    "ear": "kulak",
    "nose": "burun",
    "mouth": "ağız",
    "hand": "el",
    "foot": "ayak",
    "hair": "saç",
    "face": "yüz",
    "arm": "kol",
    "leg": "bacak",

    "house": "ev",
    "room": "oda",
    "door": "kapı",
    "window": "pencere",
    "bed": "yatak",
    "tv": "televizyon",
    "kitchen": "mutfak",
    "garden": "bahçe",
    "key": "anahtar",
    "lamp": "lamba",

    "sun": "güneş",
    "moon": "ay",
    "star": "yıldız",
    "sky": "gökyüzü",
    "tree": "ağaç",
    "flower": "çiçek",
    "rain": "yağmur",
    "snow": "kar",
    "sea": "deniz",
    "mountain": "dağ",

    "big": "büyük",
    "small": "küçük",
    "happy": "mutlu",
    "sad": "üzgün",
    "hot": "sıcak",
    "cold": "soğuk",
    "go": "gitmek",
    "come": "gelmek",
    "eat": "yemek yemek",
    "drink": "içmek",
}

EMOJI = {
    "hello": "👋", "hi": "👋", "good morning": "🌅", "good night": "🌙", "goodbye": "👋",
    "yes": "✅", "no": "❌", "please": "🙏", "thank you": "💐", "sorry": "🫶",

    "one": "1️⃣", "two": "2️⃣", "three": "3️⃣", "four": "4️⃣", "five": "5️⃣",
    "six": "6️⃣", "seven": "7️⃣", "eight": "8️⃣", "nine": "9️⃣", "ten": "🔟",

    "red": "🟥", "blue": "🟦", "yellow": "🟨", "green": "🟩", "black": "⬛", "white": "⬜",
    "orange_color": "🟧", "pink": "🩷", "purple": "🟪", "brown": "🟫",

    "cat": "🐱", "dog": "🐶", "bird": "🐦", "fish": "🐟", "lion": "🦁", "monkey": "🐒",
    "rabbit": "🐰", "duck": "🦆", "bee": "🐝", "elephant": "🐘",

    "apple": "🍎", "banana": "🍌", "milk": "🥛", "water": "💧", "bread": "🍞", "egg": "🥚",
    "cheese": "🧀", "cake": "🍰", "orange_fruit": "🍊", "ice cream": "🍦",

    "school": "🏫", "teacher": "👩‍🏫", "student": "🧒", "book": "📚", "pencil": "✏️",
    "eraser": "🧽", "bag": "🎒", "notebook": "📓", "chair": "🪑", "table": "🧾",

    "mother": "👩", "father": "👨", "brother": "👦", "sister": "👧", "baby": "👶",
    "family": "👨‍👩‍👧‍👦", "friend": "🤝", "child": "🧒",

    "sun": "☀️", "moon": "🌙", "star": "⭐", "tree": "🌳", "flower": "🌸",
    "rain": "🌧️", "snow": "❄️", "sea": "🌊", "mountain": "⛰️",

    "house": "🏠", "door": "🚪", "window": "🪟", "bed": "🛏️", "tv": "📺",
    "kitchen": "🍳", "garden": "🌿", "key": "🔑", "lamp": "💡",

    "big": "🐘", "small": "🐭", "happy": "😊", "sad": "😢", "hot": "🔥", "cold": "❄️",
    "go": "➡️", "come": "⬅️", "eat": "🍽️", "drink": "🥤",
}


def _kelime_sec():
    if "i_pool" not in st.session_state or not st.session_state.i_pool:
        havuz = list(SOZLUK.items())
        random.shuffle(havuz)
        st.session_state.i_pool = havuz
    return st.session_state.i_pool.pop()


def ingilizce_oyunu():
    tema_uygula("pembe")

    if st.button("🔙 Ana Menüye Dön"):
        st.session_state.sayfa = "ana_ekran"
        for k in ["i_k", "i_d", "i_s", "i_zaman"]:
            st.session_state.pop(k, None)
        st.rerun()

    puanlar = verileri_getir()

    st.subheader("🎯 Hedef: 100 Puan")
    st.progress(min(1.0, puanlar["ingilizce_dogru"] / 100))
    st.caption(f"{puanlar['ingilizce_dogru']} / 100 puan")

    if puanlar["ingilizce_dogru"] >= 100:
        st.balloons()
        st.success("🇬🇧 TEBRİKLER! İNGİLİZCE ŞAMPİYONU OLDUN!")
        st.audio(SOUND_OK, autoplay=True)
        if st.button("✨ YENİ OYUN ✨"):
            puanlari_sifirla("ingilizce")
            st.session_state.pop("i_pool", None)
            st.rerun()
        return

    if "i_zaman" not in st.session_state:
        st.session_state.i_zaman = time.time()

    kalan = max(0, int(20 - (time.time() - st.session_state.i_zaman)))
    st.progress(kalan / 20)
    st.write(f"⏱️ Kalan Süre: {kalan}")

    if kalan <= 0:
        puan_dusur("ingilizce")
        st.audio(SOUND_FAIL, autoplay=True)
        st.info("⏰ Süre doldu… Yeni soruya geçelim! 🌟")
        time.sleep(1.3)
        for k in ["i_k", "i_d", "i_s", "i_zaman"]:
            st.session_state.pop(k, None)
        st.rerun()

    if "i_k" not in st.session_state:
        k, d = _kelime_sec()
        yanlislar = random.sample([v for v in SOZLUK.values() if v != d], 3)
        secenekler = yanlislar + [d]
        random.shuffle(secenekler)
        st.session_state.i_k, st.session_state.i_d, st.session_state.i_s = k, d, secenekler

    emoji = EMOJI.get(st.session_state.i_k, "⭐")
    st.markdown(f"<div style='font-size:84px; text-align:center'>{emoji}</div>", unsafe_allow_html=True)

    gorunen = st.session_state.i_k.replace("_color", "").replace("_fruit", "")
    st.header(f'"{gorunen.upper()}" ne demek?')

    cols = st.columns(2)
    secilen = None
    for i, cevap in enumerate(st.session_state.i_s):
        if cols[i % 2].button(cevap, key=f"i_{i}", use_container_width=True):
            secilen = cevap

    if secilen is not None:
        if secilen == st.session_state.i_d:
            puan_artir("ingilizce")
            st.audio(SOUND_OK, autoplay=True)
            st.success("✅ Süper! Doğru cevap! 🎉")
            st.balloons()
        else:
            puan_dusur("ingilizce")
            st.audio(SOUND_FAIL, autoplay=True)
            st.info("🙂 Sorun değil, birlikte öğreniyoruz!")

        time.sleep(1.3)
        for k in ["i_k", "i_d", "i_s", "i_zaman"]:
            st.session_state.pop(k, None)
        st.rerun()

    time.sleep(0.5)
    st.rerun()
