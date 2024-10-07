from ultralytics import YOLOv10

# 模型路径，基本放best即可
model = YOLOv10("best.pt")

# 预测图片路径
result = model.predict(source = "data/test/images",         #记得设置为左斜杠
                       imgsz =640,
                       conf = 0.3,          # 置信度，设置小一点比较好
                       save = True          # 相机的话设置为False
                       )