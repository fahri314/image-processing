import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread(r'C:\Users\user\Desktop\1.png')

img2 = img[1:375:4,:,:]

plt.subplot(1,2,1),plt.imshow(img)
plt.subplot(1,2,2),plt.imshow(img2)
plt.show()