from django.contrib import admin
from .models import Department
from .models import Employees
from .models import Employee_Contact


# Register your models here.
admin.site.register(Department)
admin.site.register(Employees)
admin.site.register(Employee_Contact)
