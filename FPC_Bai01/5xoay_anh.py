import cv2
import imutils

#Lệnh đọc ảnh: cv2.imread
anh_doc_tu_file = cv2.imread("anh\\sample.jpg")


# Show ảnh:
cv2.imshow("Rose",anh_doc_tu_file)

#Xoay ảnh
anh_xoay = imutils.rotate(anh_doc_tu_file,90)


#Show ảnh đã xoay
cv2.imshow("Rose xoay", anh_xoay)

cv2.waitKey()
