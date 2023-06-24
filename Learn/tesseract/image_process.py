import pytesseract

from PIL import Image

img = Image.open('./images/tesseract.png')

# 二值化
img = img.point(lambda x: 0 if x < 126 else 255)

img.save('./images/test_backgroud.png')

text = pytesseract.image_to_string(img)

print(text)
