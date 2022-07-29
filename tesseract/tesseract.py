import cv2
import pytesseract

from PIL import Image
from pytesseract import *

pytesseract.pytesseract.tesseract_cmd = R'C:/Program Files/Tesseract-OCR/tesseract'

filename = "C:/Users/jhryu/Downloads/PySceneDetect-main/PySceneDetect/result/scenes/vlog2/vlog_Gyeongju-Scene-047-02.jpg"
image = Image.open(filename)
text = image_to_string(image, lang="kor")

with open("sample.txt", "w") as f:
    f.write(text)
