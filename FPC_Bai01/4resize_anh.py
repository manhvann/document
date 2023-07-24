import cv2


#Lệnh đọc ảnh: cv2.imread
anh_doc_tu_file = cv2.imread("anh\\sample.jpg")


# Show ảnh:
cv2.imshow("Rose",anh_doc_tu_file)

#Resize
anh_nho = cv2.resize(anh_doc_tu_file,dsize = None,fx = 0.5,fy = 0.5) #Dsize là kích thước thủ công


cv2.imshow("Rose resize",anh_nho)
cv2.waitKey()
