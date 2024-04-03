from django.db import models

# Create your models here.

class Data(models.Model):
    full_name = models.CharField(max_length=10)
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    date_of_birth = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.full_name