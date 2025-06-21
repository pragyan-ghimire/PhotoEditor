from tkinter import Menu
from customtkinter import *
from utils.file_utils import openImage
import cv2
from PIL import Image
from editor.utils import cv_format_image, cv_to_tk
from editor.filter import *

class App(CTk):
    def __init__(self):
        super().__init__()
        # self.geometry("600x500")
        self.after(100, lambda: self.state("zoomed"))
        self.title("Photo Editor")

        menubar = Menu(self)
        self.config(menu= menubar)

        fileMenu = Menu(
            menubar,
            tearoff= 0,
        )
        filterMenu = Menu(
            menubar,
            tearoff= 0,
        )
        editMenu = Menu(
            menubar,
            tearoff= 0,
        )
        menubar.add_cascade(label="File", menu = fileMenu)
        menubar.add_cascade(label="Filter", menu = filterMenu)
        menubar.add_cascade(label="Edit", menu = editMenu)

        fileMenu.add_command(label= "Open", command= self.load_image) 
        fileMenu.add_command(label= "Save")
        fileMenu.add_separator()
        fileMenu.add_command(label= "Exit", command=quit)

        filterMenu.add_command(label= "GrayScale", command= self.cvt_gray_scale )
        filterMenu.add_command(label= "Blur", command=self.blur_image )

        editMenu.add_command(label= "Resize" )
        editMenu.add_command(label= "Crop" )
        editMenu.add_command(label= "Flip")
        editMenu.add_command(label= "Rotate")

        self.imageLabel = CTkLabel(self, text="")
        self.imageLabel.pack(pady=20)

    def load_image(self):
        filepath = openImage()
        if filepath:
            pil_image = Image.open(filepath).convert("RGB")
            self.cv_image = cv_format_image(pil_image)
            self.show_image()
            
    def show_image(self):
        if self.cv_image is not None:
            self.tk_image = cv_to_tk(self.cv_image)
            self.imageLabel.configure(image=self.tk_image)

    def cvt_gray_scale(self):
        if self.cv_image is not None:
            self.gray_image = gray_scale(self.cv_image)
            self.tk_image = cv_to_tk(self.gray_image)
            self.imageLabel.configure(image=self.tk_image)
        
    def blur_image(self):
        if self.cv_image is not None:
            self.blur = blur(self.cv_image)
            self.tk_image = cv_to_tk(self.blur)
            self.imageLabel.configure(image=self.tk_image)
        