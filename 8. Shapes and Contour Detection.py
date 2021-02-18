import cv2
import numpy as np

def getContours(img):
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)
        peri = cv2.arcLength(cnt, True)
        #print(peri)
        approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
        #print(approx)
        print(len(approx))
        objcor = len(approx)
        x, y, w, h = cv2.boundingRect(approx)

        if objcor==3: objectType="Triangle"
        elif objcor==4:
            aspRatio = w/float(h)
            if aspRatio > 0.95 and aspRatio < 1.05:
                objectType = "Square"
            else:
                objectType = "Rectangle"
        else: objectType="None"

        cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(imgContour, objectType, (x+(w//2)-10, y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX, 0.3, (0,0,0), 1)

img = cv2.imread("Resources/shapes.jpg")
imgContour = img.copy()
cv2.imshow("Image", img)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

imgBlank = np.zeros_like(img)
#cv2.imshow("Blurred image", imgBlur)
cv2.imshow("Canny image", imgCanny)
#cv2.imshow("Blank image", imgBlank)
cv2.imshow("Contour image", imgContour)

cv2.waitKey(0)