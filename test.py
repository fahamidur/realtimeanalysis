import os
import time
import shutil
import cv2
from PIL import Image
import numpy as np
from glob import glob
from pathlib import Path
from PIL import Image
from model import Model
from utils import plot



def processvideo(video_path):
    print(video_path)
    model = Model()
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    size = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    success, frame = cap.read()
    success = True
    while success and cap.isOpened():
        img = Image.fromarray(np.uint8(frame))

        ct = time.gmtime(time.time())
        name=f"{ct[0]}{ct[1]}{ct[2]}{ct[3]}{ct[4]}{ct[5]}{ct[6]}"

        img.save(f'./SP/{name}.jpg')

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        prediction = model.predict(frame)
        label = prediction['label']
        conf = prediction['confidence']
        print(f"label: {label} confidence: {conf}")

        img.save(f'./SP/{label}-{name}.jpg')


        # cv2.imshow('Recording...', frame)
        
        success, frame = cap.read()

    cap.release()
    cv2.destroyAllWindows()
    shutil.move(video_path,'./AV')




directory = './RVS'
while True:
    if len(os.listdir(directory)) != 0 :
        curr_path = f"{directory}/{os.listdir(directory)[-1]}"
        print(curr_path + " " + '1')
        processvideo(curr_path)

    else:
        pass


