from yt_dlp import YoutubeDL

link = input("Enter the YouTube video URL: ")

options = {
    "format": "bestaudio/best",
    "outtmpl": "module_5/%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
        }
    ],
}

with YoutubeDL(options) as audio:
    audio.download([link])

print("Audio downloaded successfully")

#.\.venv\Scripts\python.exe module_5\todownload_from_youtube_m3.py    terminal command to run the script
# This script will download the audio from YouTube and save it in the module_5 folder with the title of the video as the filename.

