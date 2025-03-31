import serial
import numpy as np
import cv2

ser = serial.Serial('COM5', 115200)  # Изменить порт в зависимости от подключения Arduino Uno

# Разрешение камеры
width = 160
height = 120
frame_count = 0


def read_frame():
    frame = np.zeros((height, width), dtype=np.uint8)
    while True:
        if ser.read() == b'\x00':
            break
    for y in range(height):
        for x in range(width):
            pixel = ord(ser.read())
            frame[y, x] = pixel
    return frame


def show_frame(frame):
    print("Reading frame...")
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return False
    return True


while True:
    frame = read_frame()
    frame_count += 1
    print(f'Frame {frame_count} read successfully.')
    if not show_frame(frame):
        break

ser.close()
cv2.destroyAllWindows()
