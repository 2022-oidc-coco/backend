from django.shortcuts import render
# from collecting_data import collect_data
# from data_processing import data_processing_
from cocokm.data.collecting_data import collect_data
from cocokm.data.data_processing import data_processing_
from cocokm.forms import *

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
        # print(records)
        for i in range(len(records)):
            form = Form(records[i])
            print(form)
            if form.is_valid():
                form.save()
        locinfo = locationInfo.objects.all()
        print(locinfo)
        print("---------------form----------------")
        print(form)
        return render(request, "list.html", {"key":irum, 'locationInfo':locinfo})
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
    locationInfoList = locationInfo.objects.all() #Article이라는 DB에 있는 모든 column을 가져옴
    return render(request, 'list.html',{"key":irum,'locationInfoList':locationInfoList})

def view(request,num="1"):
    locInfo = locationInfo.objects.get(id=num)
    return render(request, 'view.html',{'locInfo':locInfo})
