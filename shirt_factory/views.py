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

    time_stamp = logic.make_time_stamp()

    design = logic.create_design_from_image(design_name, time_stamp, image)
    print(design)
    png_out = logic.create_png_from_design(design)

    template_args = {
        'design_name': design_name,
        'text_image': text_image,
        'time_stamp': time_stamp,
        'image': image,
        'png_out': png_out,
        'design': design,
    }

    return render(request, 'shirt_factory/design.html', template_args)

def render_design_image(request, design_id):
    design = logic.get_design_by_id(design_id)
    print(design.ascii_img)
    png_out = logic.create_png_from_design(design)
    print(png_out)
    resp = HttpResponse(content_type='image/png')
    png_out.save(resp, format='png')
    return resp
