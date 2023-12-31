from ultralytics import YOLO

import cv2


model_path = r'C:\Users\Suhan\PycharmProjects\CustomData--Butterfly\runs\segment\train\weights\last.pt'

image_path = r'C:\Users\Suhan\PycharmProjects\CustomData--Butterfly\1.png'

img = cv2.imread(image_path)
H, W, _ = img.shape

model = YOLO(model_path)

results = model(img)

for result in results:
    for j, mask in enumerate(result.masks.data):

        mask = mask.numpy() * 255

        mask = cv2.resize(mask, (W, H))

        cv2.imwrite('./output.png', mask)