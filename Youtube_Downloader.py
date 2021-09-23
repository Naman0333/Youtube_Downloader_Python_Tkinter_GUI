# Import the Pytube,tkinter & time library

from pytube import YouTube
import tkinter as tk
import os
import time
from tkinter import ttk

# function for download youtube video
def yt_downloader():
    start_time = time.time()
    download_location = "Youtubes_Downloads/"
    yt=YouTube(url_entry.get())
    yt.streams.get_highest_resolution().download(download_location)
    end_time = time.time()
    popup_window = tk.Tk()
    popup_window.geometry("300x200+0+0")
    popup_window.wm_title("Download Status: ")



    str1 = "Download Successful!!\n"
    str2 = f"Total time taken : {end_time - start_time}"
    msg = str1 + str2

    msg_label1 = tk.Label(popup_window, text=msg)
    msg_label1.pack(side=tk.TOP, fill=tk.X, pady=10)

    quit_btn = ttk.Button(popup_window, text="Quit", command=popup_window.destroy)
    quit_btn.pack()

    popup_window.mainloop()


# create mainWindow

root = tk.Tk()
root.wm_title("Youtube Downloader")
root.geometry("400x300+0+0")
root.resizable(False, False)
# Create a Label for Youtube URL & also placeing the respective positon

url_label = tk.Label(root, text="Enter the youtube Video URL: ", font=("bold", 15))
url_label.place(x=80, y=50)

# Create a Entry for Youtube URL & a also placeing the respective position

url_entry = tk.Entry(root, width=30)
url_entry.place(x=120, y=100)

# Create a Download Button for download Youtube video & placeing the respective position

download_btn = tk.Button(root, text="Download", width=20, command=yt_downloader)
download_btn.place(x=135, y=140)

root.mainloop()