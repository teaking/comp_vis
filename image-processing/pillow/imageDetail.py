from PIL import Image 

img = Image.open('../pkmon.jpg')
#file format of the source file
print(img.format)

#pixel format used by the image. Typical values are "1", "L", "RGB", or " "
print(img.mode)

#image size in pixels. size is return in 2-tuples (width, height)
print(img.size)

#color palette table, if any
print(img.palette)
