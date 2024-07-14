from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
import logging

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=254, required=True)
    email = forms.EmailField(max_length=254, required=True)
    subject = forms.CharField(max_length=254, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def send_mail(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            email = self.cleaned_data['email']
            subject = self.cleaned_data['subject']
            message = self.cleaned_data['message']
            message_context = f'Message received.\n\nName: {name}\nSubject: {subject}\nEmail: {email}\nMessage: {message}'

            email_message = EmailMessage(
                subject,
                message_context,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                reply_to=[email],
            )

            try:
                email_message.send()
                logger.info("Email sent successfully.")
            except Exception as e:
                logger.error(f"Error sending email: {e}")
