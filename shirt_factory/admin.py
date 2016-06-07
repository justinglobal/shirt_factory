"""admin.py for shirt_factory"""

from django.contrib import admin

from . import models

admin.site.register(models.ShirtDesign)
