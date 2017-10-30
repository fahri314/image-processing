# rgb resmi gray levele çevirme (rgb to gray level)

#pixel_1_rgb = [0,0,0]
#pixel_1_gray_level = 0

#pixel_1_rgb = [10,0,0]
#pixel_1_gray_level = 10

#pixel_1_rgb = [0,10,0]
#pixel_1_gray_level = 10

#pixel_1_rgb = [0,0,0]
#pixel_1_gray_level = 0

#pixel_1_rgb = [10,10,10]
#pixel_1_gray_level = 12

# bunun fonksiyonunu yazalım

import matplotlib.pyplot as plt
import numpy as np

img_1 = plt.imread(r'C:\Users\user\Desktop\eleven.png')

def convert(RGB_Pixel):
    return RGB_Pixel[0]/3 + RGB_Pixel[1]/3 + RGB_Pixel[2]/3

# convert([2,5,7])

img_2 = np.zeros((img_1.shape[0],img_1.shape[1]))        # aynı boyutta olustur

for i in range (img_1.shape[0]):
    for j in range (img_2.shape[1]):
        img_2[i,j] = convert(img_1[i,j,:])

plt.subplot(1,2,1)                                        # subplot resimleri yan yana göstermek için
plt.imshow(img_1)
plt.subplot(1,2,2)
plt.imshow(img_2,cmap = 'gray')
plt.show()