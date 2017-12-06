# Original Author: Rishi Thakkar
# OA's Github: https://github.com/Atrifex
#
# Modified on 12/06/2017
# For ECE 385 Fall 2017
# By Harsh Modhera
#
# This script is an adaptation of png_to_palette_relative_resizer.py
# found in Rishi's ECE385-HelperTools. The purpose of this script is to 
# allow you to generate step sized increments to your image to give the
# appearance that the object is coming towards you on screen. In general,
# it allows you to present a 3D feel to your game. This script
# works great for gifs such as the one we used.
# https://thumbs.gfycat.com/UnacceptableNeglectedGuillemot-max-1mb.gif
#
# You can break the gif you want to use through an online gif decomposer.
# This will give you a bunch of image files that you can then change to 
# a .png format. With those images, a starting size and an ending size 
# in mind, you should be ready to roll.


from PIL import Image
from collections import Counter
from scipy.spatial import KDTree
import numpy as np

def hex_to_rgb(num):
    h = str(num)
    return int(h[0:4], 16), int(('0x' + h[4:6]), 16), int(('0x' + h[6:8]), 16)
def rgb_to_hex(num):
    h = str(num)
    return int(h[0:4], 16), int(('0x' + h[4:6]), 16), int(('0x' + h[6:8]), 16)

# This sets up the paths so you don't have to change them individually later on
# Note, you can add an additional folder name after the '/' for which your converted
# and byte files will get stored or you can leave it the way it is if you want to just
# store the images and text files directly into the given sprite folders.

filepath_converted = './sprite_converted/'
filepath_bytes = './sprite_bytes/'
filepath_originals = './sprite_originals/'

file_picture_ext = ".png"
file_text_ext = ".txt"

# This list contains each of the frames, in .png format, decomposed from the gif
files = ['bowserT_f1', 'bowserT_f2', 'bowserT_f3', 'bowserT_f4', 'bowserT_f5', 'bowserT_f6', 'bowserT_f7']

# This list contains the colours chosen in order to recreate the original image 
# with less accuracy in order to save memory. Follow same instructions as given by
# Rishi's YouTube tutorials.

palette_hex = ['0x9900FF', '0x000000', '0xFDEED7', '0x858484', '0x262825', '0x5B2B0F', '0xBE5D28', '0x8D1F00', '0xBB4900', '0x5B4A33', '0xDCB99C', '0xA38336', '0xF8CF00', '0x1ED60B', '0xF8DDA4']
palette_rgb = [hex_to_rgb(color) for color in palette_hex]

# The number of iterations indicates how many images you want from your orignal image
# to final image, with iteration = 1 being the original size. In this example, our gif does one walk
# in 7 frames. Since we wanted three walks, we used 21 iterations.
num_iter = 21

# This is the base line width and height. In other words, the smallest image.
orig_w = 96
orig_h = 128

# This is how much you want to increment/decrement your width and height in each iteration.
# You can play around with these based on how fast you want the image to grow.
width_inc = 10
height_inc = 13

# This is so that iteration 1 can start at the original image size.
new_w = orig_w - width_inc
new_h = orig_h - height_inc

# Note: the gist of the function body is the same as Rishi's file.

# Go through all the frames and generate the varying image sizes. You probably won't use them all
# but you can then go in and select the best matching ones to generate your evolving gif.
# Next, note the file naming convention used. Feel free to change it however you like, but understand
# that this convention prevented a lot of confusion for us so we recommend it.
for filename in files:
    for iteration in range(1,num_iter+1):
        new_w = new_w + width_inc
        new_h = new_h + height_inc
        # print new_w, new_h
        pixel_tree = KDTree(palette_rgb)
        im = Image.open(filepath_originals + filename + file_picture_ext) #Can be many different formats.
        im = im.convert("RGBA")
        im = im.resize((new_w, new_h),Image.ANTIALIAS) # regular resize
        pix = im.load()
        pix_freqs = Counter([pix[x, y] for x in range(im.size[0]) for y in range(im.size[1])])
        pix_freqs_sorted = sorted(pix_freqs.items(), key=lambda x: x[1])
        pix_freqs_sorted.reverse()
        # print(pix)
        outImg = Image.new('RGB', im.size, color='white')
        outFile = open(filepath_bytes + filename + "_" + str(new_w) + "_" + str(new_h) + file_text_ext, 'w')
        i = 0
        for y in range(im.size[1]):
            for x in range(im.size[0]):
                pixel = im.getpixel((x,y))
                #print(pixel)
                if(pixel[3] < 200):
                    outImg.putpixel((x,y), palette_rgb[0])
                    outFile.write("%x\n" % (0))
                    #print(i)
                else:
                    index = pixel_tree.query(pixel[:3])[1]
                    outImg.putpixel((x,y), palette_rgb[index])
                    outFile.write("%x\n" % (index))
                i += 1
        outFile.close()
        outImg.save(filepath_converted + filename + "_" + str(new_w) + "_" + str(new_h) + file_picture_ext)
        print 'Done: ' + filename + ', ' + str(iteration)
    new_w = orig_w - width_inc
    new_h = orig_h - height_inc

