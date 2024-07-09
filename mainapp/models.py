from django.db import models

# Create your models here.


class AbstractBaseModel(models.Model):
    updated_date = models.DateTimeField(blank=True, auto_now=True, verbose_name='Updated Date', help_text='Updated Date',)
    created_date = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Created Date', help_text='Created Date',)

    class Meta:
        abstract = True


class GeneralSetting(AbstractBaseModel):
    name = models.CharField(default='', max_length=100, blank=True, verbose_name='Name', help_text='Name',)
    description = models.CharField(default='', max_length=254, blank=True, verbose_name='Description', help_text='Description',)
    parameters = models.TextField(default='',max_length=254, blank=True, verbose_name='Parameters', help_text='Parameters',)

    def __str__(self):
        return f'General Settings: {self.name}'

    class Meta:
        verbose_name = 'General Settings'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class ImageSetting(AbstractBaseModel):
    name = models.CharField(default='', max_length=100, blank=True, verbose_name='Name', help_text='Name',)
    description = models.CharField(default='', max_length=254, blank=True, verbose_name='Description', help_text='Description',)
    image = models.ImageField(default='', upload_to='images/', blank=True, verbose_name='Image', help_text='Image',)

    def __str__(self):
        return f'Image Settings: {self.name}'

    class Meta:
        verbose_name = 'Image Settings'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)