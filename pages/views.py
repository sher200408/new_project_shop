from dbm import error

from django.shortcuts import render
from pyexpat.errors import messages

from pages.forms import ContactForm
from pages.models import CantectModel


def home_page_view(request):
    return render(request, 'index.html')


def about_page_view(request):
    return render(request, 'pages/about.html')

def contact_page_view(request):
    if request.method == 'GET':
        return render(request, 'pages/contact.html')
    elif request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Your contact information is sent to database ")
            return render(request, 'pages/contact.html')
        else:
            messages.error(request, "Something getting wrong please try again later")
            return render(request,'pages/contact.html')





def shop_page_view(request):
    return render(request, 'pages/product_detail.html')
