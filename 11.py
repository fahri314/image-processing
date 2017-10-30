import matplotlib.pyplot as plt
import numpy as np
import scipy

img_1 = plt.imread(r'C:\Users\user\Desktop\1.png')
print(img_1.ndim,img_1.shape)
plt.imshow(img_1[:,:,2]+10)
plt.show()