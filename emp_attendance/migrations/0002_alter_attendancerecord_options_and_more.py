# Generated by Django 5.0.3 on 2024-03-25 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendancerecord',
            options={'verbose_name_plural': 'Add Attendence'},
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='shift',
            field=models.CharField(choices=[('morning', 'Morning Shift'), ('evening', 'Evening Shift')], max_length=10, null=True),
        ),
    ]
