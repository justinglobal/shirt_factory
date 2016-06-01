from django.db import models

import datetime
from PIL import Image

class ShirtDesign(models.Model):

    design_name = models.TextField(unique=True)
    comment = models.TextField()
    time_stamp = models.DateTimeField()
    input_img_file = models.ImageField()
    ascii_str = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.design_name, self.time_stamp)

    def __repr__(self):
        return 'ShirtDesign(design_name={!r}, comment={!r}, time_stamp={!r}, input_img_file={!r}, ascii_str={!r})'.format(
            self.design_name,
            self.comment,
            self.time_stamp,
            self.input_img_file,
            self.ascii_str,
        )
