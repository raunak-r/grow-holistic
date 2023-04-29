from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100, blank=False)
    contact_person = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=500,null=True, blank=False)
    phone = models.CharField(null=True,blank = False)
    email = models.EmailField(max_length=100,null=True,blank = False)

    def __str__(self):
        return self.supplier_name
    
    class Meta:
		    ordering = ["supplier_name"]

# If blank=True then the field will not be required, whereas if it's False the field cannot be blank.
# The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('')
# CHAR and TEXT types are never saved as NULL by Django, so null=True is unnecessary.

class product(models.Model):
    product_id = models.AutoField (primary_key=True)
    product_name = models.CharField(max_length=100,null=True,)
    supplier_id = models.ForeignKey(supplier,on_delete=models.CASCADE,blank = False)
    description = models.CharField(max_length=500,null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank = False)
    price = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank = False)

    def __str__(self):
        return self.product_name
    
    class Meta:
		    ordering = ["product_name"]

class customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    customer_id = models.AutoField (primary_key=True)
    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200,null=True, blank=False)
    phone = models.CharField(null=True,blank=False)
    email = models.EmailField(max_length=100,null=True,blank = False)

    def __str__(self):
        return self.first_name
    
    class Meta:
		    ordering = ["first_name"]

class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE)
    product_id = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True,blank=False)
    order_date = models.DateTimeField(null=True,auto_now_add=True)
    total_cost = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=False)

    def __str__(self):
        return self.order_id

    class Meta:
		    ordering = ["order_id"]