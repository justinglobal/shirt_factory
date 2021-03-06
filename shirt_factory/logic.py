"""logic.py file for shirt_factory project"""

import datetime


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


def get_design_by_id(id):
    """Given uid gets design from model for that id."""
    return models.ShirtDesign.objects.get(id=id)


def create_design_from_image(design_name, time_stamp, input_img_file, comment):
    """
    Given design name, timestamp, comment, and input img file make ascii text
    image and saves design to database.
    """
    ascii_str = ascii.convert_image_to_ascii(input_img_file, 160, .4, False)

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
    img obj for preview
    """
    ascii_str = ascii.convert_image_to_ascii(input_img_file, 260, .4, False)
    image_size = ascii.get_img_size_from_ascii_str(ascii_str)
    ascii_img_obj = ascii.convert_ascii_str_to_png(ascii_str, image_size)
    return ascii_img_obj


def create_png_from_design(design):
    """Given design obj gets ascii_str from design and makes img obj of str."""
    image_size = ascii.get_img_size_from_ascii_str(design.ascii_str)
    ascii_img_obj = ascii.convert_ascii_str_to_png(
        design.ascii_str, image_size)
    return ascii_img_obj


def create_thumb_png_from_ascii_img_obj(design):
    """
    Given design obj gets ascii_str from design and makes img obj then resizes
    to thumb size.
    """
    image_size = ascii.get_img_size_from_ascii_str(design.ascii_str)
    thumb_size = 128, 128
    ascii_img_obj = ascii.convert_ascii_str_to_png(
        design.ascii_str, image_size)
    ascii_img_thumb_obj = ascii_img_obj.copy()
    ascii_img_thumb_obj.thumbnail(thumb_size)
    return ascii_img_thumb_obj
