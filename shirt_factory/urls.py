"""shirt_factory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^alldesigns$', views.render_all_designs, name='all'),
    url(r'^post$', views.render_post_page, name='post'),
    url(r'^post/submit$', views.render_submit, name='submit'),
    url(r'^post/preview$', views.render_preview, name='preview'),
    url(r'^design/(?P<design_id>\d+)$', views.render_design_page, name='design'),
    url(r'^design/image/(?P<design_id>\d+)$', views.render_design_image, name='image'),
    url(r'^design/thumb/(?P<design_id>\d+)$', views.render_design_thumb_image, name='thumb')
]
