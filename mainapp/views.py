from django.shortcuts import render

from mainapp.models import GeneralSetting


def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameters
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameters
    site_description = GeneralSetting.objects.get(name='site_description').parameters
    home_banner_person_name = GeneralSetting.objects.get(name='home_banner_person_name').parameters
    home_banner_job_position = GeneralSetting.objects.get(name= 'home_banner_job_position').parameters
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameters
    about_myself_welcome_2 = GeneralSetting.objects.get(name='about_myself_welcome').parameters
    about_myself_welcome_3 = GeneralSetting.objects.get(name='about_myself_welcome').parameters

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_person_name': home_banner_person_name,
        'home_banner_job_position': home_banner_job_position,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_welcome_2': about_myself_welcome_2,
        'about_myself_welcome_3': about_myself_welcome_3,

    }

    return render(request, 'index.html', context=context)

