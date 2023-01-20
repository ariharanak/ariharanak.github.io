from tkinter import *
from pytube import YouTube

ytd=Tk()
ytd.geometry('500x300')
ytd.title("YOUTUBE VIDEO DOWNLOADER")

lab1=Label(ytd, text="YOUTUBE VIDEO DOWNLOADER", font='arial 20 bold').pack()
link=StringVar()
lab2=Label(ytd,text="PASTE YOUR LINK",font='arial 15 bold').place(x=160,y=50)
Entry(ytd,width=70,textvariable=link,bg='yellow').place(x=30,y=80)

def downloader():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download('C:\\Users\\ELCOT\\Desktop')
    lab3=Label(ytd,text='Downloaded',font='arial 15').place(x=180,y=210)

but=Button(ytd,text="DOWNLOAD",font='arial 15 bold',bg='red',padx=2,command=downloader).place(x=180,y=150)


ytd.mainloop()