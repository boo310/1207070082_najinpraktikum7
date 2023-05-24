import matplotlib.pyplot as plt
#%matplotlib inline

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray 
import numpy as np

citra1 = imread(fname="images (2).tiff")  # Membaca citra 1
citra2 = imread(fname="gray.tiff")  # Membaca citra 2

print('Shape citra 1 : ', citra1.shape)  # Menampilkan bentuk citra 1
print('Shape citra 1 : ', citra2.shape)  # Menampilkan bentuk citra 2

fig, axes = plt.subplots(1, 2, figsize=(10, 10))  # Membuat subplot untuk menampilkan gambar
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra 1 dalam skala keabuan
ax[0].set_title("Citra 1")
ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra 2 dalam skala keabuan
ax[1].set_title("Citra 2")

copyCitra1 = citra1.copy()  # Membuat salinan citra 1
copyCitra2 = citra2.copy()  # Membuat salinan citra 2

m1, n1 = copyCitra1.shape  # Mendapatkan ukuran citra 1
output1 = np.empty([m1, n1])  # Membuat array kosong dengan ukuran citra 1

m2, n2 = copyCitra2.shape  # Mendapatkan ukuran citra 2
output2 = np.empty([m2, n2])  # Membuat array kosong dengan ukuran citra 2
print('Shape copy citra 1 : ', copyCitra1.shape)  # Menampilkan bentuk salinan citra 1
print('Shape output citra 1 : ', output1.shape)  # Menampilkan bentuk output citra 1

print('m1 : ', m1)  # Menampilkan nilai m1
print('n1 : ', n1)  # Menampilkan nilai n1
print()

print('Shape copy citra 2 : ', copyCitra2.shape)  # Menampilkan bentuk salinan citra 2
print('Shape output citra 3 : ', output2.shape)  # Menampilkan bentuk output citra 3
print('m2 : ', m2)  # Menampilkan nilai m2
print('n2 : ', n2)  # Menampilkan nilai n2
print()

for baris in range(0, m1-1):  # Melakukan iterasi untuk setiap baris citra 1
    for kolom in range(0, n1-1):  # Melakukan iterasi untuk setiap kolom citra 1
        a1 = baris
        b1 = kolom
        dataA = [copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1-1, b1+1], \
                 copyCitra1[a1, b1-1], copyCitra1[a1, b1], copyCitra1[a1, b1+1], \
                 copyCitra1[a1+1, b1-1], copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]]  # Mengambil data sekitar piksel tertentu

        # Urutkan data
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA

        output1[a1, b1] = dataA[5]  # Menyimpan nilai median ke output1

for baris in range(0, m2-1):  # Melakukan iterasi untuk setiap baris citra 2
    for kolom in range(0, n2-1):  # Melakukan iterasi untuk setiap kolom citra 2
        a1 = baris
        b1 = kolom
        dataA = [copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1-1, b1+1], \
                 copyCitra2[a1, b1-1], copyCitra2[a1, b1], copyCitra2[a1, b1+1], \
                 copyCitra2[a1+1, b1-1], copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]]  # Mengambil data sekitar piksel tertentu

        # Urutkan data
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA

        output2[a1, b1] = dataA[5]  # Menyimpan nilai median ke output2

fig, axes = plt.subplots(2, 2, figsize=(10, 10))  # Membuat subplot baru
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra 1
ax[0].set_title("Input Citra 1")

ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra 2
ax[1].set_title("Input Citra 1")

ax[2].imshow(output1, cmap='gray')  # Menampilkan output citra 1 setelah proses median filtering
ax[2].set_title("Output Citra 1")

ax[3].imshow(output2, cmap='gray')  # Menampilkan output citra 2 setelah proses median filtering
ax[3].set_title("Output Citra 2")