import cv2

# Resmi okuyoruz
image = cv2.imread("./resim.jpg")

# Resmi gösterme
cv2.imshow("Ug urcan Turk", image)  # Pencere başlığı ve resim


print("Görüntü boyutu (yükseklik, genişlik, kanal sayısı):", image.shape)
print("Görüntü veri tipi:", image.dtype)



cv2.waitKey(0)  # Herhangi bir tuşa basılana kadar pencereyi açık tut
