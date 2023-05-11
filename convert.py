from PIL import Image
import pytesseract
import pathlib
from googletrans import Translator
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


text = ""

# ans = input("Do you want the photos to be translated into Persion?(y/n): ")
for path in pathlib.Path("persion_pics").iterdir():
    print(path)
