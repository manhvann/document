import cv2


#Lệnh đọc ảnh: cv2.imread
anh_doc_tu_file = cv2.imread("anh\\sample.jpg",cv2.IMREAD_GRAYSCALE)


# Show ảnh:
cv2.imshow("Rose",anh_doc_tu_file)

#Ghi ảnh ra file
cv2.imwrite("anh\\dentrang.png",anh_doc_tu_file)

# Dừng chương trình chờ  bấm phím
cv2.waitKey()

cv2.destroyAllWindows() # <--- Đóng tất cả các cửa sổ đang mở