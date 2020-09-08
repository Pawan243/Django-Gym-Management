"""GMS URL Configuration

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
from django.urls import path
from gym.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home, name='home'),
    path('about/',About, name = 'about'),
    path('contact/',Contact, name = 'contact'),
    path('admin_login',Login, name='login'),
    path('logout',Logout, name='logout'),
    path('add_enquiry/',Add_Enquiry,name='add_enquiry'),
    path('view_enquiry/',View_Enquiry,name='view_enquiry'),
    path('delete_enquiry(?p<int:pid>)', Delete_Enquiry, name='delete_enquiry'),
    path('add_equipment/',Add_Equipment,name='add_equipment'),
    path('view_equipment/',View_Equipment,name='view_equipment'),
    path('delete_equipment(?p<int:pid>)', Delete_Equipment, name='delete_equipment'),
]
 