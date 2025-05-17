# indirimli_fiyat Fonksiyonu
def indirimli_fiyat(*urunler, **musteri_bilgisi):
    toplam = 0
    for urun in urunler:
        print(f"Ürün: {urun[0]} Fiyat: {urun[1]:.2f} TL")
        toplam += urun[1]

    print("-" * 27)
    print(f"Toplam tutar: {toplam:.2f} TL\n")

    indirim_orani = musteri_bilgisi.get("indirim_orani", 0)

    if indirim_orani > 0:
        indirim_tutari = toplam * (indirim_orani / 100)
        toplam -= indirim_tutari
        print(f"İndirim (%{indirim_orani}): -{indirim_tutari:.2f} TL")

    return toplam

if __name__ == "__main__":
        # indirimli_fiyat Fonksiyonu Testi
    sonuc = indirimli_fiyat(
        ("Ekmek", 10),
        ("Süt", 20),
        indirim_orani=10
    )
    print(f"İndirimli Toplam: {sonuc:.2f} TL")