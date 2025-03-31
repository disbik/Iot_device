import cv2
import numpy
import zlib
import base64


def qr_scanner(img : numpy.ndarray):
    det = cv2.QRCodeDetector()
    val, pts, st_code = det.detectAndDecode(img)

    if pts is not None and len(pts) > 0:
        pts = pts[0].astype(int)
        for i in range(4):
            cv2.line(img, tuple(pts[i]), tuple(pts[(i + 1) % 4]), (0, 0, 255), 3)
        if val:
            try:
                val = zlib.decompress(base64.b64decode(val)).decode('utf-8').split('||')
            except:
                val = [val]
            if len(val) == 3:
                cv2.putText(img, "Receiver: " + val[2], (pts[0][0], pts[0][1] - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255, 255, 255), 4)
                cv2.putText(img, "Receiver: " + val[2], (pts[0][0], pts[0][1] - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                cv2.putText(img, "Sender: " + val[1], (pts[0][0], pts[0][1] - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 4)
                cv2.putText(img, "Sender: " + val[1], (pts[0][0], pts[0][1] - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 0), 2)
                cv2.putText(img, "Item id: " + val[0], (pts[0][0], pts[0][1] - 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 4)
                cv2.putText(img, "Item id: " + val[0], (pts[0][0], pts[0][1] - 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 0), 2)
    cv2.imshow('QR Code Detection', img)

    return val
