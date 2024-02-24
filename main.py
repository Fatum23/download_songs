from pytube import Playlist, YouTube
import youtube_dl
import re

URl = "https://www.youtube.com/playlist?list=PLLPYwPfN7fKQxDncTGmjP2jhqslGLsTQR"


playlist = Playlist(URl)


for video in playlist.videos:
    video_title = video.title
    video_url = video.watch_url
    print(f"Название: {video_title}")
    print(f"URL: {video_url}\n")

    yt = YouTube(video_url)
    audio = yt.streams.get_audio_only()  # Get the audio stream
    audio_title = yt.title
    audio_title = re.sub(r'\W+', ' ', audio_title)
    audio_filename = f"results/{audio_title}.mp3"  # Specify the filename to save the audio
    audio.download(filename=audio_filename)
    print(f"Download complete: {audio_filename}")