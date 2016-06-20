"""
ascii.py
A python program that convert images to ASCII art.
"""

import statistics

from PIL import Image, ImageDraw

# ascii.py adapted from Python Playground by Mahesh Venkitachalam
# gray scale level values from:
# http://paulbourke.net/dataformats/asciiart/


def get_average_new(image):
    """Given PIL Image, returns average value of grayscale value."""
    return statistics.mean(image.getdata())


def convert_to_grayscale(filename):
    """Given png file, opens as PIL img and converts to 8-bit grayscale."""
    image = Image.open(filename).convert('L')
    return image


def get_input_dims(image):
    """Given PIL img gets input image width and height"""
    width_input_img, height_input_img = image.size[0], image.size[1]
    return width_input_img, height_input_img


def get_tile_dims(width_input_img, cols, scale):
    """
    Compute initial tile dimensions for string converstion given
    width_input_img, cols, and scale
    """
    width_tile = width_input_img / cols
    height_tile = width_tile / scale
    return width_tile, height_tile


def get_rows(height_input_img, height_tile):
    """
    Given height_input_img and height_tile computes number of rows of asccii
    chars.
    """
    rows = int(height_input_img / height_tile)
    return rows


def image_size_check(
    width_tile, height_tile,
    width_input_img, height_input_img,
    cols, rows, scale
):
    """
    Given tile width and height, input image width and height, number of cols
    and number of rows, checks size of output image, if input image dims are
    too small, sets output image to be same size as input image by setting cols
    to equal input image width then computes new tile width/height and rows.
    """
    if cols > width_input_img or rows > height_input_img:
        cols = width_input_img
        width_tile, height_tile = get_tile_dims(width_input_img, cols, scale)
        rows = get_rows(height_input_img, height_tile)
    return width_tile, height_tile, cols, rows


def get_char_list_from_tile_lum(
    image,
    width_tile, width_input_img, height_tile, height_input_img,
    cols, rows, morelevels
):
    """
    Given image tile width/height, input img width/height, # of cols and rows
    and # of grayscale levels, makes list of lists of chars representing each
    row from computed average luminace for coordinates of tile for each row.
    """
    ascii_list_of_rows = []
    # generate list of dimensions
    for row in range(rows):
        # get tile y coordinates
        y1 = int(row * height_tile)
        y2 = int((row + 1) * height_tile)
        # correct last tile
        if row == rows - 1:
            y2 = height_input_img
        # append an empty string
        ascii_list_of_rows.append('')
        for col in range(cols):
            # get tile x coordinates
            x1 = int(col * width_tile)
            x2 = int((col + 1) * width_tile)
            # correct last tile
            if col == cols - 1:
                x2 = width_input_img
            # crop image to extract tile from computed coordinates
            img = image.crop((x1, y1, x2, y2))
            # get average luminance of cropped tile
            avg = int(get_average_new(img))
            # look up ascii char based on average luminance of tile
            # 70 levels of gray
            gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<\
            >i!lI;:,\"^`'. "
            # 10 levels of gray
            gscale2 = '@%#*+=-:. '
            if morelevels:
                gsval = gscale1[int((avg * 69) / 255)]
            else:
                gsval = gscale2[int((avg * 9) / 255)]
            # append ascii char representing tile luminace to string
            ascii_list_of_rows[row] += gsval
    return ascii_list_of_rows


def get_str_from_char_list(ascii_list_of_rows):
    """
    Given ascii char list of rows, adds linebreak to end of each row and joins
    all rows into one string of ascii chars.
    """
    aimg_list_with_linebreak = [line + '\n' for line in ascii_list_of_rows]
    ascii_str = ''.join(aimg_list_with_linebreak)
    return ascii_str


def convert_image_to_ascii(filename, cols, scale, morelevels):
    """
    Given image file, cols, scale factor, and # of levels, makes string of
    ascii chars representing image.
    """
    image = convert_to_grayscale(filename)
    width_input_img, height_input_img = get_input_dims(image)
    width_tile, height_tile = get_tile_dims(width_input_img, cols, scale)
    rows = get_rows(height_input_img, height_tile)
    width_tile, height_tile, cols, rows = image_size_check(
        width_tile, height_tile,
        width_input_img, height_input_img,
        cols, rows, scale)
    ascii_list_of_rows = get_char_list_from_tile_lum(
        image,
        width_tile, width_input_img, height_tile, height_input_img,
        cols, rows, morelevels)
    ascii_str = get_str_from_char_list(ascii_list_of_rows)
    return ascii_str


def get_img_size_from_ascii_str(ascii_str):
    """Given ascii string calculates base image size using dims from font"""
    cols = len((ascii_str.split('\n'))[1])
    rows = ascii_str.count('\n')
    # derives width & height of base image from default font char dims:
    # width_tile = 6px, height_tile = (11 + 4(four spaces between rows))px
    w_base_img = cols * 6
    h_base_img = rows * 15
    image_size = w_base_img, h_base_img
    return image_size


def convert_ascii_str_to_png(ascii_str, size):
    """
    Given size makes blank img, writes list of strings onto image as image data
    and returns ascii img object
    """
    im = Image.new('RGBA', size, (255, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    draw.text((1, 1), ascii_str, fill='black')
    ascii_img_obj = im
    return ascii_img_obj
