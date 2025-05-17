# Sayı tahmin oyunu fonksiyonu
import random

def oyun():
    """
    1 ile 100 arasında rastgele bir sayı tutar.
    Kullanıcıya 10 tahmin hakkı vererek bu sayıyı bulmasını ister.
    Her tahminden sonra kullanıcıya ipuçları verir.
    """
    rastgele_sayi = random.randint(1, 100)
    print("Bilgisayar 1 ile 100 arasında bir sayı tuttu. Tahmin etmeye çalış!")

    tahmin = -1 # Başlangıçta rastgele_sayi'den farklı bir sayı veriyoruz
    deneme_sayisi = 0 # Kullanıcının tahmin sayısını saymak için
    tahmin_hakki = 10 # 10 tahmin hakkı

    while tahmin != rastgele_sayi and deneme_sayisi < tahmin_hakki:
        try:
            print(f"{tahmin_hakki - deneme_sayisi} hakkın kaldı.")
            tahmin = int(input("Tahminin: "))
            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin")
                continue # Geçersiz bir tahmin yapıldığında döngü başa döner
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue # Eğer sayı girilmezse döngü başa döner

        deneme_sayisi += 1

        if tahmin < rastgele_sayi:
            print("Daha büyük bir sayı söyle 🧐")
        elif tahmin > rastgele_sayi:
            print("Daha küçük bir sayı söyle 👀")
        else:
            print("Tebrikler! Doğru tahmin 🎉")
    if tahmin != rastgele_sayi:
        print(f"Maalesef bilemedin! Doğru sayı {rastgele_sayi} idi 😔")

if __name__ == "__main__":
    # Test: Sayı tahmin oyunu
    oyun()        