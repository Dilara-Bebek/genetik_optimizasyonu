import numpy as np
import matplotlib.pyplot as plt

# Gerekli fonksiyonları diğer dosyadan çekiyoruz
from genetik_operators import (
    uygunluk_hesapla,
    rank_temelli_secim,
    tek_noktali_caprazlama,
    mutasyon_uygula,
    X1_BOUNDS, X2_BOUNDS
)

#Rastgele popülasyon üreten fonksiyon
def populasyon_olustur(pop_buyuklugu):
    yeni_pop = [] #boş liste

    # Popülasyon büyüklüğü kadar birey üret
    for _ in range(pop_buyuklugu):
        x1 = np.random.randint(X1_BOUNDS[0], X1_BOUNDS[1] + 1) #CPU değeri seç
        x2 = np.random.randint(X2_BOUNDS[0], X2_BOUNDS[1] + 1) #RAM değeri seç
        yeni_pop.append(np.array([x1, x2])) #Listeye ekle
    return np.array(yeni_pop)

#Genetik algoritmanın ana fonksiyonu
def evrimsel_algoritma_calistir(pop_buyuklugu, nesil_sayisi, mutasyon_ihtimali, mutasyon_buyuklugu):

    # Popülasyon üretimi
    populasyon = populasyon_olustur(pop_buyuklugu)

    en_iyiler = [] #Her neslin en iyilerini tutar
    elit_birey = None # Şuanki en iyi birey
    elit_uygunluk = -999999  # Başlangıçta çok düşük bir skor veriyorum ki ilk gelen bunu geçsin

    print(f"Genetik Algoritma çalışmaya başladı. Popülasyon Büyüklüğü: {pop_buyuklugu}, Nesil Sayısı: {nesil_sayisi}\n")


    for nesil in range(nesil_sayisi):
      #Şuanki popülasyondaki her bireyin fitness değeri hesaplanır
        uygunluklar = np.array([uygunluk_hesapla(b) for b in populasyon])

        # Elitizm : En iyi birey seçilir
        en_iyi_indeks = np.argmax(uygunluklar)
        mevcut_en_iyi_skor = uygunluklar[en_iyi_indeks]

        #eğer önceki bireylerden daha iyi birey bulunduysa güncelle
        if mevcut_en_iyi_skor > elit_uygunluk:
            elit_uygunluk = mevcut_en_iyi_skor
            elit_birey = populasyon[en_iyi_indeks].copy()
      # grafikte göstermek için en iyi sonuclar bir listede biriktirilir
        en_iyiler.append(elit_uygunluk)
       #her 10 nesilde bir değerleri ekrana yazalım
        if (nesil + 1) % 10 == 0:
            print(f"Nesil {nesil+1}: En İyi Skor = {elit_uygunluk:.4f} -  Birey = {elit_birey}")

        # Yeni Nesil oluştur
        yeni_populasyon = []
        yeni_populasyon.append(elit_birey) # elit bireyi koru

         # Popülasyon dolana kadar yeni bireyler üret
        while len(yeni_populasyon) < pop_buyuklugu:
            secilenler = rank_temelli_secim(populasyon, uygunluklar, adet=2) #Rank temelli seçimle 2 ebeveyn seç
            c1, c2 = tek_noktali_caprazlama(secilenler[0], secilenler[1]) #Tek noktalı çaprazlama ile 2 birey oluştur
            c1 = mutasyon_uygula(c1, mutasyon_ihtimali, mutasyon_buyuklugu)#Birey1 'e mutasyon uygula
            c2 = mutasyon_uygula(c2, mutasyon_ihtimali, mutasyon_buyuklugu)#Birey2'e mutasyon uygula
            yeni_populasyon.extend([c1, c2]) # Yeni bireyleri popülasyona ekle

        populasyon = np.array(yeni_populasyon[:pop_buyuklugu]) #Yeni nesli şuanki popülasyon yap

# SONUCLAR
    print("\n" + "-"*30)
    print("SONUÇLAR")
    print("-" * 30)
    print(f"Önerilen CPU : {elit_birey[0]}")
    print(f"Önerilen RAM : {elit_birey[1]}")
    print(f"En iyi skor  : {elit_uygunluk:.4f}")
    print("-" * 30 + "\n")

    return populasyon, en_iyiler
