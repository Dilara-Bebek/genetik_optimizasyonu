# Genetik Algoritma ile Web Sunucusu Optimizasyonu (Senaryo 8)

Bu projede, genetik algoritma kullanılarak bir yazılım şirketinin web sunucusu için en uygun CPU ve RAM değerleri belirlenmektedir.
Amaç, verilen kısıtlar altında en yüksek performans skorunu sağlayan donanım değerlerini bulmaktır.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

## AMAÇ FONKSİYONU
Fonksiyon:  y = 5x₁ + 7x₂ - 0.1x₁² - 0.2x₂²

- 'x₁': CPU Çekirdek Sayısı
- 'x₂': RAM Miktarı (GB)
- 'y': Performans Skoru

--------------------------------------------------------------------------------------------------------------------------------------------------------------

## DEĞİŞKENLER VE SINIRLAR
Genetik algoritmanın arama yapacağı gen aralıkları:

- CPU Çekirdek Sayısı (x₁): [2, 12] arası tam sayılar.
- RAM Miktarı (x₂): [4, 64] GB arası tam sayılar.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

## KISITLAR
Algoritmanın çözüm üretirken uyması gereken kurallar :

1. Sınır: x₁ * x₂ ≤ 512
2. Sınır: x₁ ≥ 4

Ceza Yöntemi: Herhangi bir kısıt ihlali durumunda, ilgili bireyin uygunluk değerinden 10.000 puan düşürülmektedir.
Ceza katsayısı yüksek seçilmiştir. Bunun nedeni, kısıtları ihlal eden çözümlerin algoritma tarafından tercih edilmemesini sağlamaktır.
--------------------------------------------------------------------------------------------------------------------------------------------------------------

## DOSYA YAPISI

| Dosya Adı                     | Açıklama                                                                                                        |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `genetik_optimizasyonu.ipynb` | Projenin Ana Dosyasısır. Google Colab üzerinde çalıştırılabilir, tüm kodları ve anlatımı içeren not defteridir. |
| `genetik_operators.py`        | Amaç fonksiyonu, kısıtlar ve seçim, çaprazlama, mutasyon gibi işlemlerin tanımlandığı dosyadır.                 |
| `evrim_motoru.py`             | Genetik algoritmanın ana çalışma döngüsünün kurulduğu ve nesillerin oluşturulduğu dosyadır.                     |
| `main.py`                     | Algoritmanın çalıştırıldığı, parametrelerin belirlendiği ve sonuç grafiğinin çizildiği ana dosyadır.            |
| `README.md`                   | Projenin amacı, yöntemi ve kullanım adımlarının açıklandığı dokümantasyon dosyasıdır.                           |
| 'sonuc_grafigi.png'           | Algoritma çalıştırıldığında elde edilen performans artış grafiğidir.                                            |


--------------------------------------------------------------------------------------------------------------------------------------------------------------

## KULLANIM
1. Tüm '.py' dosyaları aynı klasörde bulunmalıdır.
2. 'main.py' dosyasını '%run main.py' komutuyla çalıştırılır.
3. Genetik algoritma çıktısı olarak:
   - Algoritmanın önerdiği en uygun CPU ve RAM değerleri
   - Bu değerlere karşılık gelen en iyi skor
   - Nesiller ilerledikçe skorun değişimini gösteren grafik
--------------------------------------------------------------------------------------------------------------------------------------------------------------

## Genetik Operatörler Açıklamaları ('genetik_operators.py')
Bu dosya, genetik algoritmanın temel mantığını oluşturan kısımları içerir.

1. 'tahmin_y(birey)'
Verilen bireyin CPU, RAM değerlerini kullanarak amaç fonksiyonuna göre performansını hesaplar.

2. 'kisit_kontrol(birey)'
Bireyin x₁ * x₂ ≤ 512 ve x₁ ≥ 4 kısıtlarına uyup uymadığını kontrol eder.
Her ihlal için 1 ceza puanı olacak şekilde ihlal sayısını döndürür.

3. 'uygunluk_hesapla(birey)'
Performans skorundan, varsa ceza puanlarını düşerek bireyin Fitness değerini hesaplar.

4. 'rank_temelli_secim(populasyon, uygunluklar, adet=2)'
Bireyleri uygunluk değerlerine göre rank ile sıralar.
Daha iyi bireylerin seçilme olasılığını artırarak belirlenen sayıda ebeveyn seçer.

5. 'tek_noktali_caprazlama(p1, p2)'
İki ebeveynin genlerini (CPU ve RAM) tek bir noktadan değiştirerek iki yeni birey üretir.

6. 'mutasyon_uygula(birey, ihtimal, buyukluk)'
Gen çeşitliliğini sağlamak için belirli bir ihtimalle CPU veya RAM değerlerini değiştirir.
'np.clip' kullanılarak gen değerlerinin sınırların dışına çıkması engellenir.
--------------------------------------------------------------------------------------------------------------------------------------------------------------

## Evrimsel Algoritma Açıklamaları ('evrim_motoru.py')
Bu dosya, genetik algoritmanın ana döngüsünü çalıştırır ve popülasyonun nesiller boyunca nasıl evrildiğini yönetir.

Algoritma Adımları:
- Her nesilde bireylerin uygunluk değerleri hesaplanır.
- En iyi birey korunarak bir sonraki nesle aktarılır. (elitizm)
- Seçim (rank temelli), çaprazlama (tek noktalı) ve mutasyon işlemleri uygulanır.
- Elde edilen en iyi skorlar kaydedilir ve grafik üzerinde gösterilir.

Parametreler :
'pop_buyuklugu': Popülasyondaki birey sayısı (20)
'nesil_sayisi':toplam döngü sayısı (50)
'mutasyon_ihtimali': Her bir genin rastgele değişime uğrama olasılığı (0.05)
'mutasyon_buyuklugu': Mutasyon gerçekleştiğinde gen değerinin ne kadar değişeceği (1)
'secim_turu': 'Rank Temelli Seçim'
'caprazlama_turu': 'Tek Noktalı Çaprazlama'    

## Proje Sonuçları
Algoritma çalıştırıldığında elde edilen performans artış grafiği aşağıdadır. Nesiller ilerledikçe en iyi bireyin fitness değeri artmaktadır.
Genetik Algoritma Sonuç Grafiği -> ('sonuc_grafigi.png')
