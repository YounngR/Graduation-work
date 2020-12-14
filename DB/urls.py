"""NOVA URL Configuration

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
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'DB'

urlpatterns = [
    path('',views.maintest,name="main"),
    path('map/',views.kakaomap,name="kakaomap"),
    path('camera/',views.camera,name="camera"),
    path('result/',views.result,name="result"),
    path('maintest/',views.maintest,name="maintest"),
    path('history/',views.history, name="history"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
