from ultralytics import YOLOv10

# 模型配置路径
model_yaml_path = "./yolov10s.yaml"

# 数据集路径
data_yaml_path = "./data/data.yaml"

# 预训练模型路径
pre_model_name = "./yolov10s.pt"

if __name__ == '__main__':
    model = YOLOv10(model_yaml_path).load(pre_model_name)

    results = model.train(data = data_yaml_path,
                          epochs = 10,
                          batch = 2,
                          name = 'trash'
                          )