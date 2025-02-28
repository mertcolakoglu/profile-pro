from django.shortcuts import render, redirect, get_object_or_404

from mainapp.models import (GeneralSetting, ImageSetting, SkillSetting, ExperienceSetting,
                            EducationSetting, SocialMediaSetting, PersonalInformationSetting, UploadSetting)


def layout(request):
    # General Settings
    site_title = GeneralSetting.objects.get(name='site_title').parameters
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameters
    site_description = GeneralSetting.objects.get(name='site_description').parameters
    home_banner_person_name = GeneralSetting.objects.get(name='home_banner_person_name').parameters
    home_banner_job_position = GeneralSetting.objects.get(name='home_banner_job_position').parameters
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameters

    # Personal Information Settings
    personal_information = PersonalInformationSetting.objects.all()

    # Image Settings
    home_banner_person_image = ImageSetting.objects.get(name='home_banner_person_image').image
    favicon_image = ImageSetting.objects.get(name='favicon_image').image
    home_logo_image = ImageSetting.objects.get(name='home_logo_image').image

    # Upload Settings
    upload_file = UploadSetting.objects.all()

    # Social Media Settings
    social_media = SocialMediaSetting.objects.all()
    portfolio = SocialMediaSetting.objects.get(name='github_repo').url

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_person_name': home_banner_person_name,
        'home_banner_job_position': home_banner_job_position,
        'about_myself_welcome': about_myself_welcome,
        'home_banner_person_image': home_banner_person_image,
        'favicon_image': favicon_image,
        'home_logo_image': home_logo_image,
        'upload_file': upload_file,
        'personal_information': personal_information,
        'social_media': social_media,
        'portfolio': portfolio,
    }
    return context


def index(request):

    # Skills Settings
    skills = SkillSetting.objects.all().order_by('-percentage')

    # Experience Settings
    experiences = ExperienceSetting.objects.all().order_by('-start_date')

    # Education Settings
    educations = EducationSetting.objects.all().order_by('-start_date')

    context = {
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
    }

    return render(request, 'index.html', context=context)


def redirect_urls(request, slug):
    doc = get_object_or_404(UploadSetting, slug=slug)
    return redirect(doc.file.url)
