from django.db import models

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
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees', null=True)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='employees')
    phone = models.CharField(max_length=12, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
