"""
URL configuration for Employee_Mang_SystemDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from . import views
from .views import EmployeeDetail, EmployeeInfo

urlpatterns = [
    path('', views.index, name='index'),
    path("emp/", EmployeeDetail.as_view(), name="emp"),
    path("emp/<int:id>/", EmployeeDetail.as_view()),
    path('emp_info/',  EmployeeInfo.as_view(), name='all_emp'),
    path('emp_info/<int:id>/', EmployeeInfo.as_view()),
    path('all_emp/', views.all_emp, name='all_emp'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('remove_emp/', views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>/', views.remove_emp, name='remove_emp'),
    path('filter_emp/', views.filter_emp, name='filter_emp'),

]
