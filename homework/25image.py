#25 tane resim üret
#resimleri siyah beyaz yap
#reshape fonksiyonu ile boyut değiştir vektöre dönüştür matrisi 100x100 ise 1x10000 yap
#center.a b c d yap
#test

import matplotlib.pyplot as plt
import numpy as np
img_1=plt.imread(r'C:\Users\BM\Desktop\1.jpg')
img_2=plt.imread(r'C:\Users\BM\Desktop\2.jpg')
img_3=plt.imread(r'C:\Users\BM\Desktop\3.jpg')
img_4=plt.imread(r'C:\Users\BM\Desktop\4.jpg')
img_5=plt.imread(r'C:\Users\BM\Desktop\5.jpg')

img_x=np.zeros((img_1.shape [0:2]))

#plt.imshow(img_6,plt.cm.binary)
#plt.show()

threshold=150
def convert(img_y):
    for i in range(img_y.shape[0]): 
        for j in range(img_y.shape[1]):
            n=img_y[i,j,0]/3+img_y[i,j,1]/3+img_y[i,j,2]/3
            if n>threshold:
                img_x[i,j]=255
            else:
                img_x[i,j]=0
    return img_x
plt.subplot(1,6,1),plt.imshow(img_1)
img_y = img_1
img_x=np.zeros((img_1.shape [0:2]))
img_x = convert(img_y)
plt.subplot(1,6,2),plt.imshow(img_x,plt.cm.binary)
img_y = img_2
img_x=np.zeros((img_2.shape [0:2]))
img_x = convert(img_y)
plt.subplot(1,6,3),plt.imshow(img_x,plt.cm.binary)
img_y = img_3
img_x=np.zeros((img_3.shape [0:2]))
img_x = convert(img_y)
plt.subplot(1,6,4),plt.imshow(img_x,plt.cm.binary)
img_y = img_4
img_x=np.zeros((img_4.shape [0:2]))
img_x = convert(img_y)
plt.subplot(1,6,5),plt.imshow(img_x,plt.cm.binary)
img_y = img_5
img_x=np.zeros((img_5.shape [0:2]))
img_x = convert(img_y)
plt.subplot(1,6,6),plt.imshow(img_x,plt.cm.binary)
plt.show()