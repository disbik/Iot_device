# this file will be deleted later, it was created for testing purposes only
import numpy as np
import pyqrcode
import cv2

def create_qr(file_name : str, data : str) -> np.ndarray:
    url = pyqrcode.create(data)
    url.png(f'test_pics_and_vids/{file_name}.png', scale=6)
    return cv2.imread(f'test_pics_and_vids/{file_name}.png')

create_qr('test', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')