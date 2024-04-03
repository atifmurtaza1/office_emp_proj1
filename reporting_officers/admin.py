from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

@admin.register(Data)
class DataAdmin(ImportExportModelAdmin):
    list_display = [
        'id','full_name','gender','date_of_birth','email',
    ]
