import cv2
import imutils

#Lệnh đọc ảnh: cv2.imread
anh_doc_tu_file = cv2.imread("anh\\book.jpg",cv2.IMREAD_GRAYSCALE)


# Show ảnh:
cv2.imshow("Rose",anh_doc_tu_file)

# #Lấy ngưỡng
# nguong = 127
max = 255
# ketqua, anh_da_loc_nguong = cv2.threshold(anh_doc_tu_file,nguong,255,cv2.THRESH_BINARY)

#Lấy ngưỡng bằng adaptive
anh_da_loc_nguong = cv2.adaptiveThreshold(anh_doc_tu_file,max,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,199,25)

cv2.imshow("Rose da loc nguong",anh_da_loc_nguong)
cv2.waitKey()
cv2.destroyAllWindows()