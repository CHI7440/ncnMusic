from django.shortcuts import render
from .forms import ImageForm
from django.conf import settings
from models.test import detect_emotion
from models.spotify import play_from_playlist
import cv2,os,numpy
import urllib.parse

happy_songs_uri = 'spotify:playlist:0TB1scqYXu8vaFwxiOaT1j'
sad_songs_uri = 'spotify:playlist:6eq5Zviu57AxTT02x0F3pE'
neutral_songs_uri = 'spotify:playlist:1QbJym8B3Xb6rpXdk7MBiJ'

# Create your views here.
def home_screen(request):
  # print(request.headers)
  form = ImageForm(request.POST,request.FILES)
  return render(request,'index.html',{'form':form})

def get_emotion(request):
  if request.method == 'POST':
    form = ImageForm(request.POST,request.FILES)
    if form.is_valid():
      uploaded_img = form.save()
      imgUrl = uploaded_img.image.url
      print(imgUrl)
      imgPath = imgUrl.lstrip('/')
      emotion = detect_emotion(imgPath)
      if emotion == 'Happy':
        play_from_playlist(happy_songs_uri)
        return render(request,'second.html',{'form':form,'emotion':emotion})
              
      if emotion == 'Sad':
        play_from_playlist(sad_songs_uri)
        return render(request,'second.html',{'form':form,'emotion':emotion})
              
      if emotion == 'Neutral':
        play_from_playlist(neutral_songs_uri) 
        return render(request,'second.html',{'form':form,'emotion':emotion})
      
      else:
        form = ImageForm()
        return render(request,'second.html',{'form':form})  
      
    else:
      form = ImageForm()
      return render(request,'index.html',{'form':form})
    
  