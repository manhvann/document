import cv2


#Đọc ảnh
image = cv2.imread("anh\\balloon.png")


#Tạo ảnh xám
anh_xam = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Tao nguong
ret,nguong = cv2.threshold(anh_xam,245,250,cv2.THRESH_BINARY)

cv2.imshow("Nguong",nguong)
#Đếm đươc số bóng
#Đếm số đường bao(contour) có kích thước > 1 giá trị định trước do tta ước lượng
contours, _ =cv2.findContours(nguong,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
MIN_AREA = image.shape[1]*image.shape[0]/150
dem = 0
for cnt in contours[:-1]:
    if cv2.contourArea(cnt)>=MIN_AREA:
        dem+=1
        cv2.drawContours(image,[cnt],-1,(0,255,0),2,cv2.LINE_AA)
cv2.imshow("Anh",image)
print("So bong la: ",dem)
cv2.waitKey()
cv2.destroyAllWindows()