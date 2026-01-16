# tema.py
import streamlit as st

THEMES = {
    "pembe": {
        "bg": """
        background:
          radial-gradient(circle at 10% 20%, rgba(255, 182, 213, 0.55) 10%, transparent 11%),
          radial-gradient(circle at 80% 30%, rgba(255, 182, 213, 0.45) 10%, transparent 11%),
          radial-gradient(circle at 50% 80%, rgba(255, 182, 213, 0.35) 10%, transparent 11%),
          linear-gradient(135deg, #fff0f6, #ffe6f2);
        """,
        "hero": "linear-gradient(90deg, #ff7aa2 0%, #ffb6d5 55%, #ffd6e8 100%)",
    },
    "mavi": {
        "bg": """
        background:
          repeating-linear-gradient(
            45deg,
            rgba(190, 215, 255, 0.45),
            rgba(190, 215, 255, 0.45) 10px,
            rgba(220, 235, 255, 0.65) 10px,
            rgba(220, 235, 255, 0.65) 20px
          ),
          linear-gradient(135deg, #eaf4ff, #f6fbff);
        """,
        "hero": "linear-gradient(90deg, #7aa7ff 0%, #9cc5ff 55%, #d6ecff 100%)",
    },
    "yesil": {
        "bg": """
        background:
          radial-gradient(circle, rgba(170, 255, 210, 0.45) 20%, transparent 21%) 0 0 / 42px 42px,
          linear-gradient(135deg, #f2fff7, #eafff0);
        """,
        "hero": "linear-gradient(90deg, #47d18c 0%, #7affc4 55%, #dfffee 100%)",
    },
}

def tema_uygula(tema: str):
    """İstenilen temayı tüm sayfaya uygular."""
    t = THEMES.get(tema, THEMES["pembe"])

    st.markdown(
        f"""
        <style>
        .stApp {{
            {t["bg"]}
        }}

        .hero {{
            padding: 16px 18px;
            border-radius: 18px;
            background: {t["hero"]};
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
