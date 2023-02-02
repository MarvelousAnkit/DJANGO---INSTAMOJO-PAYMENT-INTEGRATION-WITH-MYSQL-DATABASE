"""website URL Configuration

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
from django.contrib import admin"""

from django.urls import path
from .views import home, success,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,pri,ref,tnc,contact
urlpatterns = [

    path('' , home, name="home"),
    path('success' , success, name="success"),
    path('r1',r1,name="r1"),
    path('r2' , r2 ,name="r2"),
    path('r3' , r3 ,name="r3"),
    path('r4' , r4 ,name="r4"),
    path('r5' , r5 ,name="r5"),
    path('r6' , r6 ,name="r6"),
    path('r7' , r7 ,name="r7"),
    path('r8' , r8 ,name="r8"),
    path('r9' , r9 ,name="r9"),
    path('r10' , r10 ,name="r10"),
    path('privacy/' , pri , name='priv'),
    path('refund/' , ref , name='ref'),
    path('tnc/' , tnc , name='tnc'),
    path('contact/' , contact , name='contact'),


]
