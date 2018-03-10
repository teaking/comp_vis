#drawing on the image using the ImageDraw module. 
#it allows to draw lines, points, ellipses, rectangles, arcs, bitmaps, chords, pieslices, polygon, shapes and text

from PIL import Image, ImageDraw

blank_img = Image.new('RGBA',(400,300),'black')#create new iamge with given dimension
img_draw = ImageDraw.Draw(blank_img)#draw newly create image using ImageDraw module
img_draw.rectangle((70, 50,270,200), outline='red', fill='blue')#drawing rectangle on the image in provided dimension with red outline 
img_draw.text((10,250), 'Hello World',fill='green')#drawing text on the image
blank_img.show()
