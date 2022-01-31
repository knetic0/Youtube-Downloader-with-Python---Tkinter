from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube 

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
          
        else:
            ytdError.config(text="Linki Yeniden Yapıştırınız!", fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="İndirme Tamamlandı!")

root = Tk()
root.title("YTD Downloader")
root.geometry("350x400") 
root.columnconfigure(0,weight=1)

#ytd link konumu
ytdLabel = Label(root,text="Videonun Linkini Giriniz", font=("jost",15))
ytdLabel.grid()

#pencere 
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable =ytdEntryVar)
ytdEntry.grid()

#hata mesajı
ytdError = Label(root,text="Hata!",fg="red",font=("jost",10))
ytdError.grid()

#kaydedilen dosya konumunu sor
saveLabel = Label(root,text="Video Dosyasını Kaydet",font=("jost",15,"bold"))
saveLabel.grid()

#dosyayı kaydet btn
saveEntry = Button(root,width=10,bg="red",fg="white",text="Dosya Yolunu Seçiniz",command=openLocation)
saveEntry.grid()

#hata mesaj lokasyonu
locationError = Label(root,text="Dosya Yolu Hatalı",fg="red",font=("jost",10))
locationError.grid()

#indirme kalitesi
ytdQuality = Label(root,text="Kaliteyi Seçiniz",font=("jost",15))
ytdQuality.grid()

#combobox
choices = ["144p", "720p", "Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#indirme btn
downloadbtn = Button(root, text="İndir",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

#developer label
developerlabel = Label(root,text="Mehmet Solak",font=("jost,15"))
developerlabel.grid()

root.mainloop()
