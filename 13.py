# 12 nin düzenli hali
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imsave

def convert(image_1):                  # rgb to gray level
    img_1 = plt.imread(image_1)
    img_2 = np.zeros((img_1.shape[0],img_1.shape[1]))
    for i in range (img_1.shape[0]):
        for j in range (img_2.shape[1]):
            img_2[i,j] = img_1[i,j,0]/3 + img_1[i,j,1]/3 + img_1[i,j,2]/3
            
    imsave(r'C:\Users\user\Desktop\gray.png', img_2)
    plt.subplot(1,2,1)
    plt.imshow(img_1)
    plt.subplot(1,2,2)
    plt.imshow(img_2,cmap = 'gray')
    plt.show()
convert(r'C:\Users\user\Desktop\eleven.png')