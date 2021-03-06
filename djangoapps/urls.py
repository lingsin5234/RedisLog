"""djangoapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path

from RedisLog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('django-rq/', include('django_rq.urls')),
    re_path(r'^redis-queue/', views.view_redis_queue),
    re_path(r'ajax/load-result/', views.load_result, name='ajax_load_result'),
    re_path(r'^redis/ocr-submit-request/', views.submit_ocr_request, name='ocr-submit-request')
]
