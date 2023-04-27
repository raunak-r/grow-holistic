from django.contrib import admin
from .models import supplier, product, customer, order

# Register your models here.
admin.site.register(supplier)
admin.site.register(product)
admin.site.register(customer)
admin.site.register(order)