"""juzgadosonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# def index(request):
# 	return render(request, 'home/index.html')

urlpatterns = [
    # path('avatar/', include('avatar.urls')),
    # path('', index(), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('select2/', include('django_select2.urls')),
    path('', include('expedientes.urls')),
    path('', include('juzgados.urls')),
    path('', include('extractor.urls')),
]
