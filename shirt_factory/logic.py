"""
logic.py file for shirt_factory project
"""

from . import models
from . import ascii

import datetime
from PIL import Image

def get_all_designs():
    """gets all design objects from the db and reverse orders by timestamp"""
    return models.Design.objects.all().order_by('time_stamp').reverse()

# def create_and_save_new_design(design_name, text_image):
#
#     time_raw = datetime.datetime.now()
#     time_stamp = time_raw.isoformat()
#
#     new_design = models.Design(
#         design_name=design_name,
#         text_image=text_image,
#         time_stamp=time_stamp,
#         )
#
#     new_design.save()
#     return time_stamp

def make_time_stamp():
    time_raw = datetime.datetime.now()
    time_stamp = time_raw.isoformat()
    return time_stamp

def create_design_from_image(design_name, time_stamp, image):
    ascii_img = ascii.convertImageToAscii(image, 100, .4, False)
    # print(ascii_img)

    new_design = models.Design(
        design_name=design_name,
        time_stamp=time_stamp,
        ascii_img=ascii_img,
    )

    new_design.save()
    return new_design

def create_png_from_design(design):
    # image_check = Image.open(image)
    # image_size = image_check.size
    # print('image size:' , image_size)
    image_size = (800, 800)
    ascii_png = ascii.convert_text_to_png(design.ascii_img, image_size)
    print(ascii_png)
    return ascii_png

def get_design_by_id(id):
    return models.Design.objects.get(id=id)
