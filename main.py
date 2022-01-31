from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import os



Folder_Name = ""

#dosya lokasyonu
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()

    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Lütfen Dosya Yolunu Seçiniz!",fg="red")  

def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()    

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
            output = select.download(Folder_Name)
            base, ext = os.path.splitext(output)
            to_mp3 = base + '.mp3'
            os.rename(output, to_mp3)
            ytdError.config(text="İndirme Tamamlandı!",fg='green')
        else:
            ytdError.config(text="Linki Yeniden Yapıştırınız!", fg="red")

    if(choice != choices[2]):
        #download function
        select.download(Folder_Name)
        ytdError.config(text="İndirme Tamamlandı!",fg='green')

root = Tk()
root.title("YTD Downloader")
root.geometry("500x300") 
root.columnconfigure(0,weight=1)

#ytd link konumu
ytdLabel = Label(root,text="Videonun Linkini Giriniz", font=("jost",15))
ytdLabel.grid()

#pencere 
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable =ytdEntryVar)
ytdEntry.grid()


#hata mesajı
ytdError = Label(root,text="Video Linkini Giriniz!",fg="red",font=("jost",10))
ytdError.grid(pady=5,padx=0)

#kaydedilen dosya konumunu sor
saveLabel = Label(root,text="Video Dosyasının Kayıt Edileceği Konumu Seçiniz!",font=("jost",15,"bold"))
saveLabel.grid(pady=5,padx=0)

#dosyayı kaydet btn
saveEntry = Button(root,width=20,bg="red",fg="white",text="Dosya Yolunu Seçiniz",command=openLocation)
saveEntry.grid(pady=5,padx=0)

locationError = Label(root,text="Dosya Yolu Hatalı",fg="red",font=("jost",10))
locationError.grid()

#indirme kalitesi
ytdQuality = Label(root,text="Kaliteyi Seçiniz",font=("jost",15))
ytdQuality.grid(pady=5,padx=0)

#combobox
choices = ["144p", "720p", "Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid(pady=5,padx=0)

#indirme btn
downloadbtn = Button(root,text="İndir",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid(pady=10,padx=0)

#developer label
developerlabel = Label(root,text="Developer Knetic!",font=("jost,15"))
developerlabel.grid(padx= 0, pady= 50)

root.mainloop()
