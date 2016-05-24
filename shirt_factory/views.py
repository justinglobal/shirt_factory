"""
shirt_factory views.py
"""

from django.http import HttpResponse
from django.shortcuts import render

from . import logic

def render_all_designs(request):
    """gets all designs from logic and prepares them for rendering page"""
    all_designs = logic.get_all_designs()

    template_args = {
        'all_designs': all_designs,
    }
    return render(request, 'shirt_factory/all.html', template_args)

def render_post_page(request):
    return render(request, 'shirt_factory/post.html', {})

def render_design_page(request):

    design_name = request.POST['design_name']
    text_image = request.POST['text_image']
    # print(request.FILES)
    image = request.FILES['image']
    # time_stamp = logic.create_and_save_new_design(design_name, text_image)

    time_stamp = 0

    image_out = logic.create_design_from_image(design_name, image)

    template_args = {
        'design_name': design_name,
        'text_image': text_image,
        'time_stamp': time_stamp,
        'image': image,
        'image_out': image_out,
    }

    return render(request, 'shirt_factory/design.html', template_args)
