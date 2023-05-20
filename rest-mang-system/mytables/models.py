from django.db import models


# Create your models here.

class rest(models.Model):
    restId = models.AutoField(primary_key='True')
    restName = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.restName


class item(models.Model):
    itemId = models.AutoField(primary_key='True')
    itemName = models.CharField(max_length=100, blank='False')
    itemPrice = models.FloatField(blank='False')
    restId = models.ForeignKey(rest, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName


class discount(models.Model):
    disId = models.AutoField(primary_key='True')
    itemId = models.ForeignKey(item, on_delete=models.PROTECT)
    disPrice = models.FloatField(blank='False')


class user(models.Model):
    userId = models.AutoField(primary_key='True')
    userName = models.CharField(max_length=100, blank='False')
    email = models.CharField(max_length=100, blank='False')

    def __str__(self):
        return self.userName


class order(models.Model):
    orderId = models.AutoField(primary_key='True')
    itemId = models.ForeignKey(item, on_delete=models.PROTECT)
    userId = models.ForeignKey(user, on_delete=models.CASCADE)
