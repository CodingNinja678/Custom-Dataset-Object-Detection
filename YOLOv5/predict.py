from ultralytics import YOLO

model=YOLO("yolov8m-seg-custom.pt")

model.predict(source="4.png",show=True,save=True,hide_labels=False,hide_conf=False,conf=0.5,save_txt=False,save_crop=False,line_thickness=10)
#model.predict(source="2.png",show=True,save=True,hide_labels=False,hide_conf=False,conf=0.5,save_txt=False,save_crop=False,line_thickness=10)
#model.predict(source="3.png",show=True,save=True,hide_labels=False,hide_conf=False,conf=0.5,save_txt=False,save_crop=False,line_thickness=10)