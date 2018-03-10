#saving image using PIL module
from PIL import Image 

img = Image.open('../pkmon.jpg')
# saving image
img.save('savedUsingPil.png', 'PNG')#saving image in different format
