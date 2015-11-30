import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import matplotlib.gridspec as gridspec

#img = Image.open('tempo.jpg')
img = Image.open('pic2.jpg')
#img = Image.open('tempo.jpg')

imgmat = np.array(list(img.getdata(band=0)), float)
imgmat.shape = (img.size[1], img.size[0])
imgmat = np.matrix(imgmat)

U, sigma, V = np.linalg.svd(imgmat)

reconstimg1 = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
reconstimg5 = np.matrix(U[:, :5]) * np.diag(sigma[:5]) * np.matrix(V[:5, :])
reconstimg10 = np.matrix(U[:, :10]) * np.diag(sigma[:10]) * np.matrix(V[:10, :])
reconstimg25 = np.matrix(U[:, :25]) * np.diag(sigma[:25]) * np.matrix(V[:25, :])
reconstimg50 = np.matrix(U[:, :50]) * np.diag(sigma[:50]) * np.matrix(V[:50, :])


plt.subplot(231,aspect='equal')
plt.title('original:1080 x 720')
plt.imshow(img,cmap='gray')

plt.subplot(232,aspect='equal')
plt.title('SVD 50')
plt.imshow(reconstimg50, cmap='gray')

plt.subplot(233,aspect='equal')
plt.title('SVD 25')
plt.imshow(reconstimg25, cmap='gray')

plt.subplot(234,aspect='equal')
plt.title('SVD 10')
plt.imshow(reconstimg10, cmap='gray')

plt.subplot(235,aspect='equal')
plt.title('SVD 5')
plt.imshow(reconstimg5, cmap='gray')

plt.subplot(236,aspect='equal')
plt.title('SVD 1')
plt.imshow(reconstimg1, cmap='gray')

plt.savefig("Me2_test.png")
