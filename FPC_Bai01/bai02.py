import cv2
import time
import imutils

video_file = "anh\\sample.mp4"
video = cv2.VideoCapture(video_file)

xoay = 0
while True:
    ret,frame = video.read()
    if ret:
        phim_bam = cv2.waitKey(1)
        if phim_bam == ord('q'):
            break
        elif phim_bam == ord('a'):
            xoay = 90
        elif phim_bam == ord('d'):
            xoay = -90
        elif phim_bam == ord(' '):
            xoay =0
        if xoay != 0:
            frame = imutils.rotate(frame,xoay)
        cv2.imshow("video",frame)
        fps = video.get(cv2.CAP_PROP_FPS)
        time.sleep(1 / fps)

cv2.destroyAllWindows()
video.release()
