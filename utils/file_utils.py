from tkinter import filedialog, messagebox

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
