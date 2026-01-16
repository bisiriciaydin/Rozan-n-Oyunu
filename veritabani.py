# veritabani.py
import json
from pathlib import Path

DOSYA_YOLU = Path(__file__).resolve().parent / "roza_puanlari.json"

DEFAULT_VERI = {
    "matematik_dogru": 0,   # puan gibi (10'ar artar)
    "matematik_yanlis": 0,  # adet
    "ingilizce_dogru": 0,
    "ingilizce_yanlis": 0,
    "turkce_dogru": 0,
    "turkce_yanlis": 0,
    "toplam_puan": 0
}

def _dosya_yoksa_olustur():
    if not DOSYA_YOLU.exists():
        DOSYA_YOLU.write_text(
            json.dumps(DEFAULT_VERI, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

def verileri_getir() -> dict:
    _dosya_yoksa_olustur()
    try:
        veri = json.loads(DOSYA_YOLU.read_text(encoding="utf-8"))
    except Exception:
        veri = DEFAULT_VERI.copy()
        DOSYA_YOLU.write_text(json.dumps(veri, ensure_ascii=False, indent=2), encoding="utf-8")

    # Eksik alan varsa tamamla
    for k, v in DEFAULT_VERI.items():
        if k not in veri:
            veri[k] = v
    return veri

def verileri_kaydet(veri: dict) -> None:
    for k, v in DEFAULT_VERI.items():
        if k not in veri:
            veri[k] = v
    DOSYA_YOLU.write_text(json.dumps(veri, ensure_ascii=False, indent=2), encoding="utf-8")

def _alanlar(ders: str):
    """
    ders: 'matematik' | 'ingilizce' | 'turkce'
    """
    dogru = f"{ders}_dogru"
    yanlis = f"{ders}_yanlis"
    return dogru, yanlis

def puan_artir(ders: str, miktar: int = 10) -> None:
    veri = verileri_getir()
    dogru_alan, _ = _alanlar(ders)

    veri[dogru_alan] = int(veri.get(dogru_alan, 0)) + miktar
    veri["toplam_puan"] = int(veri.get("toplam_puan", 0)) + miktar

    verileri_kaydet(veri)

def puan_dusur(ders: str, miktar: int = 10) -> None:
    """
    Motive kırmamak için:
    - Puan 0'ın altına düşmez
    - Yanlış sayısı +1 artar
    """
    veri = verileri_getir()
    dogru_alan, yanlis_alan = _alanlar(ders)

    mevcut = int(veri.get(dogru_alan, 0))
    dusus = min(miktar, mevcut)  # 0 altına düşmesin
    veri[dogru_alan] = mevcut - dusus

    veri[yanlis_alan] = int(veri.get(yanlis_alan, 0)) + 1

    toplam = int(veri.get("toplam_puan", 0))
    veri["toplam_puan"] = max(0, toplam - dusus)

    verileri_kaydet(veri)

def puanlari_sifirla(ders: str) -> None:
    veri = verileri_getir()
    dogru_alan, yanlis_alan = _alanlar(ders)

    # toplam puanı da düzgün azaltalım:
    veri["toplam_puan"] = max(0, int(veri.get("toplam_puan", 0)) - int(veri.get(dogru_alan, 0)))

    veri[dogru_alan] = 0
    veri[yanlis_alan] = 0
    verileri_kaydet(veri)

def tum_verileri_temizle() -> None:
    verileri_kaydet(DEFAULT_VERI.copy())
