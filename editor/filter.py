import cv2

def gray_scale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def blur(image):
    return cv2.GaussianBlur(image, (3,3), cv2.BORDER_DEFAULT)