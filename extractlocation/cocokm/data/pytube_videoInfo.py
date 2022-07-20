from pytube import YouTube
DOWNLOAD_FOLDER = "C:\\Users\\hlee\\Desktop"
url = "https://www.youtube.com/watch?v=d6LGnVCL1_A"
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)

# 영상의 제목, 길이, 게시자, 날짜, 조회수, 키워드, 설명, 썸네일 URL 같은 정보 가져오기
from pytube import YouTube
DOWNLOAD_FOLDER = "C:\\Users\\hlee\\Desktop"
url = "https://www.youtube.com/watch?v=d6LGnVCL1_A"
yt = YouTube(url)
print("제목 : ", yt.title)
print("길이 : ", yt.length)
print("게시자 : ", yt.author)
print("게시날짜 : ", yt.publish_date)
print("조회수 : ", yt.views)
print("키워드 : ", yt.keywords)
print("설명 : ", yt.description)
print("썸네일 : ", yt.thumbnail_url)
