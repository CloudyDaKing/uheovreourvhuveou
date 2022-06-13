from pytube import YouTube
import utils
from utils.upload_video import upload_video

print("welcome to fishy installer")
url = input("Youtube url: ")
my_video = YouTube(url)

print("*********************Video Title************************")
#get Video Title
print(my_video.title)
vidname = my_video.title

print("********************Tumbnail Image***********************")
#get Thumbnail Image
print(my_video.thumbnail_url)

print("********************Download video*************************")
#get all the stream resolution for the 
for stream in my_video.streams:
    print(stream)

#set stream resolution
my_video.streams.filter(res="360p").first().download()

#or
#my_video = my_video.streams.first()

print (vidname)    

video_data = {
            "file": vidname+".mp4",
            "title": "fish",
            "description": "fish",
            "keywords":"fish,animal",
            "privacyStatus":"public"
    }


upload_video(video_data)




