import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread(r'C:\Users\user\Desktop\1.png')

img1 = np.zeros((500,375,3))
img2 = np.zeros((500,375,3))
img3 = np.zeros((375,500,3))

for i in range(375):
    for j in range(500):
        img1[j,i,:] = img[i,j,:]
        #print(img[i,j,:])
for i in range(375):
    for j in range(500):
        img2[j,i,:] = 1 - img[i,j,:]
        #print(img[i,j,:])
for i in range(375):
    for j in range(500):
        img3[375-i-1,500-j-1,:] = img[i,j,:]
        #print(img[i,j,:])

plt.subplot(1,4,1),plt.imshow(img)
plt.subplot(1,4,2),plt.imshow(img1)
plt.subplot(1,4,3),plt.imshow(img2)
plt.subplot(1,4,4),plt.imshow(img3)

plt.show()