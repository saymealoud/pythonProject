from PIL import Image

# new_image = Image.new('L',(400,200),100)
#
# new_image.save('a.png')


# new_image = Image.new('RGB',(400,200),(255,255,0))
# new_image.save('a.png')

code_img = Image.open('images/tesseract.png')
code_img.save('./images/b.jpeg')

# piont 函数可以改变图片元素   用于对图片调色

# 图片变得更亮

# 0 黑色    255 白色 越大  越亮

# def change(x):
#     print(x)
#
#     return x * 0.2
#
#
#
# code_img = code_img.point(change)


# lambda 改写
code_img = code_img.point(lambda x: x * 0.2)

# 保存图片

code_img.save('./images/c.jpg')
