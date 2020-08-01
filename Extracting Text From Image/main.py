import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

value=Image.open('quotes.jpg')
text= pytesseract.image_to_string(value, config='')

filename=text[0:10]+'.txt'
f= open(filename,"w+")
f.write(text)
