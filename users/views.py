import threading

from pyexpat.errors import messages

from django.shortcuts import render, redirect

from users.forms import RegisterForms
from django.contrib import messages

from users.utils import send_email_verification


# Create your views here.
def register_view(request):
    if request.method == "GET":
        return render(request, 'auth/register.html')
    elif request.method == "POST":
        data = request.POST
        form = RegisterForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(raw_password=data['password1'])
            user.save()

            email_thread = threading.Thread(target=send_email_verification, args=(user,request,))
            email_thread.start()

            messages.success(request, "Please confirm your email and login")
            return redirect('users:login')
        else:
            messages.error(request, form.error_messages)
            return render(request, 'auth/register.html')
