# Install tkinter and Pillow with pip
from tkinter import *
from PIL import ImageTk, Image 

# Initialize images and current image
images = [PhotoImage(file="Subscribe.png"),PhotoImage(file="Like.png")]
currentImage = 0

win = Tk()

# Make sure to use the aspect ratio of your images in pixels and add 100 pixels on both axis for margin
win.geometry("700x500")

# Updating Images
def ChangeImage():
    global currentImage
    if currentImage == len(images)-1:
        currentImage = 0
    else:
        currentImage += 1
    canvas.itemconfig(image_container,image=images[currentImage])
    
# Initialize Canvas to render images
canvas = Canvas(win, width=600, height=400)
canvas.pack()
canvas.place(anchor='center', relx=0.5, rely=0.5)

change = Button(win,text="Next",command=ChangeImage)
change.pack()
image_container =canvas.create_image(0,0, anchor="nw",image=images[currentImage])

win.mainloop()
