import cv2

cap = cv2.VideoCapture("http://192.168.0.2:8080/video")

while True:
    _, frame = cap.read()

    cv2.imshow("Image", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
