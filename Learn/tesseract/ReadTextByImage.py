import pytesseract

from PIL import Image

img = Image.open("./images/tesseract.png")

# 使用导入的 pytesseract  进行识别

text = pytesseract.image_to_string(img)

print(text)
