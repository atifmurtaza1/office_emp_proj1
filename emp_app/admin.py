from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name','location',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','dept','salary','bonus','role','phone',)
    change_form_template = 'change_form.html'
