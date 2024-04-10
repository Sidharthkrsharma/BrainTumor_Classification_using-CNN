import cv2 as cv
import numpy as np
from keras.models import load_model
from PIL import Image

model=load_model('BrainTumor10EpochsCategorical.h5')

image=cv.imread('pred\pred0.jpg')

img=Image.fromarray(image)

img=img.resize((64,64))

img=np.array(img)

input_img=np.expand_dims(img, axis=0)

result=model.predict_step(input_img)
print(result)

