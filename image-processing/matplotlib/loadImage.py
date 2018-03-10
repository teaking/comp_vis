import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('./a8fd34f62e227159ab7cc89004715cf7--pokemon-funny-pokemon-stuff.jpg')
#print(img)
#imgplot = plt.imshow(img)
lum_img = img[:,:,0] #get r and g and turn blue to 0
#plt.imshow(lum_img)
imgplt = plt.imshow(lum_img)
imgplt.set_cmap('nipy_spectral')#c_map -> color map
plt.show()
