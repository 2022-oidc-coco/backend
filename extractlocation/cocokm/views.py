from django.shortcuts import render
# from collecting_data import collect_data
# from data_processing import data_processing_
from cocokm.data.collecting_data import collect_data
from cocokm.data.data_processing import data_processing_
from cocokm.forms import *
from decimal import Decimal
from datetime import datetime
from pprint import pprint

irum = ""

# Create your views here.
def checkinfo(request):
    # if request.method =="POST":
    #     form = Form(request.POST)
    #     if form.is_valid():
    #         form.save() #DB에 저장
    # else:
    #     form = Form()
    # return render(request, 'write.html',{'form':form})
    return render(request, 'checkinfo.html')

def insert(request):
    if request.method == 'GET':
        print('get 요청처리')
        return render(request, 'insert.html')
    elif request.method == 'POST':
        print('post 요청처리')
        #irum = request.POST.get("name")
        irum = request.POST["name"]
        dataset = collect_data(irum,'viewCount')
        records = data_processing_(irum,dataset)
        print("-----------------데이터 전처리 결과-----------------")
        pprint(records)
        for i in range(len(records)):
            # form = Form(records[i])
            form = Video(
            videoID=records[i]['videoID'],
            publishTime=records[i]['publishTime'].to_pydatetime(),
            viewCount=records[i]['viewCount'],
            author = records[i]['author'],
            videoThumbnail = records[i]['videoThumbnail'],
            title = records[i]['title'],
            videoURL = records[i]['videoURL']
            )
            form.save()
            form2 = Place(
            videoID = Video.objects.get(pk=records[i]['videoID']),
            placeName = records[i]['placeName'],
            placeID = records[i]['placeID'],
            x = records[i]['x'],
            y = records[i]['y'],
            category = records[i]['category'],
            placeURL = records[i]['placeURL'],
            placeThumbnail = records[i]['placeThumbnail'],
            placeRating = records[i]['placeRating']
            )
            form2.save()
            # form = locationInfo(
            # place_name = records[i]['place_name'][0],
            # x=Decimal(records[i]['x'][0]),
            # y =Decimal(records[i]['y'][0]),
            # place_url =records[i]['place_url'],
            # category =records[i]['category'],
            # video_id=records[i]['video_id'],
            # publishTime=records[i]['publishTime'].to_pydatetime(),
            # viewCount=records[i]['viewCount'],
            # author = records[i]['author']
            # )
            # print(form)
            # if form.is_valid():
        videoinfo = Video.objects.all()
        placeinfo = Place.objects.all()
        print("-----------------DB-----------------")
        pprint(videoinfo)
        pprint(placeinfo)
        # print("---------------form----------------")
        # print(form)
        return render(request, "list.html", {"key":irum, 'Video':videoinfo})
    else:
        print("요청실패")
#
# def write(request):
#     if request.method =="POST":
#         form = Form(request.POST)
#         if form.is_valid():
#             form.save() #DB에 저장
#     else:
#         form = Form()
#     return render(request, 'write.html',{'form':form})

def list(request):
    videoInfoList = Video.objects.all() #Article이라는 DB에 있는 모든 column을 가져옴
    return render(request, 'list.html',{"key":irum,'videoInfoList':videoInfoList})

def view(request,num="1"):
    videoInfo = Video.objects.get(id=num)
    return render(request, 'view.html',{'videoInfo':videoInfo})
