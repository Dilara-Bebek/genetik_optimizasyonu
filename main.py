# MAİN
import matplotlib.pyplot as plt
import numpy as np
import random
# Tekrarlanabilir sonuçların sabit değerde çıkması için Seed kullanılır
random.seed(42)
np.random.seed(42)
from evrim_motoru import evrimsel_algoritma_calistir

#Parametreler
POPULASYON_BUYUKLUGU = 20
NESIL_SAYISI = 50
MUTASYON_IHTIMALI = 0.05
MUTASYON_BUYUKLUGU = 1

#Algoritmayı çalıştır
son_populasyon, skor_gecmisi = evrimsel_algoritma_calistir(
    pop_buyuklugu=POPULASYON_BUYUKLUGU,
    nesil_sayisi=NESIL_SAYISI,
    mutasyon_ihtimali=MUTASYON_IHTIMALI,
    mutasyon_buyuklugu=MUTASYON_BUYUKLUGU
)

#Grafik Çizimi
plt.plot(skor_gecmisi, linestyle='-', color='b')
plt.title('Genetik Algoritma İlerlemesi')
plt.xlabel('Nesil')
plt.ylabel('En iyi uygunluk')
plt.grid(True)
plt.show()
