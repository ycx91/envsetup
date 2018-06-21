# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 19:33:49 2018

@author: Phoenix
"""

from PIL import Image
from pylab import *

im = array(Image.open(r"C:\Users\Phoenix\Desktop\ImageProcessing-master\image\SingaporeSkyline.jpg"))
imshow(im)
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
plot(x,y,'r*')
plot(x[:2],y[:2],'w')
title('Plotting: \"SingaporeSkyline.jpg\"')
axis('off')
imshow(im)
im_gray = array(Image.open(r"C:\Users\Phoenix\Desktop\ImageProcessing-master\image\SingaporeSkyline.jpg").convert('L'))
figure()
gray()
contour(im_gray, origin='image')
axis('equal')
axis('off')
figure()
hist(im_gray.flatten(),128)
show()
