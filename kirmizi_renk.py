import cv2
import numpy as np

# Görüntüyü yükle
image_path = 'Photos/ornek_goruntu.jpg' 
image = cv2.imread(image_path)
if image is None:
    print(f"{image_path} dosyasi bulunamadi.")
    exit()

# Görüntüyü RGB formatına dönüştür
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Kırmızı renk aralığını tanımla (BGR formatında)
lower_red = np.array([0, 0, 100])    # Alt sınır
upper_red = np.array([100, 100, 255])  # Üst sınır

# Belirtilen renk aralığında maske oluştur
mask = cv2.inRange(image_rgb, lower_red, upper_red)

# Konturları bul
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Her bir kontur için bir minimum daire çiz
for contour in contours:
    # Konturun etrafına bir daire çiz
    (x, y), radius = cv2.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(image_rgb, center, radius, (255, 0, 0), 2 )  # Yeşil renkte bir daire çiz

# Sonucu göster
cv2.imshow('Original Image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()