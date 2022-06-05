from tkinter import *
from PIL import ImageTk, Image

pic = 1

win = Tk()
win.geometry("700x500")
def Change():
    global pic
    if pic == 1:
        canvas.itemconfig(image_container,image=img)
        pic = 2
    else:
        canvas.itemconfig(image_container,image=img2)
        pic = 1


canvas = Canvas(win, width=600, height=400)
canvas.pack()
canvas.place(anchor='center', relx=0.5, rely=0.5)


img = PhotoImage(file="Subscribe.png")
img2 = PhotoImage(file="Like.png")

    
change = Button(win,text="Next",command=Change)
change.pack()
image_container =canvas.create_image(0,0, anchor="nw",image=img)

win.mainloop()