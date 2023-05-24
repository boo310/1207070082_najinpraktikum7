import matplotlib.pyplot as plt  # Mengimpor modul matplotlib.pyplot dan memberi alias plt.

#%matplotlib inline

from skimage import data  # Mengimpor modul data dari paket skimage.
from skimage.io import imread  # Mengimpor fungsi imread dari modul io dalam paket skimage.
from skimage.color import rgb2gray  # Mengimpor fungsi rgb2gray dari modul color dalam paket skimage.
import numpy as np  # Mengimpor paket numpy dan memberi alias np.
import imagecodecs  # Mengimpor paket imagecodecs.

citra1 = imread(fname="gray.tiff")  # Membaca citra "gray.tiff" menggunakan fungsi imread() dan menyimpannya dalam variabel citra1.
citra2 = imread(fname="images (2).tiff")  # Membaca citra "images (2).tiff" menggunakan fungsi imread() dan menyimpannya dalam variabel citra2.

print('Shape citra 1 : ', citra1.shape)  # Mencetak dimensi citra1.
print('Shape citra 2 : ', citra2.shape)  # Mencetak dimensi citra2.

fig, axes = plt.subplots(1, 2, figsize=(10, 10))  # Membuat gambar dengan 1 baris dan 2 subplot dengan ukuran (10, 10).
ax = axes.ravel()  # Meratakan array subplot.

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra1 pada subplot pertama dengan peta warna keabuan.
ax[0].set_title("Citra 1")  # Menetapkan judul untuk subplot pertama.

ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra2 pada subplot kedua dengan peta warna keabuan.
ax[1].set_title("Citra 2")  # Menetapkan judul untuk subplot kedua.

copyCitra1 = citra1.copy().astype(float)  # Membuat salinan citra1 dengan tipe data float.
copyCitra2 = citra2.copy().astype(float)  # Membuat salinan citra2 dengan tipe data float.

m1, n1 = copyCitra1.shape  # Mengambil dimensi citra1 dan memberikan nilai kepada variabel m1 dan n1.
print(copyCitra1.shape)  # Mencetak dimensi copyCitra1.
output1 = np.empty([m1, n1])  # Membuat array kosong dengan dimensi yang sama dengan citra1.

m2, n2 = copyCitra2.shape  # Mengambil dimensi citra2 dan memberikan nilai kepada variabel m2 dan n2.
output2 = np.empty([m2, n2])  # Membuat array kosong dengan dimensi yang sama dengan citra2.
print('Shape copy citra 1 : ', copyCitra1.shape)  # Mencetak dimensi copyCitra1.
print('Shape output citra 1 : ', output1.shape)  # Mencetak dimensi output1.
print('m1 : ', m1)  # Mencetak nilai m1.
print('n1 : ', n1)  # Mencetak nilai n1.
print()

print('Shape copy citra 2 : ', copyCitra2.shape)  # Mencetak dimensi copyCitra2.
print('Shape output citra 3 : ', output2.shape)  # Mencetak dimensi output2.
print('m2 : ', m2)  # Mencetak nilai m2.
print('n2 : ', n2)  # Mencetak nilai n2.
print()

# Melakukan iterasi melalui setiap piksel pada copyCitra1.
for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        jumlah = copyCitra1[a1-1, b1-1] + copyCitra1[a1-1, b1] + copyCitra1[a1-1, b1-1] + \
                 copyCitra1[a1, b1-1] + copyCitra1[a1, b1] + copyCitra1[a1, b1+1] + \
                 copyCitra1[a1+1, b1-1] + copyCitra1[a1+1, b1] + copyCitra1[a1+1, b1+1]
        output1[a1, b1] = (1/9 * jumlah)  # Menyimpan hasil rata-rata dalam output1.

# Melakukan iterasi melalui setiap piksel pada copyCitra2.
for baris1 in range(0, m2-1):
    for kolom1 in range(0, n2-1):
        a1 = baris1
        b1 = kolom1
        jumlah = copyCitra2[a1-1, b1-1] + copyCitra2[a1-1, b1] + copyCitra2[a1-1, b1-1] + \
                 copyCitra2[a1, b1-1] + copyCitra2[a1, b1] + copyCitra2[a1, b1+1] + \
                 copyCitra2[a1+1, b1-1] + copyCitra2[a1+1, b1] + copyCitra2[a1+1, b1+1]
        output2[a1, b1] = (1/9 * jumlah)  # Menyimpan hasil rata-rata dalam output2.

fig, axes = plt.subplots(2, 2, figsize=(10, 10))  # Membuat gambar dengan 2 baris dan 2 subplot dengan ukuran (10, 10).
ax = axes.ravel()  # Meratakan array subplot.

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra1 pada subplot pertama dengan peta warna keabuan.
ax[0].set_title("Input Citra 1")  # Menetapkan judul untuk subplot pertama.

ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra2 pada subplot kedua dengan peta warna keabuan.
ax[1].set_title("Input Citra 1")  # Menetapkan judul untuk subplot kedua.

ax[2].imshow(output1, cmap='gray')  # Menampilkan output1 pada subplot ketiga dengan peta warna keabuan.
ax[2].set_title("Output Citra 1")  # Menetapkan judul untuk subplot ketiga.

ax[3].imshow(output2, cmap='gray')  # Menampilkan output2 pada subplot keempat dengan peta warna keabuan.
ax[3].set_title("Output Citra 2")  # Menetapkan judul untuk subplot keempat.
