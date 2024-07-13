from django.contrib import admin
from mainapp.models import *

# Register your models here.


@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'description', 'parameters', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameters', 'updated_date', 'created_date']
    list_editable = ('description', 'parameters')

    class Meta:
        model = GeneralSetting


@admin.register(PersonalInformationSetting)
class PersonalInformationSettingsAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'firt_parameter', 'second_parameter', 'order', 'updated_date', 'created_date']
    search_fields = ['name', 'firt_parameter', 'second_parameter', 'order']
    list_editable = ('firt_parameter', 'second_parameter', 'order')

    class Meta:
        model = PersonalInformationSetting


@admin.register(ImageSetting)
class ImageSettingsAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'description', 'image', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'image']
    list_editable = ('description', 'image')

    class Meta:
        model = ImageSetting


@admin.register(SkillSetting)
class SkillSettingsAdmin(admin.ModelAdmin):

    list_display = ['id', 'skill', 'description', 'percentage', 'updated_date', 'created_date']
    search_fields = ['skill', 'description', 'percentage']
    list_editable = ('skill', 'description', 'percentage')

    class Meta:
        model = SkillSetting


@admin.register(ExperienceSetting)
class ExperienceSettingsAdmin(admin.ModelAdmin):

    list_display = ['id', 'company_name', 'job_position', 'job_location', 'start_date', 'end_date']
    search_fields = ['company_name', 'job_position', 'job_location']
    list_editable = ('company_name', 'job_position', 'job_location', 'start_date', 'end_date')

    class Meta:
        model = ExperienceSetting


@admin.register(EducationSetting)
class EducationSettingsAdmin(admin.ModelAdmin):

    list_display = ['id', 'school_name', 'major', 'department', 'start_date', 'end_date']
    search_fields = ['school_name', 'major', 'department']
    list_editable = ('school_name', 'major', 'department', 'start_date', 'end_date')

    class Meta:
        model = EducationSetting


@admin.register(SocialMediaSetting)
class SocialMediaSettingsAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'url', 'icon', 'updated_date', 'created_date']
    search_fields = ['name', 'url', 'icon']
    list_editable = ('name', 'url', 'icon')

    class Meta:
        model = SocialMediaSetting
