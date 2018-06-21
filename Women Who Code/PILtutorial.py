# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 19:16:57 2018

@author: Phoenix
"""

from PIL import Image
import os
import glob

pil_im = Image.open(r'C:\Users\Phoenix\Desktop\ImageProcessing-master\image\SingaporeSkyline.jpg')

print (pil_im)
filelist = glob.glob(r'C:\Users\Phoenix\Desktop\ImageProcessing-master\image\*')
print (filelist)
for infile in filelist:
    outfile = os.path.splitext(infile)[0] + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)
pil_im.thumbnail((128,128))
print (pil_im)

pil_im = Image.open(r'C:\Users\Phoenix\Desktop\ImageProcessing-master\image\SingaporeSkyline.jpg')
box = (100,100,400,400)
region = pil_im.crop(box)
print (region)
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)
pil_im2 = pil_im.resize((200,200))
print (pil_im2)
pil_im2.rotate(45)
print (pil_im2)
