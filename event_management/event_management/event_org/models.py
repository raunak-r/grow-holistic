from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=100,blank=False)
    customer_email=models.EmailField(max_length=100,null=True,blank=False)
    phone=models.CharField(null=True,blank=False) 

    def __str__(self):
        return self.customer_name
    
    class Meta:
                ordering=["customer_id"]   

     

class event(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=100,blank=False)
    event_date = models.DateTimeField(null=True,auto_now_add=True)
    event_cost = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=False)

    def __str__(self):
        return self.event_name
    
    class Meta:
                ordering=["event_name"] 

class booking(models.Model):
    booking_id=models.AutoField(primary_key=True)
    date_of_booking=models.DateField(null=True,default='23-04-2023',blank=False)
    count=models.IntegerField(null=True,blank=False)
    customer_id=models.ForeignKey(customer,blank=False,null=True,on_delete=models.CASCADE)
    event_id=models.ForeignKey(event,blank=False,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.booking_id
    
    class Meta:
                ordering=["booking_id"]     