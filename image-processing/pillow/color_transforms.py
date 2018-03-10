#convert image between different pixel representation using the convert() method. convert() supports L(greyscale), RGB and CMYK modes

from PIL import Image
img = Image.open('./savedUsingPil.png')
l_img = img.convert('L')
l_img.show()
