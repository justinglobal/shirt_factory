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

def create_and_save_new_design(design_name, text_image):

    time_raw = datetime.datetime.now()
    time_stamp = time_raw.isoformat()

    new_design = models.Design(
        design_name=design_name,
        text_image=text_image,
        time_stamp=time_stamp,
        )

    new_design.save()
    return time_stamp

def create_design_from_image(design_name, image):
    ascii_img = ascii.covertImageToAscii(image, 80, .43, False)
    # print(ascii_img)
    new_design = models.Design(
        design_name=design_name,
        ascii_img=ascii_img,
    )

    new_design.save()
