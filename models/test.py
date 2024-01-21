import cv2
import numpy as np
from keras.models import load_model

model = load_model('models/model_file.h5')


faceDetect = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

labels_dict = {0: 'Happy', 1: 'Neutral', 2: 'Sad'}

def detect_emotion(img,frame,gray):
  text = ''
  try:
    if cv2.os.path.exists(img):
      faces= faceDetect.detectMultiScale(gray, 1.3, 3)
      if len(faces)>0 :
        for x,y,w,h in faces:
          sub_face_img=gray[y:y+h, x:x+w]
          resized=cv2.resize(sub_face_img,(48,48))
          normalize=resized/255.0
          reshaped=np.reshape(normalize, (1, 48, 48, 1))
          result=model.predict(reshaped)
          label=np.argmax(result, axis=1)[0]
          text = labels_dict[label]
          print(labels_dict[label])
          cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
          cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
          cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
          cv2.putText(frame, labels_dict[label]+text, (x, y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
    else:
      print("Path does not exist")
  except Exception as e:
    print(e)
  print(text)
  return text
 