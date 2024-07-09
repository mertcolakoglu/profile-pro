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
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class ImageSetting(AbstractBaseModel):
    name = models.CharField(default='', max_length=100, blank=True, verbose_name='Name', help_text='Name',)
    description = models.CharField(default='', max_length=254, blank=True, verbose_name='Description', help_text='Description',)
    image = models.ImageField(default='', upload_to='images/', blank=True, verbose_name='Image', help_text='Image',)

    def __str__(self):
        return f'Image Settings: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)


class SkillSetting(AbstractBaseModel):
    skill = models.CharField(default='', max_length=254, blank=True, verbose_name='Skill', help_text='Skill',)
    description = models.CharField(default='', max_length=254, blank=True, verbose_name='Description', help_text='Description',)
    percentage = models.IntegerField(default=0, blank=True, verbose_name='Percentage', help_text='Percentage',)

    def __str__(self):
        return f'Skill Settings: {self.skill}'

    class Meta:
        verbose_name = 'Skill Setting'
        verbose_name_plural = 'Skill Settings'
        ordering = ('skill', )


class ExperienceSetting(AbstractBaseModel):
    company_name = models.CharField(default='', max_length=254, blank=True, verbose_name='Company Name', help_text='Company Name',)
    job_position = models.CharField(default='', max_length=254, blank=True, verbose_name='Job Position', help_text='Job Position',)
    job_location = models.CharField(default='', max_length=254, blank=True, verbose_name='Job Location', help_text='Job Location',)
    start_date = models.DateField(verbose_name='Start Date', help_text='Start Date',)
    end_date = models.DateField(default=None, null=True, blank=True, verbose_name='End Date', help_text='End Date',)

    def __str__(self):
        return f'Experience Settings: {self.company_name}'

    class Meta:
        verbose_name = 'Experience Setting'
        verbose_name_plural = 'Experience Settings'
        ordering = ('-start_date', )