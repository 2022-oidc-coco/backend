from pytube import YouTube

DOWNLOAD_FOLDER = "C:\\Users\\hlee\\Desktop"

url = "https://www.youtube.com/watch?v=d6LGnVCL1_A"

yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)