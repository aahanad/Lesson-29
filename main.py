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
screen.mainloop()