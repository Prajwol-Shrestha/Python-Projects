from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from tkinter import messagebox

window = Tk()
window.title("Youtube Video Downloader")
window.geometry('400x200')


def download():
	url = url_entrybox.get()
	try:
		youtube = YouTube(url)
		Save_path = "C:\\Users\\Prabin\\Videos\\videos"
		youtube.streams.filter(type = "video",progressive = True,file_extension = "mp4").first().download(Save_path)
		popup = messagebox.showinfo("Info", "Download Complete")
		Label(window, text = popup).grid(row = 0, column = 0)
	except ConnectionError as e:
		popup = messagebox.showerror("Error", e)
		Label(window, text = popup).grid(row = 0, column = 0)
	except Exception as e:
		popup = messagebox.showerror("Error", e)
		Label(window, text = popup).grid(row = 0, column = 0)	
		
		
#Drop Down Menu to choose the file format.



url_label = Label(window, text = "URL ", padx = 10)
url_label.grid(row = 0,column = 0, columnspan = 2)

url_entrybox = Entry(window,width = 50)
url_entrybox.grid(row = 0, column = 2, columnspan = 2, pady = 5)

download_button = Button(window, text = "Download", command = download, padx = 40, pady = 10, bd = 3)
download_button.grid(row = 1, column = 2 , columnspan = 2)


window.mainloop()