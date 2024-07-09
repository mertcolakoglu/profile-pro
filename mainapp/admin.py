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


@admin.register(ImageSetting)
class ImageSettingsAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'description', 'image', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'image']
    list_editable = ('description', 'image')

    class Meta:
        model = ImageSetting
