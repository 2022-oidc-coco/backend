from django.forms import ModelForm
from cocokm.models import *

class Form(ModelForm):
    class Meta:
        model = locationInfo
        fields=['place_name','x' ,'y','place_url','category','video_id','publishTime','viewCount'] #model에 있는 필드명이어야함
