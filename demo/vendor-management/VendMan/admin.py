from django.contrib import admin
from .models import supplier, product, customer, order

# Register your models here.
class supplierAdmin(admin.ModelAdmin):
    list_display = ['supplier_id', 'supplier_name', 'contact_person', 'address', 'phone', 'email']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'supplier_id', 'description', 'category', 'price']

class customerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'first_name', 'last_name', 'address', 'phone', 'email']

class orderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer_id', 'product_id', 'quantity', 'order_date', 'total_cost']


admin.site.register(supplier, supplierAdmin)
admin.site.register(product, ProductAdmin)
admin.site.register(customer, customerAdmin)
admin.site.register(order, orderAdmin)