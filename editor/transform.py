import cv2

def resize(image, dimensions, interpolation):
    return cv2.resize(image, dimensions, interpolation)

def crop(image, from_row, to_row, from_col, to_col):
    return image[from_row:to_row, from_col:to_col]

def rotate(image, angle, rotPoint = None):
    (height, width) = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height //2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)
    return cv2.warpAffine(img, rotMat, dimensions)

def flip(image, value):
    return cv2.flip(image, value)