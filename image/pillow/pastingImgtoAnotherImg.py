#pasting image on top of another image
from PIL import Image 

img = Image.open('./savedUsingPil.png')
logo = Image.open('./pkmn-logo.png')
logo = logo.convert("RGBA")#converting image with alpha channel
logo.thumbnail((200,200))#resizing image
cp_img = img.copy() # copying image 
pos = ((cp_img.width - logo.width),(cp_img.height - logo.height))

cp_img.paste(logo, pos, logo) # pasting image on top of another image
#pos can either be 2 tuple - giving the upper left corner
#or 4 tuple defining the left, upper, right and lower pixel coordinate
#or none (same as (0,0))
cp_img.save('pasteImg.png')
