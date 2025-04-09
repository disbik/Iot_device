from source.blockchain_info_sender import create_trans_contract, send_transaction
from source.qr_scanner import qr_scanner
from secure.sentsec import *
from web3 import Web3
import numpy as np
import serial

# параметры для чтения изображений
ser = serial.Serial('/dev/ttyUSB0', 115200)
last_info = ''
width = 160
height = 120

# параметры для отправки данных на блокчейн
w3 = Web3(Web3.HTTPProvider("https://bsc-testnet.publicnode.com"))

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


if __name__ == "__main__":
    while True:
        try:
            img = read_frame()
        except Exception as e:
            print(f"Ошибка чтения кадра: {e}")
            continue

        product_id = qr_scanner(img)[0]

        if product_id != last_info and product_id:
            tx = create_trans_contract(product_id, CONTRACT_ADDRESS, SENDER_ADDRESS, w3)
            send_transaction(tx, PRIVATE_KEY, w3)
        last_info = product_id