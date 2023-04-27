from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class supplier(models.Model):
    supplier_id = models.IntegerField (primary_key='True')
    supplier_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    address = models.CharField
    phone = models.IntegerField
    email = models.EmailField

    def __str__(self):
        return self.supplier_name

class product(models.Model):
    product_id = models.IntegerField (primary_key='True')
    product_name = models.CharField(max_length=200)
    supplier_id = models.ForeignKey(supplier,on_delete=models.CASCADE)
    description = models.CharField
    category = models.CharField
    price = models.DecimalField

    def __str__(self):
        return self.product_name

class customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    customer_id = models.IntegerField (primary_key='True')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField
    phone = models.IntegerField
    email = models.EmailField

    def __str__(self):
        return self.first_name

class order(models.Model):
    order_id = models.IntegerField (primary_key='True')
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE)
    product_id = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField
    order_date = models.DateTimeField
    total_cost = models.DecimalField