import cv2


#Đọc ảnh
image = cv2.imread("anh\\bienso.jpg")


#Tạo ảnh xám
anh_xam = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Tao nguong
ret,nguong = cv2.threshold(anh_xam,100,250,cv2.THRESH_BINARY)


contours, _ =cv2.findContours(nguong,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
MIN_HEIGHT = image.shape[0] * 0.5
MAX_WIDTH = image.shape[1] * 0.1
dem = 0
for cnt in contours[:-1]:
    #Lấy tọa độ hình chữ nhật bao quanh đường biên
    x,y,w,h = cv2.boundingRect(cnt)
    if w<=MAX_WIDTH and h>=MIN_HEIGHT:
        dem+=1
        crop_number = image[y:y+h,x:x+w]
        cv2.imwrite("numbers\\{}.png".format(dem),crop_number)
        cv2.drawContours(image,[cnt],-1,(0,255,0),2,cv2.LINE_AA)
print(dem)
cv2.imshow("Bien so",image)
cv2.imshow("nguong",nguong)
cv2.waitKey()
cv2.destroyAllWindows()