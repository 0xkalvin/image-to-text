from PIL import Image
from pytesseract import image_to_string
import urllib
import os, os.path

def get_text_from_image(url):
    id = str(len([name for name in os.listdir('.') if os.path.isfile(name)]) + 1 ) 
    urllib.request.urlretrieve(url, id + ".jpg")
    text = image_to_string(Image.open(id + ".jpg"), lang='eng')
    return text



text = get_text_from_image("http://d2jaiao3zdxbzm.cloudfront.net/wp-content/uploads/figure-65.png")
print(text)
