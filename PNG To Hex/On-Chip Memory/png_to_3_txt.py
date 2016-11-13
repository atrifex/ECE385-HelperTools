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
filename = input("What's the image name? ")
new_w, new_h = map(int, input("What's the new height x width? Like 28 28. ").split(' '))
#palette_hex = ['0x000000', '0xF83800', '0xF0D0B0', '0x503000', '0xFFE0A8', '0x0058F8', '0xFCFCFC', '0xBCBCBC', '0xA40000', '0xD82800', '0xFC7460', '0xFCBCB0', '0xF0BC3C', '0xAEACAE', '0x363301', '0x6C6C01', '0xBBBD00', '0x88D500', '0x398802', '0x65B0FF', '0x155ED8', '0x800080']
#palette_rgb = [hex_to_rgb(color) for color in palette_hex]

#pixel_tree = KDTree(palette_rgb)
im = Image.open("./sprite_originals/" + filename) #Can be many different formats.
im = im.convert("RGBA")
layer = Image.new('RGBA',(new_w, new_h), (0,0,0,0))
layer.paste(im, (0, 0))
im = layer
#im = im.resize((new_w, new_h),Image.ANTIALIAS) # regular resize
pix = im.load()
pix_freqs = Counter([pix[x, y] for x in range(im.size[0]) for y in range(im.size[1])]) 
pix_freqs_sorted = sorted(pix_freqs.items(), key=lambda x: x[1])
pix_freqs_sorted.reverse()
print(pix)
outImgR = Image.new('RGB', im.size, color='white')
outFileR = open("./sprite_bytes/" + filename + 'R.txt', 'w')
outImgG = Image.new('RGB', im.size, color='white')
outFileG = open("./sprite_bytes/" + filename + 'G.txt', 'w')
outImgB = Image.new('RGB', im.size, color='white')
outFileB = open("./sprite_bytes/" + filename + 'B.txt', 'w')
#i = 0
for y in range(im.size[1]):
    for x in range(im.size[0]):
        pixel = im.getpixel((x,y))
        print(pixel)
        r, g, b, a = im.getpixel((x,y))
        pixelR  = (r, 0, 0, 255)
        pixelG = (0, g, 0, 255)
        pixelB = (0, 0, b, 255)
        outImgR.putpixel((x,y), pixelR)
        outImgG.putpixel((x,y), pixelG)
        outImgB.putpixel((x,y), pixelB)
        #r, g, b, a = im.getpixel((x,y))
        outFileR.write("%x\n" %(r))
        outFileG.write("%x\n" %(g))
        outFileB.write("%x\n" %(b))
outFileR.close()
outFileB.close()
outFileG.close()
outImgR.save("./sprite_converted/" + filename + 'R.png')
outImgG.save("./sprite_converted/" + filename + 'G.png')
outImgB.save("./sprite_converted/" + filename + 'B.png')


