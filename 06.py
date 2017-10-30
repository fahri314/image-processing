import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread(r'C:\Users\user\Desktop\1.png')
print(img.ndim)
print(img.shape)
plt.imshow(img)
plt.show()
