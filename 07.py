import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread(r'C:\Users\user\Desktop\1.png')
print(img.shape)

img[:,100,:].max()
img2 = img[1:375:4,:,:]     # y bileşeninde 1 den 375 e 2 şer atlayarak git
img3 = img[:,1:500:2,:]
plt.imshow(img2)
plt.show()



#(375, 500, 3)