from PIL import Image, ImageFilter

img = Image.open('./images/back.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.convert('L')
# # crooked = filtered_img.rotate(90)
# # crooked = filtered_img.resize((500, 500))

# # crooked.save("grey.png", "png")

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save('region.png', 'png')
# region.show()

# new_img = img.resize((400, 400))
img.thumbnail((400, 200))
print(img.size)
img.save('thumb.jpg')
