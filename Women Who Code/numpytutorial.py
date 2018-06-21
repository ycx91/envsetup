# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 19:39:46 2018

@author: Phoenix
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
im = np.array(Image.open(r"C:\Users\Phoenix\Desktop\ImageProcessing-master\image\SingaporeSkyline.jpg"))
print(im.shape, im.dtype)
im[1,2,0]
im = np.array(Image.open(r"C:\Users\Phoenix\Desktop\ImageProcessing-master\image\SingaporeSkyline.jpg").convert('L'),'f') 
print(im.shape, im.dtype)
np.asarray(im)
im = np.array(Image.open(r"C:\Users\Phoenix\Desktop\ImageProcessing-master\image\SingaporeSkyline.jpg").convert('L'))
im2 = 255 - im
im3 = (100.0/255) * im + 100
im4 = 255.0 * (im/255.0)**2
pil_im = Image.fromarray(im)
imshow(pil_im)
print(int(im2.min()), int(im2.max()))
Image.fromarray(im2)
print(int(im3.min()), int(im3.max()))
Image.fromarray(np.uint8(im3))
print(int(im4.min()), int(im4.max()))
Image.fromarray(np.uint8(im4))

def imresize(im,sz):
    pil_im = Image.fromarray(np.uint8(im))
    return np.array(pil_im.resize(sz))

im.shape
Image.fromarray((imresize(im,(200, 150))))

def histeq(im,nbr_bins=256):
    '''Histogram equalization of a grayscale image.'''
    imhist, bins = np.histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1]
    im2 = np.interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape), cdf

im2, cdf = histeq(im)
Image.fromarray(np.uint8(im2))
plt.figure()
plt.hist(im2.flatten(),128)
plt.show()


