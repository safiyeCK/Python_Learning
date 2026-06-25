try:
    from yt_dlp import YoutubeDL
except ImportError:
    print("yt-dlp is not installed. Install it using: pip install yt-dlp")
    exit()


def download(link):
    options = {
        "outtmpl": "module_5/%(title)s.%(ext)s"
    }

    try:
        with YoutubeDL(options) as video:
            video.download([link])
        print("Download is completed successfully")
    except Exception:
        print("Download failed. Please check the URL.")


link = input("Enter the YouTube video URL: ")

if link == "":
    print("You did not enter a URL.")
else:
    download(link)


    #.\.venv\Scripts\python.exe module_5\todownlod_from_youtube.py    terminal command to run the script
    # This script will download the video from YouTube and save it in the module_5 folder with the title of the video as the filename.

    # .\.venv\Scripts\yt-dlp.exe --write-auto-subs --sub-lang tr --skip-download -o "module_5/%(title)s.%(ext)s" "https://www.youtube.com/watch?v=i7CXdy7K49Y"

    #.\.venv\Scripts\yt-dlp.exe --write-auto-subs --sub-lang tr --skip-download -o "module_5/%(title)s.%(ext)s" "https://www.youtube.com/watch?v=i7CXdy7K49Y"