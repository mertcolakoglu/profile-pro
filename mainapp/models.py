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
    parameters = models.TextField(default='', blank=True, verbose_name='Parameters', help_text='Parameters',)

    def __str__(self):
        return f'General Settings: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class PersonalInformationSetting(AbstractBaseModel):
    name = models.CharField(default='', max_length=100, blank=True, verbose_name='Name', help_text='Name',)
    firt_parameter = models.CharField(default='', max_length=254, blank=True, verbose_name='First Parameter', help_text='First Parameter',)
    second_parameter = models.CharField(default='', max_length=254, blank=True, verbose_name='Second Parameter', help_text='Second Parameter',)
    order = models.IntegerField(default=0, blank=True, verbose_name='Order', help_text='Order',)

    def __str__(self):
        return f'Personal Information Settings: {self.name}'

    class Meta:
        verbose_name = 'Personal Information Setting'
        verbose_name_plural = 'Personal Information Settings'
        ordering = ('order',)


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


class EducationSetting(AbstractBaseModel):
    school_name = models.CharField(default='', max_length=254, blank=True, verbose_name='School Name', help_text='School Name',)
    major = models.CharField(default='', max_length=254, blank=True, verbose_name='Major', help_text='Major',)
    department = models.CharField(default='', max_length=254, blank=True, verbose_name='Department', help_text='Department',)
    start_date = models.DateField(verbose_name='Start Date', help_text='Start Date',)
    end_date = models.DateField(default=None, null=True, blank=True, verbose_name='End Date', help_text='End Date',)

    def __str__(self):
        return f'Education Settings: {self.school_name}'

    class Meta:
        verbose_name = 'Education Setting'
        verbose_name_plural = 'Education Settings'
        ordering = ('-start_date', )


class SocialMediaSetting(AbstractBaseModel):
    name = models.CharField(default='', max_length=100, blank=True, verbose_name='Name', help_text='Name',)
    url = models.URLField(default='', verbose_name='Url', help_text='Url',)
    icon = models.CharField(default='', max_length=254, blank=True, verbose_name='Icon', help_text='Icon',)

    def __str__(self):
        return f'Social Media Settings: {self.name}'

    class Meta:
        verbose_name = 'Social Media Setting'
        verbose_name_plural = 'Social Media Settings'
        ordering = ('name', )
