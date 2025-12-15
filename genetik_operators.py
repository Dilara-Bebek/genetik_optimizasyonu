import numpy as np
import random
# Genetik ALgoritmada kullanacağımız kurallar ve fonksiyonların yazılması

# Değişken Sınırları
X1_BOUNDS = [2, 12]  # CPU çekirdeği sayısı
X2_BOUNDS = [4, 64]  # RAM miktarı (GB)

#parametre olarak giren bireyin performansını hesaplayan fonksiyon
def tahmin_y(birey):
    """
    Amaç Fonksiyonu: Her Bireyin performansını hesaplar.
    Amaç Fonksiyonu: y = 5x1 + 7x2 - 0.1x1^2 - 0.2x2^2
    """
    x1 = birey[0] #1. gen ->cpu
    x2 = birey[1] #2. gen ->ram
    y = (5 * x1) + (7 * x2) - (0.1 * x1**2) - (0.2 * x2**2)
    return y

# parametre olarak giren bireyin ceza puanını hesaplayan fonksiyon
def kisit_kontrol(birey):
    """
    Kısıtları kontrol eder.
    İhlal varsa ceza puanı döndürür.
    """
    ceza_puani = 0
    x1 = birey[0]
    x2 = birey[1]

    # Kısıt 1: CPU sayısı 4'ten az olamaz
    if x1 < 4:
        ceza_puani += 1

    # Kısıt 2: CPU * RAM 512'yi geçemez
    if (x1 * x2) > 512:
        ceza_puani += 1

    return ceza_puani

# Fitness Fonksiyonu
def uygunluk_hesapla(birey):
    """
    Bireyin uygunluk değerini hesaplar.
    Cezalandırma Yöntemi: Performans - (ihlal_sayisi * CEZA_KATSAYISI)
    """
    # Ham performans
    y_performans = tahmin_y(birey)

    # Kısıtların sayısı
    ihlal_sayisi = kisit_kontrol(birey)

    # Ceza Katsayısı
    CEZA_KATSAYISI = 10000

    uygunluk = y_performans - (ihlal_sayisi * CEZA_KATSAYISI)

    return uygunluk

# Seçim fonksiyonu
def rank_temelli_secim(populasyon, uygunluklar, adet=2):
    """
    Rank Temelli Seçim:
    Bireylerin uygunluk değerlerini yüksekten düşüğe sıralar,
    her bireyin olasılığı hesaplanır
    """
    #popülasyondaki birey sayısı
    N = len(populasyon)

    #Uygunluk değerlerini büyükten küçüğe sırala
    sirali_indeksler = np.argsort(-uygunluklar)

    #Rank formülü
    payda = N * (N + 1) / 2
    secim_ihtimalleri = np.array([(N - i) / payda for i in range(N)])

    # 3. İhtimalleri Doğru İndekslere Eşle
    ihtimaller = np.zeros_like(secim_ihtimalleri)
    for i, idx in enumerate(sirali_indeksler):
        ihtimaller[idx] = secim_ihtimalleri[i]

    # 4. Seçimi Yap
    # Rulet mantığı gibi ama negatif sayılardan etkilenmeyen versiyonu.
    secilen_indeksler = np.random.choice(N, size=adet, p=ihtimaller)

    return populasyon[secilen_indeksler]

#Çaprazlama
def tek_noktali_caprazlama(p1, p2):
    #Çocuk 1 = Ebeveyn1'in CPU'su + Ebeveyn2'in RAM'i
    c1 = np.array([p1[0], p2[1]])
    # Çocuk 2 = Ebeveyn2'in CPU'su + Ebeveyn1'in RAM'i
    c2 = np.array([p2[0], p1[1]])
    return c1, c2

#Mutasyon fonksiyonu
def mutasyon_uygula(birey, ihtimal, buyukluk):
  # ihtimal = 0.05 , buyukluk = 1 parametre değerleri
  #orjinal bireyi bozmamak için kopyası yapılır
    yeni = birey.copy()

    # CPU geni mutasyonu
    if np.random.rand() < ihtimal:
        degisim = np.random.randint(-int(buyukluk), int(buyukluk) + 1) #değişim miktarı
        yeni[0] += degisim
        yeni[0] = np.clip(yeni[0], X1_BOUNDS[0], X1_BOUNDS[1]) # Sınır dışına çıkmasın diye

    # RAM geni mutasyonu
    if np.random.rand() < ihtimal:
        degisim = np.random.randint(-int(buyukluk), int(buyukluk) + 1) #değişim miktarı
        yeni[1] += degisim
        yeni[1] = np.clip(yeni[1], X2_BOUNDS[0], X2_BOUNDS[1]) # Sınır dışına çıkmasın diye

    return yeni # mutasyon uygulanmış yeni birey

print("Fonksiyonlar tanımlandı.")
