# Python Temel Fonksiyonlar ve Testler

# Listeyi pozitif yapma fonksiyonu
def pozitif_yap(liste):
    duzenlenmis_liste = []
    for sayi in liste:
        if sayi < 0:
            duzenlenmis_liste.append(-sayi)
        else:
            duzenlenmis_liste.append(sayi)
    return duzenlenmis_liste

# Liste ortalaması için fonksiyon
def liste_ortalama_hesapla(liste):
    toplam = sum(liste)
    eleman_sayisi = len(liste)
    return toplam / eleman_sayisi

# En büyük ve en küçük sayıyı bulma fonksiyonu
def en_buyuk_ve_en_kucuk(liste):
    en_buyuk = max(liste)
    en_kucuk = min(liste)
    return en_buyuk, en_kucuk

# Pozitif ve negatif sayı adedini sayma fonksiyonu
def pozitif_ve_negatif_sayilari_say(liste):
    pozitif_sayac = 0
    negatif_sayac = 0
    for sayi in liste:
        if sayi >= 0:
            pozitif_sayac += 1
        else:
            negatif_sayac += 1
    return pozitif_sayac, negatif_sayac

# 0'dan 9'a kadar olan sayıların karelerini yazdıran fonksiyon
def kareleri_yazdir():
    for sayi in range(10):
        print(f"{sayi}^2 = {sayi * sayi}")

# 1'den 100'e kadar olan sayıların toplamını hesaplayan fonksiyon
def yuz_toplamini_bul():
    toplam = 0
    sayi = 1
    while sayi <= 100:
        toplam += sayi
        sayi += 1
    return toplam

# 1'den 100'e kadar çift sayıları yazdıran fonksiyon
def cift_sayilari_yazdir():
    for sayi in range(2, 101, 2):
        print(sayi)

if __name__ == "__main__":
    # Test: Pozitif yap fonksiyonu
    liste = [-5, 3, -2, 4, -1]
    print("Pozitif yap:", pozitif_yap(liste))

    # Test: Liste ortalaması hesaplama fonksiyonu
    print("Ortalama:", liste_ortalama_hesapla(liste))

    # Test: En büyük ve en küçük sayıyı bulma fonksiyonu
    en_buyuk, en_kucuk = en_buyuk_ve_en_kucuk(liste)
    print(f"En büyük: {en_buyuk}, En küçük: {en_kucuk}")

    # Test: Pozitif ve negatif sayı adedini sayma fonksiyonu
    pozitif_sayac, negatif_sayac = pozitif_ve_negatif_sayilari_say(liste)
    print(f"Pozitif sayılar: {pozitif_sayac}, Negatif sayılar: {negatif_sayac}")

    # Test: Kareleri yazdırma fonksiyonu
    print("Kareler:")
    kareleri_yazdir()

    # Test: 1'den 100'e kadar toplamı bulma fonksiyonu
    print("1'den 100'e kadar toplam:", yuz_toplamini_bul())

    # Test: 1'den 100'e kadar çift sayıları yazdırma fonksiyonu
    print("Çift sayılar:")
    cift_sayilari_yazdir()