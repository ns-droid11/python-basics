# Ortalama hesaplama fonksiyonu
def ortalama_hesapla(vize, final):
    """
    Verilen vize ve final notlarına göre ortalama hesaplar.
    :param vize: Vize notu
    :param final: Final notu
    :return: Hesaplanan ortalama
    """
    return (vize * 0.4) + (final * 0.6)

# Not durumu fonksiyonu
def not_durumu(vize, final):
    """
    Verilen vize ve final notlarına göre not durumunu döndürür.
    :param vize: Vize notu
    :param final: Final notu
    :return: Not durumu ("Geçti", "Şartlı Geçti", "Kaldı")
    """
    ortalama = ortalama_hesapla(vize, final)
    if ortalama >= 60:
        return "Geçti"
    elif ortalama >= 50:
        return "Şartlı Geçti"
    else:
        return "Kaldı"
        
if __name__ == "__main__":
 # Test: Not ortalaması hesaplama ve durum belirleme
    vize_notu = 70
    final_notu = 80
    ortalama = ortalama_hesapla(vize_notu, final_notu)
    durum = not_durumu(vize_notu, final_notu)
    print(f"Vize: {vize_notu}, Final: {final_notu}, Ortalama: {ortalama}, Durum: {durum}")