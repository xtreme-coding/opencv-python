import cv2

#load an image
img = cv2.imread('assets/image.jpg', 0)

#display an image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()