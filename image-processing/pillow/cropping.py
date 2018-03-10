#when image is cropped, rectangular region inside the image is selected and retained while everything else outside the region is removed

from PIL import Image 

img = Image.open('./savedUsingPil.png')
box = (0,0,400,700)#(left, upper, right, lower)
cropped_img = img.crop(box)
cropped_img.save('croppedImg.jpg')


