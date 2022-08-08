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
        v_records, p_records = data_processing_(irum,dataset)
        print("-----------------데이터 전처리 결과-----------------")
        pprint(v_records)
        for i in range(len(v_records)):
            # form = Form(records[i])
            form = Video(
            videoID=v_records[i]['video_id'],
            publishTime=v_records[i]['publishTime'].to_pydatetime(),
            viewCount=v_records[i]['viewCount'],
            author = v_records[i]['author'],
            videoThumbnail = v_records[i]['video_thumbnail'],
            title = v_records[i]['title'],
            videoURL = v_records[i]['video_url']
            )
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
            form.save()
        videoinfo = Video.objects.all()
        print("-----------------DB-----------------")
        pprint(videoinfo)
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
