import matplotlib.pyplot as plt
#%matplotlib inline
# Mengimport library matplotlib dan mengatur mode inline untuk menampilkan plot secara langsung.

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray 
import numpy as np

import cv2

citra1 = imread(fname="pexels-faris-al-orfali-1697159.tiff")
# Membaca citra dari file "pexels-faris-al-orfali-1697159.tiff" dan menyimpannya dalam variabel citra1.
print(citra1.shape)
# Menampilkan dimensi citra1.

plt.imshow(citra1, cmap='gray')
# Menampilkan citra1 dalam skema warna abu-abu.

kernel = np.array([[-1, 0, -1], 
                   [0, 4, 0], 
                   [-1, 0, -1]])
# Membuat kernel yang digunakan untuk operasi filter.

citraOutput = cv2.filter2D(citra1, -1, kernel)
# Mengaplikasikan operasi filter dengan menggunakan kernel pada citra1 dan menyimpan hasilnya dalam variabel citraOutput.

fig, axes = plt.subplots(1, 2, figsize=(12, 12))
# Membuat gambar dengan 1 baris dan 2 kolom menggunakan matplotlib dan menyimpannya dalam variabel fig dan axes.
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')
ax[0].set_title("Citra Input")
# Menampilkan citra1 dalam skema warna abu-abu dan memberikan judul "Citra Input" pada plot tersebut.

ax[1].imshow(citraOutput, cmap='gray')
ax[1].set_title("Citra Output")
# Menampilkan citraOutput dalam skema warna abu-abu dan memberikan judul "Citra Output" pada plot tersebut.