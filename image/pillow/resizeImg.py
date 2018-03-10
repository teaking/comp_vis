#resizing image 
from PIL import Image 

img = Image.open('./savedUsingPil.png')
new_img = img.resize((400,400))#resizing image 
new_img.save('newImageSize.jpg')

