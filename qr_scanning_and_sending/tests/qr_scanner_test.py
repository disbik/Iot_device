from source.qr_scanner import qr_scanner
from source.qr_creator import create_qr
from scipy.ndimage import rotate
import cv2

def test_qr_scanner():
    #right qr-code
    assert qr_scanner(create_qr('test', 'rope'))[0] == 'rope'
    assert qr_scanner(create_qr('test', 'soap'))[0] == 'soap'
    assert qr_scanner(create_qr('test', 'weeee'))[0] == 'weeee'

    #wrong qr-code
    assert qr_scanner(create_qr('test', 'word1'))[0] != 'word2'
    assert qr_scanner(create_qr('test', 'word2'))[0] != 'word3'

    #no qr-code
    assert qr_scanner(cv2.imread('test_pics_and_vids/no_qr.png')) == None

def test_rotated_image():
    assert qr_scanner(rotate(create_qr('test', 'rope'), 45))[0] == 'rope'
    assert qr_scanner(rotate(create_qr('test', 'rope'), 90))[0] == 'rope'
    assert qr_scanner(rotate(create_qr('test', 'soap'), 180))[0] == 'soap'
    assert qr_scanner(rotate(create_qr('test', 'big sentence so that the qr code gets big'), 45))[0] == 'big sentence so that the qr code gets big'
