from PIL import Image
from pytesseract import image_to_string
import urllib
import os, os.path

def get_text_from_image(url):
    id = len([name for name in os.listdir('.') if os.path.isfile(name)])
    urllib.request.urlretrieve(url, "0000000"+ str(id) +".jpg")
    text = image_to_string(Image.open("0000000"+ str(id) +".jpg"), lang='eng')
    return text



text = get_text_from_image("http://d2jaiao3zdxbzm.cloudfront.net/wp-content/uploads/figure-65.png")
print(text)
