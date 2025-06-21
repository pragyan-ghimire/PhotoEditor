from tkinter import Menu
from customtkinter import *
from controller import app_controller


class App(CTk):
    # showResize, showCrop, showRotate, showFlip = False, False, False, False


    def __init__(self):
        super().__init__()
        # self.geometry("600x500")
        self.after(100, lambda: self.state("zoomed"))
        self.title("Photo Editor")

        # self.grid_columnconfigure((0), weight=1) # setting frame
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

        editMenu.add_command(label="Resize", command= self.resize_clicked)
        editMenu.add_command(label="Crop", command= self.crop_clicked)
        editMenu.add_command(label="Flip", command= self.filp_clicked)
        editMenu.add_command(label="Rotate", command= self.rotate_clicked)

        # self.text = CTkLabel(self.setting_frame, text="Some text")
        # self.text.pack()

        self.imageLabel = CTkLabel(self.image_frame, text="")
        self.imageLabel.pack(pady=20)



    def resize_clicked(self):
        # print("resize from menu clicked")
        # print(self.imageLabel.cget("image"))
        # self.showResize, self.showCrop, self.showRotate, self.showFlip = True, False, False, False
        self.clear_setting_frame()
        if self.imageLabel.cget("image") is not None:
            self.resize_width_label = CTkLabel(
                self.setting_frame,
                text="Width:",
                font=("Arial", 24),      
                padx= 24,
                pady = 24
                )
            self.resize_width_label.grid(row= 0, column= 0, sticky= "w")

            self.resize_width_entry = CTkEntry(
                self.setting_frame,
                font=("Arial", 24),
            )
            self.resize_width_entry.grid(row= 0, column= 1, sticky= "w")

            self.resize_height_label = CTkLabel(
                self.setting_frame,
                text="Height:",
                font=("Arial", 24),
                padx= 24,
                pady= 24,
                )
            self.resize_height_label.grid(row= 1, column= 0, sticky= "w")

            self.resize_height_entry = CTkEntry(
                self.setting_frame,
                font=("Arial", 24)
            )
            self.resize_height_entry.grid(row= 1, column= 1, sticky= "w")

            self.resize_interpolation_label = CTkLabel(
                self.setting_frame,
                text="Interpolation:",
                font=("Arial", 24),
                padx= 24,
                pady= 24,
                )
            self.resize_interpolation_label.grid(row= 2, column= 0, sticky= "w")

            self.interpolation_menu = CTkOptionMenu(
                self.setting_frame,
                values=["INTER_AREA", "INTER_CUBIC","INTER_LINEAR"],
                font=("Arial", 24),
                # command=optionmenu_callback
                )
            self.interpolation_menu.set("INTER_AREA")
            self.interpolation_menu.grid(row= 2, column= 1,sticky= "w")

            self.resize_button = CTkButton(
                self.setting_frame, 
                text="Resize",
                font=("Arial", 24),
                command= self.controller.apply_resize
                )
            self.resize_button.grid(row=3, column = 0)
    
    # once cropped then if again cropping is applied, it applies to already cropped image.
    def crop_clicked(self):

        self.clear_setting_frame()
        if self.imageLabel.cget("image") is not None:

            # select row
            self.from_row_label = CTkLabel(
                self.setting_frame,
                text="From row:",
                font=("Arial", 24),      
                padx= 24,
                pady = 24
                )
            self.from_row_label.grid(row= 0, column= 0, sticky= "w")

            self.from_row_entry = CTkEntry(
                self.setting_frame,
                font=("Arial", 24),
            )
            self.from_row_entry.grid(row= 0, column= 1, sticky= "w")

            self.to_row_label = CTkLabel(
                self.setting_frame,
                text="To row:",
                font=("Arial", 24),      
                padx= 24,
                pady = 24
                )
            self.to_row_label.grid(row= 1, column= 0, sticky= "w")

            self.to_row_entry = CTkEntry(
                self.setting_frame,
                font=("Arial", 24),
            )
            self.to_row_entry.grid(row= 1, column= 1, sticky= "w")

            # select col
            self.from_col_label = CTkLabel(
                self.setting_frame,
                text="From col:",
                font=("Arial", 24),      
                padx= 24,
                pady = 24
                )
            self.from_col_label.grid(row= 2, column= 0, sticky= "w")

            self.from_col_entry = CTkEntry(
                self.setting_frame,
                font=("Arial", 24),
            )
            self.from_col_entry.grid(row= 2, column= 1, sticky= "w")

            self.to_col_label = CTkLabel(
                self.setting_frame,
                text="To col:",
                font=("Arial", 24),      
                padx= 24,
                pady = 24
                )
            self.to_col_label.grid(row= 3, column= 0, sticky= "w")

            self.to_col_entry = CTkEntry(
                self.setting_frame,
                font=("Arial", 24),
            )
            self.to_col_entry.grid(row= 3, column= 1, sticky= "w")

            # crop button
            self.crop_button = CTkButton(
                self.setting_frame, 
                text="Crop",
                font=("Arial", 24),
                command= self.controller.apply_crop
                )
            self.crop_button.grid(row=4, column = 0)

    def filp_clicked(self):
        # print("filp from menu clicked")
        # print(self.imageLabel.cget("image"))
        # self.showResize, self.showCrop, self.showRotate, self.showFlip = False, False, False, True
        self.clear_setting_frame()
        if self.imageLabel.cget("image") is not None:
            self.flip_value_label = CTkLabel(
                self.setting_frame,
                text="Value:",
                font=("Arial", 24),      
                padx= 24,
                pady = 24
                )
            self.flip_value_label.grid(row= 0, column= 0, sticky= "w")

            self.flip_value_menu = CTkOptionMenu(
                self.setting_frame,
                values=["0", "1","-1"],
                font=("Arial", 24),
                )
            self.flip_value_menu.set("1")
            self.flip_value_menu.grid(row= 0, column= 1,sticky= "w")

            self.flip_button = CTkButton(
                self.setting_frame, 
                text="Flip",
                font=("Arial", 24),
                command= self.controller.apply_flip
                )
            self.flip_button.grid(row=1, column = 0)


            self.flip_value_label = CTkLabel(
                self.setting_frame,
                text="0 for vertical flip",
                font=("Arial", 16),      
                padx= 24,
                pady = 24
                )
            self.flip_value_label.grid(row= 2, column= 0, sticky= "w")

            self.flip_value_label = CTkLabel(
                self.setting_frame,
                text="1 for horizontal flip",
                font=("Arial", 16),      
                padx= 24,
                pady = 24
                )
            self.flip_value_label.grid(row= 3, column= 0, sticky= "w")

            self.flip_value_label = CTkLabel(
                self.setting_frame,
                text="-1 for vertical and horizontal flip",
                font=("Arial", 16),      
                padx= 24,
                pady = 24
                )
            self.flip_value_label.grid(row= 4, column= 0, sticky= "w")
    
    # Todo: rotating is clipping the image
    def rotate_clicked(self):
        # print("filp from menu clicked")
        self.clear_setting_frame()

        if self.imageLabel.cget("image") is not None:

            self.rotate_angle_label = CTkLabel(
                self.setting_frame,
                text="Angle:",
                font=("Arial", 24),      
                padx= 24,
                pady = 24
                )
            self.rotate_angle_label.grid(row= 0, column= 0, sticky= "w")

            self.rotate_angle_entry = CTkEntry(
                self.setting_frame,
                font=("Arial", 24),
            )
            self.rotate_angle_entry.grid(row= 0, column= 1, sticky= "w")

            self.rotate_button = CTkButton(
                self.setting_frame, 
                text="Rotate",
                font=("Arial", 24),
                command= self.controller.apply_rotate
                )
            self.rotate_button.grid(row=1, column = 0)



    def clear_setting_frame(self):
        for widget in self.setting_frame.winfo_children():
            widget.destroy()



        
    def show_image(self, ctk_img):
        self.imageLabel.configure(image=ctk_img)
        self.imageLabel.image = ctk_img
