import os

from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'You have subscribed to the newsletter',
        'We will send a lot of spam)',
        os.environ['EMAIL_HOST_USER'],
        [user_email],
        fail_silently=False,
    )
