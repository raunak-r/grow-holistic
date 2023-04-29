from django.contrib import admin
from .models import customer,event,booking
# Register your models here.

class customerAdmin(admin.ModelAdmin):
    list_display=['customer_id','customer_name','customer_email','phone']

class eventAdmin(admin.ModelAdmin):
    list_display=['event_id','event_name','event_date','event_cost'] 

class bookingAdmin(admin.ModelAdmin):
    list_display=['booking_id','date_of_booking','count','customer_id','event_id']


admin.site.register(customer,customerAdmin)
admin.site.register(event,eventAdmin) 
admin.site.register(booking,bookingAdmin)   