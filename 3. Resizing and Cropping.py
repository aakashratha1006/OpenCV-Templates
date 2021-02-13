import cv2

img = cv2.imread('Resources/lena.png')
print(img.shape)
cv2.imshow("Original image", img)
imgResize = cv2.resize(img, (300, 200))
cv2.imshow("Resized image", imgResize)
imgCropped = img[0:200, 200:500]
cv2.imshow("Cropped image", imgCropped)
cv2.waitKey(0)
print(imgResize.shape)