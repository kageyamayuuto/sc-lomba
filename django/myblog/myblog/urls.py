"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# import settings.py
from django.conf import settings
from django.views import static as django_static
from django.conf.urls.static import static

import os

from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home),
    path('post/?<single>', blog_views.single, name='single'),
    path('category/?<category>', blog_views.archive, name='category'),
    path("show/", blog_views.imageDownload, name='imgdownload'),
    path("images/<path>", blog_views.single, name='image')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

