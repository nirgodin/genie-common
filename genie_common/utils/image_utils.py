import cv2
import numpy as np


def decode_image(image_bytes: bytes) -> np.ndarray:
    array = np.fromstring(image_bytes, np.uint8)
    return cv2.imdecode(array, cv2.IMREAD_COLOR)
