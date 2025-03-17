# Görüntü İşleme Dersi - Ödev 1

Bu proje, OpenCV kütüphanesi kullanılarak basit bir görüntü okuma ve gösterme uygulamasını içerir.

## Özellikler

- Resim dosyasını okuma
- Resmi ekranda gösterme
- Görüntü boyutlarını ve veri tipini gösterme

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
python odev.py
```
3. Resim penceresi açılacaktır
4. Kapatmak için herhangi bir tuşa basın

## Kod Açıklaması

- `cv2.imread()`: Resim dosyasını okur
- `cv2.imshow()`: Resmi bir pencerede gösterir
- `image.shape`: Görüntünün boyutlarını verir (yükseklik, genişlik, kanal sayısı)
- `image.dtype`: Görüntü verilerinin tipini gösterir



