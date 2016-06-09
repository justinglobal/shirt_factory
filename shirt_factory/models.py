"""Models.py for shirt_factory project"""

from django.db import models


class ShirtDesign(models.Model):
    """Creates and defines ShirtDesign class."""

    design_name = models.TextField()
    comment = models.TextField()
    time_stamp = models.DateTimeField()
    input_img_file = models.ImageField()
    ascii_str = models.TextField()

    def __str__(self):
        """Format str to show design name and time stamp"""
        return '{} - {}'.format(self.design_name, self.time_stamp)

    def __repr__(self):
        """Format repr to show all saved database fields"""
        return 'ShirtDesign(design_name={!r}, comment={!r}, time_stamp={!r}, input_img_file={!r}, ascii_str={!r})'.format(
            self.design_name,
            self.comment,
            self.time_stamp,
            self.input_img_file,
            self.ascii_str,
        )
