from PIL import Image
from pytesseract import pytesseract
import os

#Define path to save images e.g. 'C:\Users/'
path_to_images = r'C:\Users/'

#Define path to tessaract.exe e.g. 'C:\Program Files\Tesseract-OCR\tesseract.exe'
path_to_tesseract = r'C:\Program Files/'


#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file name in the folder
    for file_name in file_names:
        #Open image with PIL
        img = Image.open(path_to_images + file_name)

        #Extract text from image
        text = pytesseract.image_to_string(img,lang='grc')

        with open(file_name+'_text.txt', 'w') as f:
            f.write(text)
            f.close
        #   print(text)