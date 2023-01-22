import os

from django.core.mail import send_mail

from .models import Contact
from .service import send
from send_email.celery import app


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'You have subscribed to the newsletter',
            'We will send a lot of spam every minute)',
            os.environ['EMAIL_HOST_USER'],
            [contact.email],
            fail_silently=False,
        )
