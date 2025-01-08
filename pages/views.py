from dbm import error

from django.shortcuts import render

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
            date = forms.data
            CantectModel.objects.create(
                name=date['name'],
                email=date['email'],
                subject=date['subject'],
                text=date['text']
            )
            return render(request, 'pages/contact.html')
        else:
            context = {
                'errors':forms.errors
            }
            return render(request,'pages/contact.html',context)





def shop_page_view(request):
    return render(request, 'pages/product_detail.html')
