import cv2 as cv 
import matplotlib.pyplot as plt


img = cv.imread("Photos/park.jpg")
cv.imshow("Boston",img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# BGR to HSV 

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

# BGR to L*a*b

lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow("Lab",lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR",hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab,cv.COLOR_Lab2BGR)
cv.imshow("LAB to BGR",lab_bgr)

# RGB to BGR
rgb_bgr = cv.cvtColor(rgb,cv.COLOR_RGB2BGR)
cv.imshow("RGB to BGR",rgb_bgr)




cv.waitKey(0)