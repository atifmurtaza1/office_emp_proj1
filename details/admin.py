from django.contrib import admin
from django.forms import ModelForm
from django.conf import settings
from .models import *

class Educational_BackgroundInline(admin.StackedInline):
    model = Educational_Background
    extra = 1

class otherProfessionalSkillInline(admin.StackedInline):
    model = otherProfessionalSkill
    extra = 1

class professionalSkillsInline(admin.StackedInline):
    model = professionalSkills
    extra = 1

class relgiousOrPolictsInline(admin.StackedInline):
    model = relgiousOrPolicts
    extra = 1

class refrenceInline(admin.StackedInline):
    model = refrence
    extra = 1

class DocumentsInline(admin.StackedInline):
    model = Documents
    # readonly_fields = ['id_card','photo','documents','teaching','skills']
    max_num = 1

class ResignationInline(admin.StackedInline):
    model = Resignation
    fk_name = 'personal_inf'

    max_num = 1

@admin.register(Personal_Information)
class Personal_InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'registration_num' ,'full_name', 'cnic', 'gender', 'date_of_birth', 'contact_number')
    inlines = [Educational_BackgroundInline,otherProfessionalSkillInline,professionalSkillsInline,relgiousOrPolictsInline
               ,refrenceInline,DocumentsInline,ResignationInline]  # Use the inline class here
    readonly_fields = ['registration_num']
    change_form_template = 'change_form.html'


    # formfield_overrides = {
    #     models.CharField: {'widget': InputMaskWidget(mask='(999) 999-9999')},
    #     models.DateField: {'widget': InputMaskWidget(mask='99/99/9999')},
    # }
    # class Media:
    #     js = (
    #         'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js',  # Add this line
    #         'js/admin_custom.js',
    #     )
