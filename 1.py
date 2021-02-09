import cv2

#load an image
img = cv2.imread('assets/image.jpg', 0)

#resize an image
# img = cv2.resize(img, (500, 500))

#change ratio of img
# img = cv2.resize(img, (0, 0), fx=2, fy=2)

#rotate an image
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

#write output to new img
cv2.imwrite('assets/new_image.jpg', img)


#display an image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()