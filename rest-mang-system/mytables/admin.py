from django.contrib import admin
from .models import rest,item,discount,user,order
# Register your models here.

admin.site.register(rest)
admin.site.register(item)
admin.site.register(discount)
admin.site.register(user)
admin.site.register(order)