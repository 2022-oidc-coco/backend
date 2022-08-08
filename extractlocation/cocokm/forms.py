from django.forms import ModelForm
from cocokm.models import *

class Form(ModelForm):
    class Meta:
        model = Video
        fields=['videoID','title','videoURL','videoThumbnail','publishTime','viewCount','author'] #model에 있는 필드명이어야함
