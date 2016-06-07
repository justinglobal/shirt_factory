"""logic.py file for shirt_factory project"""

import datetime

# from PIL import Image

from . import ascii
from . import models


def get_all_designs():
    """Get all design objects from the db and reverse order by timestamp"""
    return models.ShirtDesign.objects.all().order_by('time_stamp').reverse()


def make_time_stamp():
    """Get timestamp and format to ISO format"""
    time_raw = datetime.datetime.now()
    time_stamp = time_raw.isoformat()
    return time_stamp


def create_design_from_image(design_name, time_stamp, input_img_file, comment):
    """
    Given design name, timestamp, comment, and input img file make ascii text
    image and saves design to database.
    """
    ascii_str, image_size = ascii.convert_image_to_ascii(input_img_file, 100, .4, False)
    print('print4______________________________________________')
    print(image_size)
    new_design = models.ShirtDesign(
        design_name=design_name,
        time_stamp=time_stamp,
        ascii_str=ascii_str,
        comment=comment,
    )

    new_design.save()
    return new_design


def create_preview_from_image(input_img_file):
    """
    Given input image, converts image to asccii str then makes str into
    image for preview
    """
    ascii_str, image_size = ascii.convert_image_to_ascii(input_img_file, 100, .4, False)
    # image_size = (800, 800)
    print('print3______________________________________________')
    # print(ascii.convert_image_to_ascii.init_size)
    print('print3______________________________________________')
    ascii_img_obj = ascii.convert_text_to_png(ascii_str, image_size)
    return ascii_img_obj


def get_design_by_id(id):
    """Given uid gets design from model for that id."""
    return models.ShirtDesign.objects.get(id=id)


def create_png_from_design(design):
    """Given design obj gets ascii_str from design and makes img obj of str."""
    # image_check = Image.open(image)
    # image_size = image_check.size
    # print('image size:' , image_size)
    image_size = (800, 800)
    ascii_img_obj = ascii.convert_text_to_png(design.ascii_str, image_size)
    print('print1______________________________________________')
    print(ascii_img_obj.format)
    print('_________________________________________________')
    return ascii_img_obj


def create_thumb_from_ascii_img_obj(design):
    """
    Given design obj gets ascii_str from design and makes img obj then resizes
    to thumb size.
    """
    image_size = (800, 800)
    # print('print2______________________________________________')
    # print(design.ascii_str)
    ascii_img_obj = ascii.convert_text_to_png(design.ascii_str, image_size)
    ascii_img_thumb_obj = ascii_img_obj.resize((100, 100))
    return ascii_img_thumb_obj

# def create_thumb_png_from_design(design):
#     image_size = (100, 100)
#     ascii_img_thumb_obj = ascii.convert_text_to_png(design.ascii_str, image_size)
#     return ascii_img_thumb_obj
