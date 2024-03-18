from django.contrib import admin
from .models import *

class Educational_BackgroundInline(admin.TabularInline):
    model = Educational_Background
    extra = 1

class otherProfessionalSkillInline(admin.TabularInline):
    model = otherProfessionalSkill
    extra = 1

class professionalSkillsInline(admin.TabularInline):
    model = professionalSkills
    extra = 1

class relgiousOrPolictsInline(admin.TabularInline):
    model = relgiousOrPolicts
    extra = 1

class refrenceInline(admin.TabularInline):
    model = refrence
    extra = 1

class DocumentsInline(admin.StackedInline):
    model = Documents
    readonly_fields = ['id_card','photo','documents','teaching','skills']
    max_num = 1

@admin.register(Personal_Information)
class Personal_InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'registration_num' ,'full_name', 'cnic', 'gender', 'date_of_birth', 'contact_number')
    inlines = [Educational_BackgroundInline,otherProfessionalSkillInline,professionalSkillsInline,relgiousOrPolictsInline
               ,refrenceInline,DocumentsInline]  # Use the inline class here
    readonly_fields = ['registration_num']

