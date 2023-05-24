import matplotlib.pyplot as plt
# Mengimpor modul matplotlib.pyplot untuk membuat visualisasi grafik.

#%matplotlib inline

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray 
import numpy as np

citra1 = imread(fname="images (2).tiff")
# Membaca citra dengan nama file "images (2).tiff" dan menyimpannya dalam variabel citra1.
citra2 = imread(fname="gray.tiff")
# Membaca citra dengan nama file "gray.tiff" dan menyimpannya dalam variabel citra2.

print('Shape citra 1 : ', citra1.shape)
# Menampilkan dimensi citra1.
print('Shape citra 1 : ', citra2.shape)
# Menampilkan dimensi citra2.

fig, axes = plt.subplots(1, 2, figsize=(10, 10))
# Membuat gambar dengan 1 baris dan 2 kolom menggunakan matplotlib dan menyimpannya dalam variabel fig dan axes.
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')
# Menampilkan citra1 dengan menggunakan skema warna abu-abu.
ax[0].set_title("Citra 1")
# Memberikan judul "Citra 1" pada citra1.
ax[1].imshow(citra2, cmap = 'gray')
# Menampilkan citra2 dengan menggunakan skema warna abu-abu.
ax[1].set_title("Citra 2")
# Memberikan judul "Citra 2" pada citra2.

copyCitra1 = citra1.copy()
# Membuat salinan citra1 dan menyimpannya dalam variabel copyCitra1.
copyCitra2 = citra2.copy()
# Membuat salinan citra2 dan menyimpannya dalam variabel copyCitra2.

m1,n1 = copyCitra1.shape
# Mendapatkan dimensi citra1 dan menyimpannya dalam variabel m1 dan n1.
output1 = np.empty([m1, n1])
# Membuat array kosong dengan dimensi yang sama dengan citra1 dan menyimpannya dalam variabel output1.

m2,n2 = copyCitra2.shape
# Mendapatkan dimensi citra2 dan menyimpannya dalam variabel m2 dan n2.
output2 = np.empty([m2, n2])
# Membuat array kosong dengan dimensi yang sama dengan citra2 dan menyimpannya dalam variabel output2.
print('Shape copy citra 1 : ', copyCitra1.shape)
# Menampilkan dimensi copyCitra1.
print('Shape output citra 1 : ', output1.shape)
# Menampilkan dimensi output1.

print('m1 : ',m1)
# Menampilkan nilai m1.
print('n1 : ',n1)
# Menampilkan nilai n1.
print()

print('Shape copy citra 2 : ', copyCitra2.shape)
# Menampilkan dimensi copyCitra2.
print('Shape output citra 3 : ', output2.shape)
# Menampilkan dimensi output2.
print('m2 : ',m2)
# Menampilkan nilai m2.
print('n2 : ',n2)
# Menampilkan nilai n2.
print()

for baris in range(0, m1-1):
    # Melakukan perulangan untuk setiap baris citra1.
    for kolom in range(0, n1-1):
        # Melakukan perulangan untuk setiap kolom citra1.
        
        a1 = baris
        b1 = kolom
        
        arr = np.array([copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1, b1+1], \
            copyCitra1[a1, b1-1], copyCitra1[a1, b1+1], copyCitra1[a1+1, b1-1],  \
            copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]])
        # Membuat array dengan nilai piksel sekitar citra1[a1, b1] dan menyimpannya dalam variabel arr.
        
        minPiksel = np.amin(arr)
        # Menemukan nilai piksel terkecil dalam array arr dan menyimpannya dalam variabel minPiksel.
        maksPiksel = np.amax(arr)
        # Menemukan nilai piksel terbesar dalam array arr dan menyimpannya dalam variabel maksPiksel.
            
        if copyCitra1[baris, kolom] < minPiksel :
            output1[baris, kolom] = minPiksel
            # Jika nilai piksel citra1[baris, kolom] lebih kecil daripada minPiksel, simpan minPiksel di output1[baris, kolom].
        else :
            if copyCitra1[baris, kolom] > maksPiksel :
                output1[baris, kolom] = maksPiksel
                # Jika nilai piksel citra1[baris, kolom] lebih besar daripada maksPiksel, simpan maksPiksel di output1[baris, kolom].
            else :
                output1[baris, kolom] = copyCitra1[baris, kolom]
                # Jika nilai piksel citra1[baris, kolom] berada di antara minPiksel dan maksPiksel, simpan nilai tersebut di output1[baris, kolom].

for baris1 in range(0, m2-1):
    # Melakukan perulangan untuk setiap baris citra2.
    for kolom1 in range(0, n2-1):
        # Melakukan perulangan untuk setiap kolom citra2.
        
        a1 = baris1
        b1 = kolom1
        
        arr = np.array([copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1, b1+1], \
            copyCitra2[a1, b1-1], copyCitra2[a1, b1+1], copyCitra2[a1+1, b1-1],  \
            copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]])
        # Membuat array dengan nilai piksel sekitar citra2[a1, b1] dan menyimpannya dalam variabel arr.
        
        minPiksel = np.amin(arr)
        # Menemukan nilai piksel terkecil dalam array arr dan menyimpannya dalam variabel minPiksel.
        maksPiksel = np.amax(arr)
        # Menemukan nilai piksel terbesar dalam array arr dan menyimpannya dalam variabel maksPiksel.
            
        if copyCitra2[baris1, kolom1] < minPiksel :
            output2[baris1, kolom1] = minPiksel
            # Jika nilai piksel citra2[baris1, kolom1] lebih kecil daripada minPiksel, simpan minPiksel di output2[baris1, kolom1].
        else :
            if copyCitra2[baris1, kolom1] > maksPiksel :
                output2[baris1, kolom1] = maksPiksel
                # Jika nilai piksel citra2[baris1, kolom1] lebih besar daripada maksPiksel, simpan maksPiksel di output2[baris1, kolom1].
            else :
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]
                # Jika nilai piksel citra2[baris1, kolom1] berada di antara minPiksel dan maksPiksel, simpan nilai tersebut di output2[baris1, kolom1].

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
# Membuat gambar dengan 2 baris dan 2 kolom menggunakan matplotlib dan menyimpannya dalam variabel fig dan axes.
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')
# Menampilkan citra1 dengan menggunakan skema warna abu-abu.
ax[0].set_title("Input Citra 1")
# Memberikan judul "Input Citra 1" pada citra1.

ax[1].imshow(citra2, cmap = 'gray')
# Menampilkan citra2 dengan menggunakan skema warna abu-abu.
ax[1].set_title("Input Citra 2")
# Memberikan judul "Input Citra 2" pada citra2.

ax[2].imshow(output1, cmap = 'gray')
# Menampilkan output1 dengan menggunakan skema warna abu-abu.
ax[2].set_title("Output Citra 1")
# Memberikan judul "Output Citra 1" pada output1.

ax[3].imshow(output2, cmap = 'gray')
# Menampilkan output2 dengan menggunakan skema warna abu-abu.
ax[3].set_title("Output Citra 2")
# Memberikan judul "Output Citra 2" pada output2.