import time
import cv2
camera_port_0 = 3

camera_0 = cv2.VideoCapture(camera_port_0)
counter = 0

for i in range(1,100):
    time.sleep(0.1)  # If you don't wait, the image will be dark
    return_value, image = camera_0.read()
    cv2.imwrite(str(counter)+ ".png", image)
    counter +=1

del(camera_0)  # so that others can use the camera as soon as possible
