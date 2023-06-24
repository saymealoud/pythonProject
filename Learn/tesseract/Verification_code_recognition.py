import pytesseract

from PIL import Image

img = Image.open('./images/v.png')

# 背景色变成黑白
img = img.convert('L')

img.save('./images/v-1.png')

# 降噪处理  二值化
img = img.point(lambda x: 0 if x < 200 else 255)

img.save('./images/v-2.png')

text = pytesseract.image_to_string(img)
print(text)
