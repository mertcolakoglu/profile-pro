# Generated by Django 5.0.6 on 2024-07-13 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_generalsetting_parameters'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformationSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, help_text='Updated Date', verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Created Date', verbose_name='Created Date')),
                ('name', models.CharField(blank=True, default='', help_text='Name', max_length=100, verbose_name='Name')),
                ('firt_parameter', models.CharField(blank=True, default='', help_text='First Parameter', max_length=254, verbose_name='First Parameter')),
                ('second_parameter', models.CharField(blank=True, default='', help_text='Second Parameter', max_length=254, verbose_name='Second Parameter')),
            ],
            options={
                'verbose_name': 'Personal Information Setting',
                'verbose_name_plural': 'Personal Information Settings',
                'ordering': ('name',),
            },
        ),
    ]
