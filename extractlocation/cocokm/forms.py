from django.forms import ModelForm
from cocokm.models import *

class videoForm(ModelForm):
    class Meta:
        model = Video
        fields=['videoID','title','videoURL','videoThumbnail','publishTime','viewCount','author'] #model에 있는 필드명이어야함

class placeForm(ModelForm):
    class Meta:
        model = Place
        fields=['videoID','placeName','placeID','x','y','category','placeURL','placeThumbnail','placeRating'] #model에 있는 필드명이어야함
