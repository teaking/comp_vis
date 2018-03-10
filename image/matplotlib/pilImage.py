#converting  image to numpy array which can be used with matplotlin functions
from PIL import Image 
import matplotlib.pyplot as plt
import numpy as np

img = Image.open('./pkmon.jpg')
#image size
width, height = img.size
print(width, height)
pix = np.array(img)#changing image to matrix form
#print(pix)

imgplt = plt.imshow(img)
plt.hist(pix)
plt.show()
