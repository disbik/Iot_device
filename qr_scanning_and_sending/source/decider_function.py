import cv2
from source.quality_enchancers import preprocess_image
from source.qr_scanner import qr_scanner

def decider(cap: cv2.VideoCapture):
    frame_size = (640, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Не удалось захватить кадр")
            break

        val, new_image = qr_scanner(preprocess_image(frame))

        if val: print(*val)

        cv2.waitKey(1)

    return True