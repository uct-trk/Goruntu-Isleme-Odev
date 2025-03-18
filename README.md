# Görüntü İşleme Dersi - Ödev 1

# 1. Görüntü Okuma ve Görüntüleme:

Bu proje, OpenCV kütüphanesi kullanılarak basit bir görüntü okuma ve gösterme uygulamasını içerir.

## Özellikler

- Resim dosyasını okuma
- Resmi ekranda gösterme
- Görüntü boyutlarını ve veri tipini gösterme

## Örnek Çıktı

![Örnek Resim](resim.jpg)

Programın çalıştırılması sonucu:
- Görüntü boyutu: (yükseklik, genişlik, kanal)
- Veri tipi: uint8

## Gereksinimler

Projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekir:

1. OpenCV

```bash
pip install opencv-python
```

2. Matplotlib

```bash
pip install matplotlib
```

## Kullanım

1. Resim dosyanızı proje klasörüne koyun
2. Kodu çalıştırın:

```bash
python odev-1.py
```
3. Resim penceresi açılacaktır
4. Kapatmak için herhangi bir tuşa basın

## Kod Açıklaması

- `cv2.imread()`: Resim dosyasını okur
- `cv2.imshow()`: Resmi bir pencerede gösterir
- `image.shape`: Görüntünün boyutlarını verir (yükseklik, genişlik, kanal sayısı)
- `image.dtype`: Görüntü verilerinin tipini gösterir


# 2. Gri Tonlamalı Görüntüye Dönüştürme:

Bu projede renkli resimleri gri tonlamalı resimlere dönüştürüyoruz. Gri tonlamalı görüntünü boyutlarını kontrol edip neden kanal sayısının değiştiğini açıklıyoruz.

## Renkli resim ve gri tonlamalı resim:

### Renkli Resim:
![Renkli Resim](resim.jpg)

### Gri Tonlamalı Resim:
![Gri Tonlamalı Resim](gri_resim.jpg)


## Kod Açıklaması:

-`cv2.cvtColor()`: Gri tonlamalı görüntüye dönüştürür


-`cv2.imwrite()`:  Görüntüyü kaydeder


-`plt.figure(figsize=(10,5))`: Çizim alanının boyutunu belirler. genişlik=10 inç, yükseklik=5 inç


-`plt.subplot(1, 2, 1)`: sıra numarasını belirler. 1: satır sayısı, 2: sütun sayısı, 1: bu plot'un sıra numarası


-`plt.title('BASLIK')`: Başlığı belirler.


-`plt.axis('off')`: Eksenlerdeki sayıları ve çizgileri gizler.


-`plt.tight_layout()`: Resimlerin ve başlıkların birbirine girmesini önlüyoruz.


-`plt.show()`: Resimleri ekranda gösterir.


## Kullanım:

```bash
python odev-2.py
```

## Neden Kanal Sayısı Değişir? (Ders notlarından alınmıştır.)

Görüntüler aslında matrisler olarak temsil edilir. Siyah-beyaz 
(grayscale) görüntüler tek kanallı matrislerdir; renkli (RGB) görüntüler 
ise üç kanallı matrislerdir (Kırmızı, Yeşil, Mavi).Örneğin, 200x300 
piksellik bir grayscale görüntü, numpy dizisi olarak şöyle temsil edilir:

```bash
import numpy as np
image = np.random.randint(0, 256, (200, 300), dtype=np.uint8)  # 0-255 arasında rastgele pikseller
print(image.shape)  # (200, 300)
```

Renkli bir görüntü (RGB) ise 3 boyutlu bir dizi ile ifade edilir:

```bash
color_image = np.random.randint(0, 256, (200, 300, 3), dtype=np.uint8)
print(color_image.shape)  # (200, 300, 3)
```

## Kişisel Yorum (Analiz):

### RGB Resimler:
     3 kanaldan oluşur: Kırmızı (Red), Yeşil (Green) ve Mavi (Blue).
     Her piksel, bu üç kanalın birleşimiyle temsil edilir.
     Örneğin, bir pikselin değeri (R, G, B) şeklindedir (örneğin, (255, 0, 0) tamamen kırmızıyı temsil eder).

### Gri Tonlamalı Resimler:
     1 kanaldan oluşur: Parlaklık (Intensity).
     Her piksel, yalnızca bir parlaklık değeriyle temsil edilir (0: siyah, 255: beyaz).
     Örneğin, bir pikselin değeri 128 gibi tek bir sayıdır (orta griyi temsil eder).

### Kanal Sayısının Değişme Nedeni
     RGB resimde her piksel 3 değerle (R, G, B) temsil edilirken, gri tonlamalı resimde her piksel yalnızca 1 değerle (parlaklık) temsil edilir.
     Bu nedenle, gri tonlamalı resimde kanal sayısı 3'ten 1'e düşer.

### Bellek ve İşlem Optimizasyonu:
     Gri tonlamalı resimler, RGB resimlere göre 3 kat daha az bellek kullanır.
     Bu, özellikle büyük veri setleri üzerinde çalışırken performans avantajı sağlar.

