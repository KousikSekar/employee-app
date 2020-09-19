from django.db import models


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=50)
    manager = models.CharField(max_length=25)


class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    doj = models.DateField(max_length=10)
    dob = models.DateField(max_length=10)
    designation = models.CharField(max_length=25)
    dept_id = models.ForeignKey(Department, related_name='department' ,on_delete=models.CASCADE)


class Employee_Contact(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    employee_id = models.ForeignKey(Employees, related_name='contact',on_delete=models.CASCADE)

    class Meta:
        unique_together = ['address', 'phone']


