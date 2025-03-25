import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

# Temiz görüntüyü yükle
image = cv2.imread('gri_resim.jpg', 0)  # Gri tonlamalı olarak yükle
image = cv2.resize(image, (256, 256))  # Boyutu küçült

# Klasörü oluştur (eğer yoksa)
if not os.path.exists('gurultu_ornekleri'):
    os.makedirs('gurultu_ornekleri')

def add_gaussian_noise(image, mean=0, sigma=25):
    """Gauss gürültüsü ekle"""
    gauss = np.random.normal(mean, sigma, image.shape)
    noisy = np.clip(image + gauss, 0, 255)
    return noisy.astype(np.uint8)

def add_salt_pepper_noise(image, prob=0.05):
    """Tuz-biber gürültüsü ekle"""
    output = np.copy(image)
    # Tuz (beyaz)
    salt = np.random.rand(*image.shape) < (prob/2)
    output[salt] = 255
    # Biber (siyah)
    pepper = np.random.rand(*image.shape) < (prob/2)
    output[pepper] = 0
    return output

def add_poisson_noise(image):
    """Poisson gürültüsü ekle"""
    # Görüntüyü [0,1] aralığına normalize et
    norm_image = image.astype(float) / 255.0
    # Poisson gürültüsü ekle
    noisy = np.random.poisson(norm_image * 50) / 50.0
    # [0,255] aralığına geri dönüştür
    return np.clip(noisy * 255, 0, 255).astype(np.uint8)

# Gürültülü görüntüleri oluştur
gaussian_noisy = add_gaussian_noise(image)
sp_noisy = add_salt_pepper_noise(image)
poisson_noisy = add_poisson_noise(image)

# Görselleştirme
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Orijinal')
plt.subplot(2, 2, 2), plt.imshow(gaussian_noisy, cmap='gray'), plt.title('Gauss Gürültüsü')
plt.subplot(2, 2, 3), plt.imshow(sp_noisy, cmap='gray'), plt.title('Tuz-Biber Gürültüsü')
plt.subplot(2, 2, 4), plt.imshow(poisson_noisy, cmap='gray'), plt.title('Poisson Gürültüsü')
plt.tight_layout()
plt.show()

# Görüntüleri kaydet
cv2.imwrite('gurultu_ornekleri/orijinal.jpg', image)
cv2.imwrite('gurultu_ornekleri/gauss_gurultu.jpg', gaussian_noisy)
cv2.imwrite('gurultu_ornekleri/tuz_biber_gurultu.jpg', sp_noisy)
cv2.imwrite('gurultu_ornekleri/poisson_gurultu.jpg', poisson_noisy)

"""
+------------------+---------------------+-----------------------------+-----------------------------+-----------------------------------+
| Gürültü Türü     | Dağılım             | Python Üretme Kodu          | Temel Özellikler             | Uygun Temizleme Yöntemleri        |
+------------------+---------------------+-----------------------------+-----------------------------+-----------------------------------+
| Gauss (Normal)   | Normal Dağılım      | np.random.normal(mean, sigma)| - Tüm pikselleri etkiler     | - Gauss filtresi                 |
|                  |                     |                             | - Düşük frekanslı bozulma    | - Wiener filtresi                |
|                  |                     |                             | - Elektronik gürültü modeli  | - Ortalama filtre                |
+------------------+---------------------+-----------------------------+-----------------------------+-----------------------------------+
| Tuz-Biber        | Ayrık (0 ve 255)    | Rastgele siyah/beyaz piksel | - Anlık piksel bozulmaları   | - Medyan filtresi                |
|                  |                     |                             | - Sensör veya iletim hataları| - Morfolojik filtreler           |
|                  |                     |                             | - Yüksek kontrastlı noktalar | - Non-local means                |
+------------------+---------------------+-----------------------------+-----------------------------+-----------------------------------+
| Poisson          | Poisson Dağılımı    | np.random.poisson(image)    | - Foton istatistiklerinden   | - Anscombe dönüşümü              |
| (Shot Noise)     |                     |                             | - Parlaklığa bağımlı         | - Wavelet temizleme              |
|                  |                     |                             | - Düşük ışıkta belirgin      | - BM3D algoritması               |
+------------------+---------------------+-----------------------------+-----------------------------+-----------------------------------+
"""

# Gauss (Normal) Gürültüsü:
"""
- En yaygın gürültü türüdür, elektronik sistemlerde termal kaynaklıdır
- Her piksel değerine sürekli değerler eklenir
- Parametreleri: Ortalama (genelde 0), Standart Sapma (sigma)
- Sigma arttıkça gürültü şiddeti artar
- Özellikle düşük kaliteli sensörlerde belirgindir
"""
# Örnek parametrelerle oluşturma
gauss_low = add_gaussian_noise(image, sigma=15)  # Düşük gürültü
gauss_high = add_gaussian_noise(image, sigma=50) # Yüksek gürültü

# Tuz-Biber Gürültüsü:
"""
- Anlık piksel hataları (beyaz=tuz, siyah=biber)
- Sensör arızaları veya dijital iletim hatalarından kaynaklanır
- Gürültü yoğunluğu 'prob' parametresiyle kontrol edilir
- Kenarları bozma eğilimindedir
- Özellikle eski görüntüleme sistemlerinde yaygındır
"""
# Farklı yoğunluklarda örnekler
sp_low = add_salt_pepper_noise(image, prob=0.02)  # %2 gürültü
sp_high = add_salt_pepper_noise(image, prob=0.1)   # %10 gürültü

# Poisson Gürültüsü:
"""
- Foton istatistiklerinden kaynaklanan kuantum gürültüsü
- Parlak piksellerde daha belirgindir (ışığa bağımlı)
- Özellikle düşük ışıklı tıbbi/astronomik görüntülerde
- Gürültü miktarı görüntü yoğunluğuyla doğru orantılıdır
- Poisson dağılımı np.random.poisson() ile modellenir
"""
# Poisson gürültüsü parlaklıkla artar
bright_image = cv2.add(image, 100)  # Parlaklık artırma
poisson_bright = add_poisson_noise(bright_image)  # Daha çok gürültü
