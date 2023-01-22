import uvicorn
from fastapi import FastAPI
import cv2
from glob import glob
from pathlib import Path
import os
from model import Model
from utils import plot
app = FastAPI()

@app.post('/')
def process_video():
    directory = './RVS'
    curr_path = f"{directory}/{os.listdir(directory)[-1]}"
    word=curr_path.split('.')
    word = word.split("-")
    return {
        'label' : word[0],
        'time' : word[1]
    }

if __name__ == '__main__':

    process_video()
    uvicorn.run(app, host='127.0.0.1', port=8000)