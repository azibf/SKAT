from ultralytics import YOLO

# Загрузка модели
model = YOLO("yolov8x.yaml")  # создание новой модели из файла

# Исользование модели
model.train(data='custom_data.yaml', epochs=10)
metrics = model.val()
#results = model("https://ultralytics.com/images/bus.jpg")
path = model.export(format="onnx")