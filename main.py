from tkinter import*
from tkinter import PhotoImage
from PIL import Image,ImageTk
screen=Tk()
screen.title("word game")
screen.geometry("468x837")
image=Image.open("christmas1.PNG")
image=ImageTk.PhotoImage(image)
imageLabel=Label(screen,image=image)
imageLabel.place(relwidth=1,relheight=1)
title=Label(screen,text="Jumbled word game  -christmas edition-",bg="plum1",fg="SpringGreen2",font=("Brush Script",19))
title.place(x=6,y=100)
good=["Santa Claus","elves", "Rudolph", "Jack Frost","carols","tree","gingerbread","stockings","presents","holly","tinsel","mistletoe",]
bad=["talna saucs","eselv","olhrudp","cjka trfso","scoarl","eert","gairdbrnege","skingosct","retpness","lyohl","isntle","setiltemo"]
guess=Entry()
guess.place(x=190,y=230)
screen.mainloop()
