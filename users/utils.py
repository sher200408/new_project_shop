

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.urls import reverse



def send_email_verification(user,request):
    token = default_token_generator(user)
    uid = user.pk

    confirmation_link = request.build_absolute_uri(
        reverse('user:confirm_email',kwargs ={'uid':uid, 'token':token})
    )

    subject  = "Confirm Your Email Address"

    message = render_to_string('auth/email_confirmation.html',{
        'user':user,
        'confirmation_link':confirmation_link,
    })

    send_mail(subject,message,settings.EMAIL_HOST_USER ,[user.email])