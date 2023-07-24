import cv2

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    if ret:
        # Tính tọa độ điểm trung tâm
        # shape là một tuple có 2 phần tử (height, width)
        height = frame.shape[0]
        width = frame.shape[1]
        centre_x = width // 2
        centre_y = height // 2

        # Tính kích thước 20% của vùng trung tâm cần lấy
        crop_width = int(width * 0.2)
        crop_height = int(height * 0.2)

        left_top_x = centre_x - crop_width // 2
        left_top_y = centre_y - crop_height // 2


        #Chú ý trục Oy đi từ trên xuống, trong frame nói y trước, x sau
        # Cắt ảnh từ khung hình gốc từ điểm (left_top_y,left_top_x) đến(left_top_y + crop_height,left_top_x + crop_width)
        crop_frame = frame[left_top_y:left_top_y + crop_height, left_top_x:left_top_x + crop_width]

        cv2.imshow("Crop frame", crop_frame)
        cv2.imshow("Goc", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()
