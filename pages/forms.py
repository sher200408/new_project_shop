from django import forms

"""
modelform 
form
"""

class ContactForm(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    text = forms.Textarea()

