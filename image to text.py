from PIL import Image
from pytesseract import *
#Define path to process images e.g. 'C:\Users/'
img_path = r'C:\Users/'
#Define path to tessaract.exe e.g. 'C:\Program Files\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = r'C:\Program Files'
pytesseract.tesseract_cmd = tessdata_dir_config
language = 'grc'

def process_image(iamge_name, lang_code, tessdata_dir_config):
    return pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)

def print_data(data):
    print(data)

def output_file(filename, data):
    file = open(filename, "w+")
    file.write(data)
    file.close()

def main():
    data_gr = process_image(img_path, language, tessdata_dir_config)
    print_data(data_gr)
    #output_file('my_ocr', data_gr)

if  __name__ == '__main__':
    main()