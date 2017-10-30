#25 tane resim üret
#resimleri siyah beyaz yap
#reshape fonksiyonu ile boyut değiştir vektöre dönüştür matrisi 100x100 ise 1x10000 yap
#center.a b c d yap
#test

import matplotlib.pyplot as plt
import numpy as np
img_1=plt.imread(r'C:\Users\User\Desktop\image\a1.png')
img_2=plt.imread(r'C:\Users\User\Desktop\image\a2.png')
img_3=plt.imread(r'C:\Users\User\Desktop\image\a3.png')
img_4=plt.imread(r'C:\Users\User\Desktop\image\a4.png')
img_5=plt.imread(r'C:\Users\User\Desktop\image\a5.png')
img_6=plt.imread(r'C:\Users\User\Desktop\image\b1.png')
img_7=plt.imread(r'C:\Users\User\Desktop\image\b2.png')
img_8=plt.imread(r'C:\Users\User\Desktop\image\b3.png')
img_9=plt.imread(r'C:\Users\User\Desktop\image\b4.png')
img_10=plt.imread(r'C:\Users\User\Desktop\image\b5.png')
img_11=plt.imread(r'C:\Users\User\Desktop\image\c1.png')
img_12=plt.imread(r'C:\Users\User\Desktop\image\c2.png')
img_13=plt.imread(r'C:\Users\User\Desktop\image\c3.png')
img_14=plt.imread(r'C:\Users\User\Desktop\image\c4.png')
img_15=plt.imread(r'C:\Users\User\Desktop\image\c5.png')
img_16=plt.imread(r'C:\Users\User\Desktop\image\d1.png')
img_17=plt.imread(r'C:\Users\User\Desktop\image\d2.png')
img_18=plt.imread(r'C:\Users\User\Desktop\image\d3.png')
img_19=plt.imread(r'C:\Users\User\Desktop\image\d4.png')
img_20=plt.imread(r'C:\Users\User\Desktop\image\d5.png')
img_21=plt.imread(r'C:\Users\User\Desktop\image\e1.png')
img_22=plt.imread(r'C:\Users\User\Desktop\image\e2.png')
img_23=plt.imread(r'C:\Users\User\Desktop\image\e3.png')
img_24=plt.imread(r'C:\Users\User\Desktop\image\e4.png')
img_25=plt.imread(r'C:\Users\User\Desktop\image\e5.png')

def convert(img_y):
    for i in range(img_y.shape[0]): 
        for j in range(img_y.shape[1]):
            img_x[i,j]=img_y[i,j,0]/3+img_y[i,j,1]/3+img_y[i,j,2]/3
    return img_x

def reshape(img_y):
    n = img_y.shape[0] * img_y.shape[1]
    img_x = img_y.reshape(1,n)
    return img_x


img_y = img_1
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,1), plt.imshow(img_x, plt.cm.binary)
img_y = img_2
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,2), plt.imshow(img_x, plt.cm.binary)
img_y = img_3
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,3), plt.imshow(img_x, plt.cm.binary)
img_y = img_4
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,4), plt.imshow(img_x, plt.cm.binary)
img_y = img_5
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,5), plt.imshow(img_x, plt.cm.binary)
img_y = img_6
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,6), plt.imshow(img_x, plt.cm.binary)
img_y = img_7
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,7), plt.imshow(img_x, plt.cm.binary)
img_y = img_8
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,8), plt.imshow(img_x, plt.cm.binary)
img_y = img_9
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,9), plt.imshow(img_x, plt.cm.binary)
img_y = img_10
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,10), plt.imshow(img_x, plt.cm.binary)
img_y = img_11
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,11), plt.imshow(img_x, plt.cm.binary)
img_y = img_12
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,12), plt.imshow(img_x, plt.cm.binary)
img_y = img_13
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,13), plt.imshow(img_x, plt.cm.binary)
img_y = img_14
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,14), plt.imshow(img_x, plt.cm.binary)
img_y = img_15
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,15), plt.imshow(img_x, plt.cm.binary)
img_y = img_16
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,16), plt.imshow(img_x, plt.cm.binary)
img_y = img_17
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,17), plt.imshow(img_x, plt.cm.binary)
img_y = img_18
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,18), plt.imshow(img_x, plt.cm.binary)
img_y = img_19
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,19), plt.imshow(img_x, plt.cm.binary)
img_y = img_20
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,20), plt.imshow(img_x, plt.cm.binary)
img_y = img_21
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,21), plt.imshow(img_x, plt.cm.binary)
img_y = img_22
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,22), plt.imshow(img_x, plt.cm.binary)
img_y = img_23
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,23), plt.imshow(img_x, plt.cm.binary)
img_y = img_24
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,24), plt.imshow(img_x, plt.cm.binary)
img_y = img_25
img_x = np.zeros((img_y.shape[0:2]))
img_x = convert(img_y)
img_x = reshape(img_x)
plt.subplot(1,25,25), plt.imshow(img_x, plt.cm.binary)
plt.show()
