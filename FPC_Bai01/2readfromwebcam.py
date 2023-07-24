import cv2

#Mở webcam
camera_id = 0 #Là một số nguyên dương chạy từ 0 -> N, mã của camera muốn đọc
cam = cv2.VideoCapture(camera_id)


#Đọc ảnh liên tục từ camera
while True:
    #Đọc từ camera
    ret,frame = cam.read()
    if ret == True: #Nếu thành công thì show hàng
        cv2.imshow("Webcam",frame)
        #Viết code ở đây để xử lý thêm
    phim_bam = cv2.waitKey(1)
    if phim_bam == ord('q'):
        break

cam.release() #Tắt cam
cv2.destroyAllWindows()






