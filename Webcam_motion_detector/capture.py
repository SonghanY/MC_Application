import cv2, time

video = cv2.VideoCapture(0)  # trigger the camera

cnt=1   # 计算video产生了多少个frame

# make many image to form video 
while True:
    cnt = cnt + 1
    check, frame = video.read()     # numpy array of image

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #time.sleep(2)
    cv2.imshow("Capturing", gray)

    key=cv2.waitKey(1)   # press the key，the subsequent line will be executed

    if key==ord('q'):
        break

print(cnt)
#video.release()     # video be released
cv2.destroyAllWindows()