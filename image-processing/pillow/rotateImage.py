#rotating image - takes integer or float argument representing
#the degree to rotate an image and returns a new Image object 
#of the rotated image.
#The rotation is done counterclock wise
from PIL import Image

img = Image.open('./savedUsingPil.png')

#img_rot = img.rotate(90)
#img_rot.show()
img.rotate(18).show()#rotate image in number degree in counterclockwise
