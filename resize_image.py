import cv2

img = cv2.imread("image.jpg")

resize = cv2.resize(img, (300, 300))

cv2.imshow("Resized Image", resize)

cv2.waitKey(0)
cv2.destroyAllWindows()
