from django.db import models
from reporting_officers.models import *

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)


    def __str__(self):
        return self.name


class Employee(models.Model):

    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    SYED = 'Syed'
    MIRZA = 'Mirza'
    NONSYED = 'Non-Syed'

    CASTE_CHOICE = [
        (SYED, 'Syed'),
        (MIRZA, 'Mirza'),
        (NONSYED, 'Non Syed'),
    ]
    Title = models.CharField(max_length=10,choices=CASTE_CHOICE,default=NONSYED)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees', null=True)
    salary = models.IntegerField(default=0, verbose_name='Salary Cap')
    bonus = models.IntegerField(default=0, verbose_name='Basic Salary')
    allowance = models.IntegerField(default=0, verbose_name='Total Daily Allowance', null=True)  # Corrected field name
    officers = models.ForeignKey(Data, on_delete=models.CASCADE, verbose_name='Reporting Officer', null=True)  # Updated field
    FLEXIBLE = 'Flexible'
    FOUR = '4'
    EIGHT = '8'
    WORK_HOURS = [
        (FLEXIBLE,'Flexible'),
        (FOUR, '4'),
        (EIGHT, '8'),
    ]
    allowed_working_hours = models.CharField(max_length=8,null=True,choices=WORK_HOURS)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='employees')

    phone = models.CharField(max_length=12, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
