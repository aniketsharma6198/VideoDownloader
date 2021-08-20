from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil


def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download():
    video_url = url_entry.get()
    file_path = path_label.cget("text")
    mp4 = YouTube(video_url).streams.get_highest_resolution().download()
    video = VideoFileClip(mp4)
    video.close()
    shutil.move(mp4, file_path)
    status_label.config(text="Download Complete")


root = Tk()
root.title("Video Downloader")
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# App_Label
app_label = Label(root, text="Video Downloader", fg='blue', font=("Courier New", 20))
canvas.create_window(200, 30, window=app_label)

# url entry and label
url_label = Label(root, text='Enter URL', fg='black', font=('Courier New', 10))
canvas.create_window(80, 80, window=url_label)
url_entry = Entry(root, width=35)
canvas.create_window(250, 80, window=url_entry)

# path to download video
path_label = Label(root, text='Select path to download', fg='black', font=('Courier New', 10))
canvas.create_window(200, 120, window=path_label)
path_button = Button(root, text='Select', width=10, fg='black', font=('Courier New', 10), command=get_path)
canvas.create_window(200, 150, window=path_button)

# Download Button
download_button = Button(root, text='Start Download', fg='black', font=('Courier New', 10), command=download)
canvas.create_window(200, 200, window=download_button)

# Status Label
status_label = Label(root, text="", fg='black', font=('Courier New', 10))
canvas.create_window(200, 250, window=status_label)

root.mainloop()
