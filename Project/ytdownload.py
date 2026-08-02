import yt_dlp

url = input("Enter YouTube video URL: ")

try:
    ydl_opts = {
        'format': 'best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Download completed successfully!")

except Exception as e:
    print("Error occurred:", e)
