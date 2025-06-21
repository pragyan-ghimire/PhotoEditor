import cv2
from PIL import Image
import numpy as np
from customtkinter import CTkImage

def cv_format_image(pil_image):
    image_np = np.array(pil_image)
    image = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    return image

def cv_to_tk(cv_image, size = None):
    rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)

    if size is None:
        size = pil_image.size 

    return CTkImage(light_image=pil_image, size=size)