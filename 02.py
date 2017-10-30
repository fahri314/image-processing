from scipy import ndimage, misc
import matplotlib.pyplot as plt

f = misc.face()
f[:,:,2] = 0
plt.imshow(f)
plt.show()