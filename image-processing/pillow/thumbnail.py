#resize(), it doesnot account for the image's Aspect ration, hence the image might end up looking squished or stretched

#thumbnail() keeps the images aspect ration when resized
from PIL import Image 

img = Image.open('./savedUsingPil.png')
img.thumbnail((400,400))#resizing, keeping aspect ratio
img.save('saveThumbnail.jpg') #thumbnail edits original image
print(img.size)
