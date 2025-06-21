from tkinter import Menu
from customtkinter import *

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
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

        fileMenu.add_command(label= "Open") 
        fileMenu.add_command(label= "Save")
        fileMenu.add_separator()
        fileMenu.add_command(label= "Exit", command=quit)

        filterMenu.add_command(label= "GrayScale" )
        filterMenu.add_command(label= "Blur" )

        editMenu.add_command(label= "Resize" )
        editMenu.add_command(label= "Crop" )
        editMenu.add_command(label= "Flip")
        editMenu.add_command(label= "Rotate")


    #     self.upload = CTkButton(self, text= "Upload", command= self.upload_click)
    #     self.upload.pack()

    # def upload_click():
    #     print("Upload clicked")

app = App()
app.mainloop()
