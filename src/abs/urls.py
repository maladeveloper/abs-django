"""abs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import os
import sys
#from abs_immigration.views import secondary_immigration_detail_view
from abs_immigration.views import abs_form_create_view
from abs_immigration.views import dynamic_lookup_view
from abs_immigration.views import abs_immigration_list_view

urlpatterns = [
    #path('',secondary_immigration_detail_view, name='home'),
    path('',abs_form_create_view),
    path('admin', admin.site.urls),
    path('data/<int:my_id>',dynamic_lookup_view),
    path('listdata', abs_immigration_list_view)
]
