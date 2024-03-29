"""
URL configuration for mywebsite project.

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
# from mywebsite import views
from formapp2 import views


urlpatterns = [
    path("secure/", admin.site.urls),
    path("",views.newuser, name='regis'),
    path("login/",views.custom_login, name='index'),
    # path("loginsucc/",views.success, name='success'),
    # path("calculator/",views.calculator,name='calculator'),
    # path("evenodd/",views.evenoff,name='calculator'),
    # path("marksheet/",views.marksheet),
    # path("input/",views.incert),
   
    # path("register/",views.register, name='contact'),
    # path("password/",views.password, name='password'),
    # path("login/",views.login, name='login'),
]
