from PIL import Image, ImageFilter, ImageDraw, ImageFont

img = Image.open('b.png')
d = ImageDraw.Draw(img)
fnt = ImageFont.truetype("comicbd.ttf", 25)
d.text((60, img.size[1]/2), "Hello world!!!", font=fnt, fill=(255, 255, 255))
img.save('bb.png')


# print(img.size)
# print(img.format)

# print(img.mode)

# filtered = img.filter(ImageFilter.BLUR)
# filtered.save('blurred.png', 'png')

# filtered = img.convert('L')
# filtered.save('gray.png', 'png')

# filtered = img.rotate(180)
# filtered.save('rote.png', 'png')

# filtered = img.resize((400,400))
# filtered.save('rez.png', 'png')

# box = (100, 100, 400, 400)
# region = img.crop(box)
# region.save('crop.png', 'png')

# img.thumbnail((400, 400))
# img.save('thumb.png', 'png')
