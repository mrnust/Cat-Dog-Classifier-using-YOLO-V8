

# Image classification ( Cat and Dog classification) ---------------------------------------


from ultralytics import YOLO V8

# Load a model
model = YOLO("yolov8n-cls.pt") 

# Use the model
model.train(data="C:/Users/HP/Desktop/Python/Dog and Cat Image classifier", epochs=20)  # train the model






