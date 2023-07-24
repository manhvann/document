import cv2

#Mở video
video_file = "anh\\sample.mp4"
cam = cv2.VideoCapture(video_file)


#Đọc ảnh liên tục từ camera
while True:
    #Đọc từ camera
    ret,frame = cam.read()
    if ret == True: #Nếu thành công thì show hàng
        cv2.imshow("Video file",frame)
        #Viết code ở đây để xử lý thêm
    phim_bam = cv2.waitKey(1)
    if phim_bam == ord('q'):
        break

cam.release() #Tắt cam
cv2.destroyAllWindows()






