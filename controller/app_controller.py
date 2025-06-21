from PIL import Image
from utils.file_utils import openImage, saveImage
from editor.utils import cv_format_image, cv_to_tk
from editor import filter, transform
import cv2

INTERPOLATION_MAP = {
    "INTER_AREA": cv2.INTER_AREA,
    "INTER_CUBIC": cv2.INTER_CUBIC,
    "INTER_LINEAR": cv2.INTER_LINEAR
}
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
    
    def save_image(self):
        if self.cv_img is not None:
            saveImage(self.cv_img)

    def apply_gray(self):
        if self.cv_img is not None:
            self.cv_img = filter.gray_scale(self.cv_img)
            self._refresh_view()

    def apply_blur(self):
        if self.cv_img is not None:
            self.cv_img = filter.blur(self.cv_img)
            self._refresh_view()
    
    def apply_resize(self):
        if self.cv_img is not None:
            width = int(self.view.resize_width_entry.get())
            height = int(self.view.resize_height_entry.get())
            selected_interpolation = self.view.interpolation_menu.get()
            interpolation = INTERPOLATION_MAP[selected_interpolation]
            self.cv_img = transform.resize(self.cv_img, (width, height),interpolation )
            self._refresh_view()

    def apply_flip(self):
        if self.cv_img is not None:
            self.cv_img = transform.flip(self.cv_img, value= int(self.view.flip_value_menu.get()))
            self._refresh_view()
    
    def apply_rotate(self):
        if self.cv_img is not None:
            self.cv_img = transform.rotate(self.cv_img, angle= int(self.view.rotate_angle_entry.get()))
            self._refresh_view()
    
    def apply_crop(self):
        if self.cv_img is not None:
            self.cv_img = transform.crop(
                self.cv_img, 
                from_row= int(self.view.from_row_entry.get()),
                to_row= int(self.view.to_row_entry.get()),
                from_col= int(self.view.from_col_entry.get()),
                to_col= int(self.view.to_col_entry.get()),
                )
            self._refresh_view()
    
    def _refresh_view(self):
        tk_img = cv_to_tk(self.cv_img)
        self.view.show_image(tk_img)
