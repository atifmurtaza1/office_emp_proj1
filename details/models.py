from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime



# Create your models here.

class Personal_Information(models.Model):
    registration_num = models.CharField(max_length=10, unique=True, editable=False, verbose_name='Employee Id', null=True)

    def registration_number(self):
        current_year = datetime.now().year
        # Logic to generate registration number based on the year
        return f"{current_year}-{self.pk}"  # Example format: 2022-1, 2022-2, ...

    def save(self, *args, **kwargs):
        if not self.pk:  # Only generate registration number for new instances
            current_year = datetime.now().year
            last_registered = Personal_Information.objects.filter(registration_num__startswith=current_year).order_by(
                '-registration_num').first()
            if last_registered:
                last_number = int(last_registered.registration_num.split('-')[-1])
                self.registration_num = f"{current_year}-{last_number + 1}"
            else:
                self.registration_num = f"{current_year}-1"
        super().save(*args, **kwargs)

    full_name = models.CharField(max_length=100)
    cnic_regex = RegexValidator(
        regex=r'^\d{5}-\d{7}-\d{1}$',  # CNIC format: 00000-0000000-0
        message="CNIC must be in the format: '00000-0000000-0'",
    )
    cnic = models.CharField(max_length=15, validators=[cnic_regex])
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
    present_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$',  # Validates international phone numbers
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )
    ])
    alternate_contact = models.CharField(max_length=15, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$',  # Validates international phone numbers
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )
    ])
    email = models.EmailField()

    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Informations"  # Optional, for plural form

class Educational_Background(models.Model):
    personal_info = models.ForeignKey(Personal_Information, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100, verbose_name='Title of Degree/Certificate/Sanad')
    institue = models.CharField(max_length=100, verbose_name='Institute/Hoza/Madrasa')
    GRADE_CHOICE = [
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),

    ]
    grade = models.CharField(max_length=2, choices=GRADE_CHOICE)

    passing_year = models.DateField(null=True)

    class Meta:
        verbose_name = "Educational Background"
        verbose_name_plural = "Educational Background"  # Optional, for plural form


class otherProfessionalSkill(models.Model):
    personal_info = models.ForeignKey(Personal_Information, on_delete=models.CASCADE)

    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100, verbose_name='Organization/company/Employer Name')
    _from = models.CharField(max_length=100, verbose_name='From')
    to = models.CharField(max_length=100, verbose_name='To')

    class Meta:
        verbose_name = "Other Professional Skill"
        verbose_name_plural = "Other Professional Skills"  # Optional, for plural form


class professionalSkills(models.Model):
    personal_info = models.ForeignKey(Personal_Information, on_delete=models.CASCADE)

    description = models.CharField(max_length=1000, verbose_name='Description')

    class Meta:
        verbose_name = 'PROFESSIONAL SKILL'
        verbose_name_plural = 'PROFESSIONAL SKILLS'


class relgiousOrPolicts(models.Model):
    personal_info = models.ForeignKey(Personal_Information, on_delete=models.CASCADE)

    position = models.CharField(max_length=100)
    name = models.CharField(max_length=100, verbose_name='Name of party or association')
    _from = models.CharField(max_length=100, verbose_name='From')
    to = models.CharField(max_length=100, verbose_name='To')

    class Meta:
        verbose_name = 'RELIGIOUS OR Political Affiliation'
        verbose_name_plural = 'RELIGIOUS OR Political Affiliations'


class refrence(models.Model):
    personal_info = models.ForeignKey(Personal_Information, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    relation = models.CharField(max_length=100, verbose_name='Relation with applicant')
    contact_number = models.CharField(max_length=12, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$',  # Validates international phone numbers
            message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed."
        )
    ])

    class Meta:
        verbose_name = 'Reference'
        verbose_name_plural = 'References'


class Documents(models.Model):
    personal_info = models.ForeignKey(Personal_Information, on_delete=models.CASCADE)

    id_card = models.CharField(max_length=100, verbose_name='Copy of National ID card')
    photo = models.CharField(max_length=100, verbose_name='2 Passport Size Photographs')
    documents = models.CharField(max_length=100, verbose_name='Copy of all educational documents')
    teaching = models.CharField(max_length=100, verbose_name='Teaching Experience letter (if applicable)')
    skills = models.CharField(max_length=100, verbose_name='Skill certificates (if any)')
