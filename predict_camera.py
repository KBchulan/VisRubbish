import cv2
from ultralytics import YOLOv10

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

model = YOLOv10("best.pt") # model path

while True:
    ret,frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    img = cv2.resize(frame, (640, 640))
    results = model.predict(source=cv2.cvtColor(img, cv2.COLOR_BGR2RGB),imgsz=640,conf= 0.05,save=False)
    

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) == ord('q'): # 按下q退出
        break

cap.release()
cv2.destroyAllWindows()