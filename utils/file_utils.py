from tkinter import filedialog, messagebox
import cv2

def openImage():
    filepath = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[
            ("PNG Image", "*.png"),
            ("JPG Image", "*.jpg"),
        ]
    )
    if not filepath:
        messagebox.showinfo("Notification", "No image was selected.")
        return None
    return filepath

def saveImage(cv_image):
    file = filedialog.asksaveasfilename(
        defaultextension= ".jpg",
        filetypes= [
            ("JPG Image", "*.jpg"),
            ("PNG Image", "*.png"),
        ]
    ) 
    if file:
        cv2.imwrite(file, cv_image)