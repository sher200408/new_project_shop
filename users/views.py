import threading

from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import RegisterForms
from users.models import CustomUserModel
from users.utils import send_email_verification


def register_view(request):
    if request.method == "GET":
        return render(request, 'auth/register.html')

    elif request.method == "POST":
        form = RegisterForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(raw_password=form.cleaned_data['password2'])
            user.save()

            email_thread = threading.Thread(target=send_email_verification, args=(user, request,))
            email_thread.start()

            messages.success(request, "Please confirm your email and login")
            return redirect('users:login')
        else:
            messages.error(request, form.errors)
            return render(request, 'auth/register.html', {'form': form})


def confirm_email(request,uid,token):
    try:
        user = CustomUserModel.objects.get(id=uid)
    except CustomUserModel.DoesNotExist:
        return redirect('users:login')
    if default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request, "your email address is login")
        return redirect('user:login')
    else:
        messages.success(request, "link is not correst")
        return redirect('user:login')