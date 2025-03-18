import cv2
import matplotlib.pyplot as plt

# Resmi okuyoruz
image = cv2.imread('resim.jpg')

#matplotlib için BGR'den RGB'ye çeviriyoruz
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# renkli resimde kanal sayısını göster
print("Renkli resimde kanal sayısı:", image.shape)
# Renkli resimde kanal sayısı: (4492, 6774, 3)  3 kanallı (RGB)

# Gri tonlamalıya çeviriyoruz
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı resmi kaydediyoruz
cv2.imwrite('gri_resim.jpg', gray_image)

# gri resimde kanal sayısını gösteriyoruz
print("Gri resimde kanal sayısı:", gray_image.shape)
# Gri resimde kanal sayısı: (4492, 6774) 1 kanal.

# Yeni bir figür çizim alanı oluşturuyoruz
# figsize=(10,5) ile genişlik=10 inç, yükseklik=5 inç olarak boyut belirlenir
plt.figure(figsize=(10,5))

# subplot(1, 2, 1) parametreleri:
# 1: satır sayısı
# 2: sütun sayısı
# 1: bu plot'un sıra numarası (sol taraftaki resim)
plt.subplot(1, 2, 1)

# renkli resmi göster
plt.imshow(image_rgb)

# renkli resmin başlığını belirliyoruz
plt.title('Renkli Resim')

# eksenlerdeki sayıları ve çizgileri gizliyoruz
plt.axis('off')

# Gri tonlamalı resim
plt.subplot(1, 2, 2)

# gri resmi göster
plt.imshow(gray_image, cmap='gray')

# gri resmin başlığını belirliyoruz
plt.title('Gri Tonlamalı Resim')

# eksenlerdeki sayıları ve çizgileri gizliyoruz
plt.axis('off')

# Resimlerin ve başlıkların birbirine girmesini önlüyoruz
plt.tight_layout()

# Görüntüyü ekranda gösteriyoruz
plt.show()

# Neden Kanal Sayısı Değişir? (Ders notlarından alınmıştır.)
#Görüntüler aslında matrisler olarak temsil edilir. Siyah-beyaz 
#(grayscale) görüntüler tek kanallı matrislerdir; renkli (RGB) görüntüler 
#ise üç kanallı matrislerdir (Kırmızı, Yeşil, Mavi).Örneğin, 200x300 
#piksellik bir grayscale görüntü, numpy dizisi olarak şöyle temsil edilir:
#import numpy as np
#image = np.random.randint(0, 256, (200, 300), dtype=np.uint8)  # 0-255 arasında rastgele 
#pikseller
#print(image.shape)  # (200, 300)
# Renkli bir görüntü (RGB) ise 3 boyutlu bir dizi ile ifade edilir:
#color_image = np.random.randint(0, 256, (200, 300, 3), dtype=np.uint8)
#print(color_image.shape)  # (200, 300, 3)

#--------------------------------

# Kişisel yorum:

# RGB Resimler:
    # 3 kanaldan oluşur: Kırmızı (Red), Yeşil (Green) ve Mavi (Blue).
    # Her piksel, bu üç kanalın birleşimiyle temsil edilir.
    # Örneğin, bir pikselin değeri (R, G, B) şeklindedir (örneğin, (255, 0, 0) tamamen kırmızıyı temsil eder).

#Gri Tonlamalı Resimler:
    # 1 kanaldan oluşur: Parlaklık (Intensity).
    # Her piksel, yalnızca bir parlaklık değeriyle temsil edilir (0: siyah, 255: beyaz).
    # Örneğin, bir pikselin değeri 128 gibi tek bir sayıdır (orta griyi temsil eder).

# Kanal Sayısının Değişme Nedeni
    # RGB resimde her piksel 3 değerle (R, G, B) temsil edilirken, gri tonlamalı resimde her piksel yalnızca 1 değerle (parlaklık) temsil edilir.
    # Bu nedenle, gri tonlamalı resimde kanal sayısı 3'ten 1'e düşer.

# Bellek ve İşlem Optimizasyonu:
    # Gri tonlamalı resimler, RGB resimlere göre 3 kat daha az bellek kullanır.
    # Bu, özellikle büyük veri setleri üzerinde çalışırken performans avantajı sağlar.





