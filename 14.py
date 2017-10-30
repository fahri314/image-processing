#iki resimdeki farkları bulma

import matplotlib.pyplot as plt

img_1 = plt.imread(r'C:\Users\user\Desktop\var.jpg')
img_2 = plt.imread(r'C:\Users\user\Desktop\yok.jpg')
plt.imshow(img_2-img_1)
plt.show()