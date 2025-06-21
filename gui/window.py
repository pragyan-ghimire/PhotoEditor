from tkinter import Menu
from customtkinter import *
from controller import app_controller


class App(CTk):
    def __init__(self):
        super().__init__()
        # self.geometry("600x500")
        self.after(100, lambda: self.state("zoomed"))
        self.title("Photo Editor")

        self.grid_columnconfigure((0), weight=1) # setting frame
        self.grid_columnconfigure((1), weight=3) # image_frame
        self.grid_rowconfigure(0, weight=1)# allow vertical stretch
        self.controller = app_controller.PhotoController(self)

        self.setting_frame = CTkFrame(
            self,
            fg_color="#ff6600",
        )
        self.setting_frame.grid_columnconfigure((0), weight=1)
        self.setting_frame.grid(row=0, column=0, sticky="nsew")

        self.image_frame = CTkFrame(self, fg_color="light yellow")
        self.image_frame.grid(row=0, column=1, sticky="nsew")

        menubar = Menu(self)
        self.config(menu=menubar)

        fileMenu = Menu(
            menubar,
            tearoff=0,
        )
        filterMenu = Menu(
            menubar,
            tearoff=0,
        )
        editMenu = Menu(
            menubar,
            tearoff=0,
        )
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Filter", menu=filterMenu)
        menubar.add_cascade(label="Edit", menu=editMenu)

        fileMenu.add_command(label="Open", command=self.controller.load_image)
        fileMenu.add_command(label="Save")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=quit)

        filterMenu.add_command(label="GrayScale", command=self.controller.apply_gray)
        filterMenu.add_command(label="Blur", command=self.controller.apply_blur)

        editMenu.add_command(label="Resize")
        editMenu.add_command(label="Crop")
        editMenu.add_command(label="Flip")
        editMenu.add_command(label="Rotate")

        # self.text = CTkLabel(self.setting_frame, text="Some text")
        # self.text.pack()

        self.imageLabel = CTkLabel(self.image_frame, text="")
        self.imageLabel.pack(pady=20)

    def show_image(self, ctk_img):
        self.imageLabel.configure(image=ctk_img)
        self.imageLabel.image = ctk_img
