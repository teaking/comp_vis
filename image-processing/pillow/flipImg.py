#flip image to get their mirror version. Done using the 
#transpose() function. 
#transpose() function takes one of the following options
#PIL.Image.FLIP_LEFT_RIGHT
#PIL.Image.FLIP_TOP_BOTTOM
#PIL.Image.ROTATE_90
#PIL.Image.ROTATE_180
#PIL.Image.ROTATE_270
#PIL.Image.TRANSPOSE

from PIL import Image
img = Image.open('./savedUsingPil.png')
img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)#flip image - mirror img 
img_flip.show()
img2 = img.transpose(Image.TRANSPOSE)#Flip image
img2.show()


