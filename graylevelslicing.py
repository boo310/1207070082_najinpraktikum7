import imageio.v2 as imageio  # Importing the imageio package with the v2 module.
import numpy as np  # Importing the numpy package and assigning it the alias np.
from skimage import data  # Importing the data module from the skimage package.
import matplotlib.pyplot as plt  # Importing the matplotlib.pyplot module and assigning it the alias plt.

img = imageio.imread("noiseimage.jpg")  # Reading the image "noiseimage.jpg" using the imageio.imread() function.

row, column = img.shape  # Retrieving the shape of the image and assigning the values to the variables row and column.

img1 = np.zeros((row,column),dtype='uint8')  # Creating a new numpy array of zeros with the same shape as the image, with data type 'uint8'.

min_range = 10  # Setting the minimum range value.
max_range = 60  # Setting the maximum range value.

# Iterating through each pixel of the image.
for i in range(row):
    for j in range(column):
        if img[i,j] > min_range and img[i,j] < max_range:  # Checking if the pixel intensity is within the specified range.
            img1[i,j] = 255  # Setting the pixel value to 255 (white) if it is within the range.
        else:
            img1[i,j] = 0  # Setting the pixel value to 0 (black) if it is not within the range.

fig, axes = plt.subplots(2, 2, figsize=(12, 12))  # Creating a figure with 2x2 subplots and setting the size to (12, 12).
ax = axes.ravel()  # Flattening the subplots array.

ax[0].imshow(img, cmap=plt.cm.gray)  # Displaying the original image in the first subplot with a grayscale colormap.
ax[0].set_title("Citra Input")  # Setting the title of the first subplot.

ax[1].hist(img.ravel(), bins=256)  # Creating a histogram of the pixel intensities and displaying it in the second subplot.
ax[1].set_title('Histogram Input')  # Setting the title of the second subplot.

ax[2].imshow(img1, cmap=plt.cm.gray)  # Menampilkan gambar hasil pada subplot ketiga dengan peta warna keabuan.
ax[2].set_title("Citra Output")  # Menetapkan judul untuk subplot ketiga.

ax[3].hist(img1.ravel(), bins=256)  # Membuat histogram intensitas piksel hasil dan menampilkannya pada subplot keempat.
ax[3].set_title('Histogram Output')  # Menetapkan judul untuk subplot keempat.