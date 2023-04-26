"""TemplateProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from MyApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tempinherit/',views.f1),
    path('tempinherit1/',views.f11),
    path('demo1/',views.demo1),
    path('demo2/',views.demo2),
    path('demo3/', views.demo3,name='d3'),
    path('thankyou/',views.thankyou,name='thanq'),
    path('thankyou2/<v1>/<v2>/', views.thankyou2, name='thankyou2'),
]
