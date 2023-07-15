import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import subprocess
import os
import lasio

root=Tk()
root.title('Well Log Interpreter')
root.state('zoomed')

def Upload() :
    root.destroy()
    import welllog
        

Label(root,text='Well Log Interpreter (WLI)',font='Arial 20 bold').place(relx=0.39,rely=0.07)
# Load the foreground image using PIL
foreground_image_path = r"D:\Tkinter Python\WLI.png"  # Replace with the path to your foreground image
foreground_image = Image.open(foreground_image_path)

 # Set the maximum width and height for the foreground image
max_width = 400
max_height = 400

# Resize the foreground image while maintaining aspect ratio
foreground_image.thumbnail((max_width, max_height))
# Create a PhotoImage object for the foreground image
# foreground_photo = ImageTk.PhotoImage(foreground_image)

# canvas = tk.Canvas(root, width=max_width, height=max_height)
# canvas.pack()

foreground_photo = ImageTk.PhotoImage(foreground_image)

image_label = tk.Label(root, image=foreground_photo)
image_label.place(relx=0.42,rely=0.5,anchor=tk.CENTER)


Button(root,text='Upload',command=Upload,fg='purple',font='calibri 17',relief=RIDGE,highlightcolor='black').place(relx=0.575,rely=0.27)
Label(root,text='(please upload the file in .Las Format)',font='calibri 13').place(relx=0.575,rely=0.34)


Label(root,text=' Well Log Interpreter is a well log Interpretation software developed\n by Daksh Joshi , Meet Chaklasiya & Pariket Pansara final year petroleum\n engineering students from Pandit Deendayal Energy University.\n This software provides users with free access to extract standard well\n logging plots from .las fil formats, which are commonly used to store\n data collected by well logging tools in real-time, with its user-friendly\n interface and efficient data extraction capabilities. Well Logging\n Interpreter simplifies the process of analyzing and interpreting\n well log data for petroleum engineering professionals and research\n alike.',justify=LEFT,font='calibri 13').place(relx=0.575,rely=0.47)

Label(root,text='Developed by Meet Chaklasiya , Daksh Joshi & Pariket Pansara',font='calibri 15 bold').place(relx=0.35,rely=0.89)
root.mainloop()