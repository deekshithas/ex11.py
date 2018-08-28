#image blurring
import cv2
import numpy as np
img=cv2.imread("flower.jpg")
cv2.imshow("original",img)
cv2.waitKey(0)
blur=cv2.blur(img,(3,3))
cv2.imshow("blur image",blur)
cv2.waitKey(0)

Gausian=cv2.GausianBlur(img,(7,7),0)
cv2.imshow("gausian blur image",Gausian)
cv2.waitKey(0)

median=cv2.medianBlur(img,5)
cv2.imshow("median blur image",median)
cv2.waitKey(0)

bilateral=cv2.bilateralBlur(img,9,75,75)
cv2.imshow("bilateral blur image",bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()
