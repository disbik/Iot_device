from source.decider_function import decider
import cv2

def test_qr_scanner():
    # showing nothing
    assert decider(cv2.VideoCapture('test_pics_and_vids/2025-01-16 17-03-42.mkv', 0))
    #just showing the qr-code
    assert decider(cv2.VideoCapture('test_pics_and_vids/2025-01-16 17-04-33.mkv', 0))
    #rotating the camera and moving it around
    assert decider(cv2.VideoCapture('test_pics_and_vids/2025-01-16 17-06-22.mkv', 0))