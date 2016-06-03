"""
shirt_factory views.py
"""

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from io import BytesIO
import base64

from . import logic

def render_all_designs(request):
    """
    Gets all designs from logic and prepares them for rendering page
    """
    all_designs = logic.get_all_designs()

    template_args = {
        'all_designs': all_designs,
    }
    return render(request, 'shirt_factory/all.html', template_args)

def render_post_page(request):
    """
    Renders post.html page for uploading designs.
    """
    return render(request, 'shirt_factory/post.html', {})

def render_submit(request):
    """
    Gets arguments for design, makes design, returns redirect URL with ID
    """
    design_name = request.POST['design_name']
    comment = request.POST['comment']
    input_img_file = request.FILES['input_img_file']
    time_stamp = logic.make_time_stamp()
    design = logic.create_design_from_image(design_name, time_stamp, input_img_file, comment)

    return redirect('design', design_id=design.id)

def render_preview(request):
    """
    Gets user input image, creates img obj from input image, encodes img obj in base64 and serves encoded string to JS for rendering in browser.
    """
    input_img_file = request.FILES['input_img_file']
    ascii_img_obj = logic.create_preview_from_image(input_img_file)
    ascii_img_file = BytesIO()
    ascii_img_obj.save(ascii_img_file, format='png')
    ascii_img_file_b64 = base64.b64encode(ascii_img_file.getvalue())
    return HttpResponse(ascii_img_file_b64)

def render_design_page(request, design_id):
    """
    Given design id gets design from database
    """
    design = logic.get_design_by_id(design_id)

    template_args = {
        'design': design,
    }
    return render(request, 'shirt_factory/design.html', template_args)

def render_design_image(request, design_id):
    """
    Given design id gets design, makes design into img obj, and creates img file for rendering to browser
    """
    design = logic.get_design_by_id(design_id)
    print(design.ascii_str)
    ascii_img_obj = logic.create_png_from_design(design)
    print(ascii_img_obj)
    ascii_img_file = HttpResponse(content_type='image/png')
    ascii_img_obj.save(ascii_img_file, format='png')
    return ascii_img_file

def render_design_thumb_image(request, design_id):
    """
    Given design id gets design, makes design into img obj, and creates thumb size img file for rendering to browser
    """
    design = logic.get_design_by_id(design_id)
    print(design.ascii_str)
    ascii_img_thumb_obj = logic.create_thumb_from_ascii_img_obj(design)
    ascii_img_thumb_file = HttpResponse(content_type='image/png')
    ascii_img_thumb_obj.save(ascii_img_thumb_file, format='png')
    return ascii_img_thumb_file
