from django import forms

from pages.models import CantectModel

"""
modelform 
form
"""

class ContactForm(forms.ModelForm):

    class Meta:
        model = CantectModel
        fields = '__all__'
