import cv2


def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    upscaled = cv2.resize(gray, (640, 480), interpolation=cv2.INTER_CUBIC)
    warped = cv2.GaussianBlur(upscaled, (5, 5), 0)

    return warped
