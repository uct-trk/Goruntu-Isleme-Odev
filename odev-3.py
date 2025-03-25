import cv2
import numpy as np
import matplotlib.pyplot as plt

# Gri resmi oku
grey_image = cv2.imread('gri_resim.jpg')

# Parlaklık değeri (0-255 arası bir değer)
brightness_value = 50

# Parlaklığı artır ve değerleri 0-255 arasında tut
brightened_image = np.clip(grey_image + brightness_value, 0, 255).astype(np.uint8)

# Görüntüleri yan yana göster
plt.figure(figsize=(10,5))

# Orijinal gri görüntü
plt.subplot(1, 2, 1)
plt.imshow(grey_image, cmap='gray')
plt.title('Orijinal Gri Görüntü')
plt.axis('off') # Eksenleri kapatır

# Parlaklığı artırılmış görüntü
plt.subplot(1, 2, 2)
plt.imshow(brightened_image, cmap='gray')
plt.title(f'Parlaklığı +{brightness_value} Artırılmış Görüntü')
plt.axis('off') # Eksenleri kapatır

plt.tight_layout() # Subplot'lar (yan yana gösterilen resimler) arasındaki boşlukları otomatik ayarlar
plt.show()

# Parlaklığı artırılmış görüntüyü kaydet
cv2.imwrite('parlak_gri_resim.jpg', brightened_image)

# Parlaklık artırmanın görüntü üzerindeki etkisi# Örnek piksel değişimleri:

# 1 Piksel Değerindeki Değişim
# Yeni değer = Orijinal değer + Parlaklık değeri
# Orijinal -> Yeni değer
#   50    ->   100   (50 + 50)
#  150    ->   200   (150 + 50)
#  220    ->   255   (220 + 50 = 270, ama 255'te sınırlandı)
#   10    ->    60   (10 + 50)

# 2. Görsel Etki:

# Gri tonlamalı resimde (0-255 arası):
# - 0: Tam siyah (0)
# - 128: Gri (ortanca)
# - 255: Tam beyaz (255)

# Parlaklık artırma:

#  Koyu gri tonları daha açık gri olur

#  Açık gri tonları beyaza yaklaşır

#  Çok açık bölgeler beyazda doygunluğa ulaşır

# 3. Potansiyel Sorunlar:

# Detay kaybı oluşabilir
# Çok açık bölgelerde ayrıntılar kaybolabilir
# Kontrastın azalması görüntü kalitesini düşürebilir

# 4. Kullanım Amaçları:
# Düşük ışıklı görüntüleri iyileştirme
# Görüntüdeki detayları daha görünür hale getirme
# Görüntü ön işleme adımı olarak kullanılabilir

# 5. Avantaj ve Dezavantajları:

# Avantajlar:
# Basit ve hızlı bir işlem
# Düşük ışıklı bölgeleri görünür hale getirir
# Kolay uygulanabilir

# Dezavantajlar:
# Aşırı parlaklık detay kaybına neden olur
# Kontrast azalabilir
# Doğal görünümü bozabilir