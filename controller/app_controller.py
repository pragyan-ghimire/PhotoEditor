from PIL import Image
from utils.file_utils import openImage
from editor.utils import cv_format_image, cv_to_tk
from editor import filter

class PhotoController:
    def __init__(self, view):
        self.view = view        # the window / widgets (View)
        self.cv_img = None      # model state

    def load_image(self):
        path = openImage()
        if path:
            pil_image = Image.open(path).convert("RGB")
            self.cv_img = cv_format_image(pil_image)
            self._refresh_view()

    def apply_gray(self):
        if self.cv_img is not None:
            self.cv_img = filter.gray_scale(self.cv_img)
            self._refresh_view()

    def apply_blur(self):
        if self.cv_img is not None:
            self.cv_img = filter.blur(self.cv_img)
            self._refresh_view()
    
    def _refresh_view(self):
        tk_img = cv_to_tk(self.cv_img)
        self.view.show_image(tk_img)
