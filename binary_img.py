import cv2

original_img = cv2.imread('kuda.png', cv2.IMREAD_GRAYSCALE)
(thresh, binary_img) = cv2.threshold(original_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite('kuda_binary.png', binary_img)