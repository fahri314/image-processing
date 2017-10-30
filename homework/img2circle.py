#adres > http://www.scipy-lectures.org/advanced/image_processing/

from scipy import ndimage,misc
import matplotlib.pyplot as plt
import math

def findDistance(x,y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

#d = findDistance([3,0],[0,4])

f = misc.face()
im_size = f.shape
center = [im_size[0]/2,im_size[1]/2]

for i in range(im_size[0]):
    for j in range(im_size[1]):
        if findDistance([i,j],center)>400:
            f[i,j,:] = 0

plt.imshow(f)
plt.show()