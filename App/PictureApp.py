from tkinter import *
# use pip to install Pillow for this to work
from PIL import ImageTk, Image 

# you can call this whatever you want
pic = 1

win = Tk()

#make sure to use the geometry of your photos +100 on both axis
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

#if you have more than 2 files you might want to make it a list
img = PhotoImage(file="Subscribe.png")
img2 = PhotoImage(file="Like.png")

    
change = Button(win,text="Next",command=Change)
change.pack()
image_container =canvas.create_image(0,0, anchor="nw",image=img)

win.mainloop()
