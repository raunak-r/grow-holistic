from django.contrib import admin
from .models import User, airline, city, flight, booking


# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'first_name', 'last_name', 'dob', 'passport_number', 'email', 'phone', 'address']
    list_per_page = 50


class airlineAdmin(admin.ModelAdmin):
    list_display = ['Airline_id', 'Airline_name', 'email', 'phone']
    list_per_page = 50


class cityAdmin(admin.ModelAdmin):
    list_display = ['city_code', 'city_name']
    list_per_page = 50


class flightAdmin(admin.ModelAdmin):
    list_display = ['filght_id', 'airline_name', 'arr_city', 'des_city', 'date', 'number_of_seats', 'price']
    list_per_page = 50


class bookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'flight_id', 'user_id', 'order_date', 'total_cost']
    list_per_page = 50


admin.site.register(User, userAdmin)
admin.site.register(airline, airlineAdmin)
admin.site.register(city, cityAdmin)
admin.site.register(flight, flightAdmin)
admin.site.register(booking, bookingAdmin)
