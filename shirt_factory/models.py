from django.db import models

import datetime
from PIL import Image

class Design(models.Model):

    design_name = models.TextField()
    text_image = models.TextField()
    time_stamp = models.DateTimeField()
    image = models.ImageField()
    ascii_img = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.design_name, self.time_stamp)

    def __repr__(self):
        return 'Design(design_name={!r}, text_image={!r}, time_stamp={!r}, image={!r}, ascii_img={!r})'.format(
            self.design_name,
            self.text_image,
            self.time_stamp,
            self.image,
            self.ascii_img,
        )
