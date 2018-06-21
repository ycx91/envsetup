# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 19:50:29 2018

@author: Phoenix
"""

from PIL import Image
from numpy import *
from scipy.ndimage import filters
import matplotlib.pyplot as plt
im = array(Image.open(r"C:\Users\Phoenix\Desktop\ImageProcessing-master\image\SingaporeSkyline.jpg").convert('L'))
im2 =  filters.gaussian_filter(im,5) # params: (image, standard deviation)
Image.fromarray(im2)
# Apply Gussian blurring to each colour channel:
im = array(Image.open(r"C:\Users\Phoenix\Desktop\ImageProcessing-master\image\SingaporeSkyline.jpg"))
im2 = zeros(im.shape)
for i in range(3):
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
im2 = uint8(im2) # or \"im2 = array(im2, 'uint8')\" to force pixel values to 8-bit representations"
plt.imshow(im2)

Image.fromarray(im2)
im = array(Image.open(r"C:\Users\Phoenix\Desktop\ImageProcessing-master\image\SingaporeSkyline.jpg").convert('L'))
imx = zeros(im.shape)
filters.sobel(im, 1, imx)
imy = zeros(im.shape)
filters.sobel(im, 0, imy)
magnitude = sqrt(imx**2 + imy**2)
Image.fromarray(uint8(im-magnitude))
# Gaussian derivatives
sigma = 5 # standard deviation
imx = zeros(im.shape)
filters.gaussian_filter(im, (sigma,sigma), (0,1), imx)

imy = zeros(im.shape)
filters.gaussian_filter(im, (sigma,sigma), (1,0), imy)


## Morphology - Counting Objects
from scipy.ndimage import measurements, morphology
# load image and threshold to make sure it is binary
im = array(Image.open(r"C:\Users\Phoenix\Desktop\ImageProcessing-master\image\women_who_code.jpg").convert('L'))
for i in range(1, 3):
    im = 1*(im<150)
    plt.imshow(im)
    labels, nbr_objects = measurements.label(im)
    print("Number of objects:", nbr_objects)
    Image.open(r"C:\Users\Phoenix\Desktop\ImageProcessing-master\image\women_who_code.jpg").convert('L')
    plt.imshow(im)

