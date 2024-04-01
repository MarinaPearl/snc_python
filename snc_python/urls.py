"""
URL configuration for snc_python project.

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

from snc_python_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diplom/', views.diplom, name="home"),
    path('diplom_1/', views.diplom_1, name="home"),
    path('diplom_2/', views.diplom_2, name="home"),
    path('diplom_3/', views.diplom_3, name="home"),
    path('getProductWithCondition/', views.getProductWithCondition, name="home"),
    path('getSetsHair/', views.getSetsHair, name="home"),
]
