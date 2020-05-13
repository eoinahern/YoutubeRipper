from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)
youtube_url_partial = "https://www.youtube.com/watch?v"


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("main_page.html")
    elif request.method == "POST":
        url = request.form.get("url")

        if youtube_url_partial in url:
            video = YouTube(url)
            vid_streams = video.streams.filter(mime_type="video/mp4", progressive=True)
            video_title = video.title
            dictionary = {i: vid_streams[i] for i in range(0, len(vid_streams))}
            return render_template("search_complete.html", streams=dictionary, title=video_title)
        else:
            return render_template("error_loading.html")

