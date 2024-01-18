import cv2,os
import numpy as np
from keras.models import load_model

model = load_model('models/model_file.h5')


faceDetect = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

labels_dict = {0: 'Happy', 1: 'Neutral', 2: 'Sad'}

def detect_emotion(img):
  text = ''
  try:
    if cv2.os.path.exists(img):
      frame = cv2.imread(img)
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      resized = cv2.resize(gray, (48, 48))
      normalize = resized / 255.0
      reshaped = np.reshape(normalize, (1, 48, 48, 1))
      result = model.predict(reshaped)
      label = np.argmax(result, axis=1)[0]
      text = labels_dict[label]
      print(labels_dict[label])
    else:
      print("Path does not exist")
  except Exception as e:
    print(e)
  print(text)
  return text
