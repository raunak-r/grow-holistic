"""
URL configuration for djRms project.

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
from django.contrib import admin
from django.urls import path
from mytables import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rests/<str:city_name>/', views.get_queryset, name='rests_by_city'),
    path('items/', views.get_items, name='items'),
    path('items/<str:rest_name>', views.get_itemsbyrests),
    path('users/', views.get_users.as_view(), name='users'),
    path('users/create/', views.create_user.as_view(), name='create_user'),
    path('users/<int:pk>/delete/', views.delete_user, name='delete_user'),
    path('user/<int:pk>/update/', views.update_user.as_view(), name='update_user'),
]



