from pytube import Playlist, YouTube
from pytube.innertube import _default_clients

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]
import re
import os

URl = "https://www.youtube.com/playlist?list=PLLPYwPfN7fKQxDncTGmjP2jhqslGLsTQR"


playlist = Playlist(URl)


for count, video in enumerate(playlist.videos):
    tries = 0
    while True:
        if tries > 5:
            print("Too many attempts, skipping...")
            break
        try:
            video_title = video.title
            video_url = video.watch_url
            print(f"Название: {video_title}")
            print(f"URL: {video_url}\n")
        
            yt = YouTube(video_url)
            if yt.length > 60 * 60 * 3:
                print("Too long video")
            else:
                audio = yt.streams.get_audio_only()  # Get the audio stream
                audio_title = yt.title
                audio_title = re.sub(r'\W+', ' ', audio_title)
                audio_filename = f"results/{audio_title}.mp3"  # Specify the filename to save the audio
                if not os.path.isfile(audio_filename):
                    audio.download(filename=audio_filename)
                    print(f"Download complete: {audio_filename}")
                else:
                    print("Already downloaded")
            print(f"{count + 1} / {len(playlist.videos)}")
            tries = 0
            break
        except Exception as e:
            tries += 1
            print(e)
