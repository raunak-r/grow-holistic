"""
URL configuration for FlightMngSys project.

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
from flightsApp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/', views.user_list),
    path('user/create/', views.create_user),
    path('airline/', views.airline_list),
    path('city/', views.city_list),
    path('flight/', views.flight_list),
    path('flight/<str:arr_city>/<str:dep_city>/', views.target_flight_list),      #arr = arival_city,  dep = departure_city
    path('flight/<str:name>/', views.airline_flight_list),
    path('booking/', views.booking_list),
    path('booking/<int:id>/', views.user_booking_list),
    path('booking/create', views.create_booking),
]

urlpatterns = format_suffix_patterns(urlpatterns)