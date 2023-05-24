import numpy as np                  #Numpy digunakan untuk operasi numerik
import matplotlib.pyplot as plt     #matplotlib untuk visualisasi
#%matplotlib inline
import cv2                          #cv2 untuk pemrosesan gambar
import matplotlib.image as mpimg    #mpimg untuk membaca gambar
from skimage import data            #skimage untuk data gambar
import imageio.v2 as imageio        #dan imageio untuk operasi pada gambar

image = cv2.imread("gry.png", 0)    #baca gambar simpan di image
image_equalized = cv2.equalizeHist(image)#menggunakan fungsi equalizeHist dari OpenCV untuk melakukan ekualisasi histogram pada gambar "image" dan menyimpan hasilnya ke dalam variabel "image_equalized".
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))#membuat objek CLAHE (Contrast Limited Adaptive Histogram Equalization) dengan batas klip sebesar 2 dan ukuran grid tile sebesar 8x8, yang akan digunakan nanti.

#Apply CLAHE to the original image
image_clahe = clahe.apply(image) #menerapkan CLAHE pada gambar asli ("image") menggunakan objek CLAHE yang telah dibuat sebelumnya, dan menyimpan hasilnya ke dalam variabel "image_clahe".
# Create an empty array to store the final output
image_cs = np.zeros((image.shape[0],image.shape[1]),dtype = 'uint8')#membuat array kosong dengan ukuran yang sama dengan gambar "image" dan tipe data unsigned integer 8-bit (uint8), yang akan digunakan untuk menyimpan output akhir.

# Apply Min-Max Contrasting
min = np.min(image) #menghitung nilai minimum dari gambar "image" menggunakan fungsi  np.min(), dan menyimpannya ke dalam variabel "min" .
max = np.max(image) #menghitung nilai maksimum dari gambar "image" menggunakan fungsi np.mmax() , dan menyimpannya ke dalam variabel  "max" .

for i in range(image.shape[0]):#melakukan perulangan untuk setiap piksel dalam gambar "image" 
    for j in range(image.shape[1]):#melakukan perulangan untuk setiap piksel dalam gambar "image" 
        image_cs[i,j] = 255*(image[i,j]-min)/(max-min)#menghitung kontras dan stretching menggunakan rumus (piksel - min) / (max - min) dengan nilai piksel diubah ke dalam rentang 0-255, dan hasilnya disimpan ke dalam array "image_cs".
copyCamera = image.copy().astype(float)#membuat salinan gambar "image" dengan tipe data float menggunakan metode .copy() dan .astype(float), dan menyimpannya ke dalam variabel "copyCamera".

m1,n1 = copyCamera.shape#mengambil dimensi gambar "copyCamera" menggunakan .shape dan menyimpannya ke dalam variabel "m1" dan "n1". 
output1 = np.empty([m1, n1])# array kosong "output1" dengan ukuran yang sama dengan "copyCamera" dibuat menggunakan np.empty().

for baris in range(0, m1-1):#Melakukan perulangan untuk setiap piksel dalam citra salinan 'copyCamera' 
    for kolom in range(0, n1-1):
        a1 = baris#memasukan hasil baris kedalam variable a1
        b1 = kolom##memasukan hasil kolom kedalam variable b1
        output1[a1, b1] = copyCamera[baris, kolom] * 1.9#mengalikan nilai setiap piksel dengan 1.9, kemudian menyimpan hasilnya di dalam array 'output1'.
    fig, axes = plt.subplots(5, 2, figsize=(20, 20))# Citra dan histogram ditampilkan dalam grid 5x2 dengan ukuran 20 *20 pixel . 
    ax = axes.ravel()#Posisi citra dan histogram dalam grid ditentukan oleh indeks pada array 'ax'.

    ax[0].imshow(image, cmap=plt.cm.gray)#Menghasilkan plot dan visualisasi untuk citra-citra dan histogram yang dihasilkan.
    ax[0].set_title("Citra Input")#judul
    ax[1].hist(image.ravel(), bins=256)
    ax[1].set_title('Histogram Input')

    ax[2].imshow(image_equalized, cmap=plt.cm.gray)
    ax[2].set_title("Citra Output HE")
    ax[3].hist(image_equalized.ravel(), bins=256)
    ax[3].set_title('Histogram Output HE Method')

    ax[4].imshow(image_cs, cmap=plt.cm.gray)
    ax[4].set_title("Citra Output CS")
    ax[5].hist(image_cs.ravel(), bins=256)
    ax[5].set_title('Histogram Output CS Method')

    ax[6].imshow(image_clahe, cmap=plt.cm.gray)
    ax[6].set_title("Citra Grayscale CLAHE")
    ax[7].hist(image_clahe.ravel(), bins=256)
    ax[7].set_title('Histogram Output CLAHE Method')

    ax[8].imshow(output1, cmap=plt.cm.gray)
    ax[8].set_title("Citra Grayscale Perkalian Konstanta")
    ax[9].hist(output1.ravel(), bins=256)
    ax[9].set_title('Histogram Output Perkalian Konstanta Method')

    fig.tight_layout()#digunakan untuk mengatur tata letak (layout) gambar agar sesuai dan tidak tumpang tindih. Fungsi ini memastikan agar tidak ada tumpang tindih antara gambar-gambar yang ditampilkan dalam subplots.

    plt.close()# digunakan untuk menutup (close) gambar yang ditampilkan. Hal ini dilakukan untuk membersihkan memori dan menghindari tumpang tindih antara gambar-gambar yang ditampilkan saat menjalankan program berulang kali atau dalam lingkungan pengembangan interaktif.