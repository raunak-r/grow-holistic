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
from rest_framework.urlpatterns import format_suffix_patterns

from flightsApp import views


urlpatterns = format_suffix_patterns([
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),

    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),

    path('airlines/', views.AirlineList.as_view(), name='airline-list'),
    path('airlines/<int:pk>/', views.AirlineDetail.as_view(), name='airline-detail'),

    path('cities/', views.city_list, name='city-list'),
    path('cities/<int:pk>/', views.city_detail, name='city-detail'),

    path('flights/', views.flight_list, name='flight-list'),
    path('flights/<int:pk>/', views.flight_detail, name='flights-detail'),
    path('flights/<str:arr_city>/<str:dep_city>/', views.flights_between_cities, name='flights-between-cities'),
    path('flights/results/', views.flights_on_date, name='flights-on-date'),

    path('bookings/', views.booking_list, name='booking-list'),
    path('bookings/<int:pk>/', views.booking_detail, name='booking-detail'),
])
