"""
ascii.py
A python program that convert images to ASCII art.
"""

# import sys
# import random
import argparse
# import numpy as np
# import math
import statistics

# from PIL import Image
from PIL import Image, ImageDraw
# , ImageFont

# import os

# ascii.py adapted from Python Playground by Mahesh Venkitachalam
# gray scale level values from:
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10 levels of gray
gscale2 = '@%#*+=-:. '

# below not used because get_average_new() function replaces it.
# def getAverageL(image):
#     """
#     Given PIL Image, return average value of grayscale value
#     """
#     # get image as numpy array
#     im = np.array(image)
#     # get shape
#     w,h = im.shape
#     # get average
#     return np.average(im.reshape(w*h))


def get_average_new(image):
    """Given PIL Image, returns average value of grayscale value."""
    return statistics.mean(image.getdata())
# getAverageNew
# def getInputSize(filename):
#     """
#     Given user input file gets tuple of image w and h
#     """


def convert_image_to_ascii(filename, cols, scale, morelevels):
    # convertImageToAscii
    """
    Given Image and dimensions (rows, cols) returns an m*n list of strings
    representing the ascii image.
    """
    # declare globals
    global gscale1, gscale2
    # open image and convert to grayscale
    image = Image.open(filename).convert('L')
    # store dimensions
    W, H = image.size[0], image.size[1]
    # init_size = (W, H)
    print('input image dims: %d x %d' % (W, H))
    # compute width of tile
    w = W / cols
    # compute tile height based on aspect ratio and scale
    h = w / scale
    # compute number of rows
    rows = int(H / h)

    print('cols: %d, rows: %d' % (cols, rows))
    print('tile dims: %d x %d' % (w, h))

    # check if image size is too small
    if cols > W or rows > H:
        print('Image too small for specified cols!')
        exit(0)

    # ascii image is a list of character strings
    aimg = []
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        # correct last tile
        if j == rows - 1:
            y2 = H
        # append an empty string
        aimg.append('')
        for i in range(cols):
            # crop image to tile
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            # correct last tile
            if i == cols - 1:
                x2 = W
            # crop image to extract tile
            img = image.crop((x1, y1, x2, y2))
            # get average luminance
            avg = int(get_average_new(img))
            # look up ascii char
            if morelevels:
                gsval = gscale1[int((avg * 69) / 255)]
            else:
                gsval = gscale2[int((avg * 9) / 255)]
            # append ascii char to string
            aimg[j] += gsval

    # return txt ascii image list of strs as aimg
    # format aimg here
    aimg_list_with_linebreak = [line + '\n' for line in aimg]
    ascii_str = ''.join(aimg_list_with_linebreak)
    # print('W, H below________________________________')
    # print(W, H)
    return ascii_str, (W, H)


def convert_text_to_png(ascii_str, size):
    """
    Given size makes blank img, writes list of strings onto image as image data
    and returns ascii img object
    """
    print('ascii_img below________________________________')
    print(type(ascii_str), ascii_str)
    im = Image.new('RGBA', size, (255, 0, 0, 0))

    draw = ImageDraw.Draw(im)
    draw.text((20, 20), ascii_str, fill='purple')
    print(im)
    ascii_img_obj = im
    # im.save('drawtext2.png')
    return ascii_img_obj

    # background_img_obj = backround.open()


# main() function
def main():
    """main function takes parser args and outputs .txt file"""
    # create parser
    descstr = 'This program converts an image into ASCII art.'
    parser = argparse.ArgumentParser(description=descstr)
    # add expected arguments
    parser.add_argument('--file', dest='img_file', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='out_file', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels', dest='morelevels', action='store_true')

    # parse args
    args = parser.parse_args()

    img_file = args.img_file
    # set output file
    out_file = 'out.txt'
    if args.out_file:
        out_file = args.out_file
    # set scale default as 0.43 which suits a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    # set cols
    cols = 80
    if args.cols:
        cols = int(args.cols)

    print('generating ASCII art...')
    # convert image to ascii txt
    aimg = convert_image_to_ascii(img_file, cols, scale, args.morelevels)

    # open file
    f = open(out_file, 'w')
    # write to file
    for row in aimg:
        f.write(row + '\n')
    # cleanup
    f.close()
    print('ASCII art written to %s' % out_file)

# call main
if __name__ == '__main__':
    main()
