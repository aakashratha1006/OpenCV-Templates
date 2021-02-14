import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")
cv2.imshow("Image", img)

# Warp perspective - to get image's bird-eye view

width, height = 150, 300
pts1 = np.float32([[200,400], [350,200], [800,400], [500,700]])
pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)