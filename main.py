from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

@app.route("/")
def MusicDownload():
    return render_template("MusicDownload.html")

@app.route('/download/', methods=['POST'])
def download():
    link = request.form['link']
    try:
        yt = YouTube(link)
        video = yt.streams.filter(only_audio=True).first()
        directory = '\Downloads'
        if not os.path.exists(directory):
            os.makedirs(directory)
        os.chdir(directory)
        video.download(filename=f"{yt.title}.mp3")
        return render_template("paginadownload.html",title={yt.title},directory=directory)

    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)