import matplotlib.pyplot as plt
import numpy as np

img_1 = plt.imread(r'C:\Users\user\Desktop\eleven.png')
img_2 = img_1
plt.imshow(img_2)
plt.show()

img_3 = np.zeros((img_2.shape[0:2]))

thresold = 100
for i in range(img_2.shape[0]):
    for j in range(img_2.shape[1]):
        n = img_2[i,j,0]/3 + img_2[i,j,1]/3 + img_2[i,j,2]/3
        img_3[i,j] = n
        if n > thresold:
            img_3[i,j] = 255
        else:
            img_3[i,j] = 0

plt.subplot(1,2,1),plt.imshow(img_2)
plt.subplot(1,2,2),plt.imshow(img_3,plt.cm.binary)
plt.show()