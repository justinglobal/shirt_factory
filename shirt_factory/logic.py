"""
logic.py file for shirt_factory project
"""

from . import models
from . import ascii

import datetime
from PIL import Image

def get_all_designs():
    """gets all design objects from the db and reverse orders by timestamp"""
    return models.ShirtDesign.objects.all().order_by('time_stamp').reverse()

def make_time_stamp():
    time_raw = datetime.datetime.now()
    time_stamp = time_raw.isoformat()
    return time_stamp

def create_design_from_image(design_name, time_stamp, input_img_file, comment):
    ascii_str = ascii.convertImageToAscii(input_img_file, 100, .4, False)

    new_design = models.ShirtDesign(
        design_name=design_name,
        time_stamp=time_stamp,
        ascii_str=ascii_str,
        comment=comment,
    )

    new_design.save()
    return new_design

def create_preview_from_image(input_img_file):
    ascii_str = ascii.convertImageToAscii(input_img_file, 100, .4, False)
    image_size = (800, 800)
    ascii_img_obj = ascii.convert_text_to_png(ascii_str, image_size)
    return ascii_img_obj

def get_design_by_id(id):
    return models.ShirtDesign.objects.get(id=id)

def create_png_from_design(design):
    # image_check = Image.open(image)
    # image_size = image_check.size
    # print('image size:' , image_size)
    image_size = (800, 800)
    ascii_img_obj = ascii.convert_text_to_png(design.ascii_str, image_size)
    print('_________________________________________________')
    print(ascii_img_obj.format)
    print('_________________________________________________')
    return ascii_img_obj

# def create_thumb_from_ascii_img_obj(ascii_img_obj):
#     ascii_img_thumb_obj = ascii_img_obj.resize((100, 100))
#
def create_thumb_png_from_design(design):
    image_size = (100, 100)
    # Image.resize(size, resample=0)
    ascii_img_thumb_obj = ascii.convert_text_to_png(design.ascii_str, image_size)
    return ascii_img_thumb_obj
