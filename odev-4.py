import cv2
import numpy as np
import matplotlib.pyplot as plt

# Gri resmi oku
grey_image = cv2.imread('gri_resim.jpg')

# Kontrast faktörü (1'den büyük değerler kontrastı artırır)
contrast_factor = 1.5

# 1. Görüntüyü float32'ye dönüştürüyoruz
# float32'ye dönüştürme:
# - Piksel değerlerini float32 formatına dönüştürür
# - Bu sayede daha hassas bir aritmetik işlem yapılabilir
# - Örneğin, 0-255 arası değerleri 0-1 arasına normalize edebiliriz
# - Bu sayede daha doğru bir kontrast ayarı yapılabilir
contrasted_image = grey_image.astype(np.float32)

# 2. Kontrastı artırıyoruz
contrasted_image = contrasted_image * contrast_factor

# 3. Değerleri 0-255 arasında sınırla ve uint8'e dönüştürüyoruz
contrasted_image = np.clip(contrasted_image, 0, 255).astype(np.uint8)

# Görüntüleri yan yana gösteriyoruz
plt.figure(figsize=(10,5))

# Orijinal gri görüntü
plt.subplot(1, 2, 1)
plt.imshow(grey_image, cmap='gray')
plt.title('Orijinal Gri Görüntü')
plt.axis('off')

# Kontrastı artırılmış görüntü
plt.subplot(1, 2, 2)
plt.imshow(contrasted_image, cmap='gray')
plt.title(f'Kontrastı {contrast_factor}x Artırılmış Görüntü')
plt.axis('off')

plt.tight_layout()
plt.show()

# Kontrastı artırılmış görüntüyü kaydediyoruz
cv2.imwrite('kontrast_gri_resim.jpg', contrasted_image)

# Kontrast artırma işleminin görüntü üzerindeki etkilerini açıklayınız.

# Kontrast artırma işleminin görüntü üzerindeki etkilerini detaylı olarak açıklayalım:

# 1. Piksel Değerlerindeki Değişim:
# Örnek (contrast_factor = 1.5):
# Orijinal -> Yeni değer
#   50    ->    75    (50 × 1.5)
#  100    ->   150    (100 × 1.5)
#  200    ->   255    (200 × 1.5 = 300, ama 255'te sınırlandı)
#   10    ->    15    (10 × 1.5)

# 2. Görsel Etki:

# Gri tonlamalı resimde (0-255 arası):
# - Koyu pikseller daha koyu olur
# - Açık pikseller daha açık olur
# - Orta tonlar daha belirgin hale gelir

# 3. Kontrast Artırmanın Sonuçları:

# - Açık ve koyu bölgeler arasındaki fark artar
# - Kenarlar ve detaylar daha belirgin hale gelir
# - Görüntüdeki nesneler daha net ayırt edilebilir

# 4. Potansiyel Sorunlar:

# - Çok açık bölgelerde beyazda doygunluk (255'te kırpılma)
# - Çok koyu bölgelerde siyahta doygunluk (0'da kırpılma)
# - Aşırı kontrast detay kaybına neden olabilir

# 5. Kullanım Amaçları:
# - Düşük kontrastlı görüntüleri iyileştirme
# - Görüntüdeki detayları belirginleştirme
# - Nesne tespitini kolaylaştırma

# 6. Matematiksel İşlem:
# - Her piksel değeri contrast_factor ile çarpılır
# - Sonuçlar 0-255 aralığında sınırlandırılır
# - Doğrusal bir dönüşümdür

# 7. Avantaj ve Dezavantajları:

# Avantajlar:
# - Görüntüdeki detaylar daha belirgin hale gelir
# - Nesneler arası ayrım netleşir
# - Görüntü daha canlı görünür

# Dezavantajlar:
# - Aşırı kontrast detay kaybına neden olabilir
# - Çok açık ve çok koyu bölgelerde bilgi kaybı
# - Doğal görünüm bozulabilir

# 8. Kullanım Alanları:

# - Görüntü ön işleme
# - Görüntü sıkıştırma
