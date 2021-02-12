import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
cv2.imshow("Original Image", img)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", imgGray)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
cv2.imshow("Blur image", imgBlur)
imgCanny = cv2.Canny(img, 100, 100)
cv2.imshow("Canny image", imgCanny)

kernel = np.ones((5,5), np.uint8)
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)
cv2.imshow("Dilated image", imgDilation)
imgEroded = cv2.erode(imgDilation, kernel, iterations = 1)
cv2.imshow("Eroded image", imgEroded)
cv2.waitKey(0)