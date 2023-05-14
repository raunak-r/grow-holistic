from django.db import models


# Create your models here.
class Department(models.Model):
    d_id = models.BigAutoField(primary_key=True)
    d_name = models.CharField(max_length=100, null=False)
    d_location = models.CharField(max_length=100)

    def __str__(self):
        return self.d_name
class Roles(models.Model):
    role_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    emp_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    Hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.phone)
