from django import forms

from pages.models import CantactModel

"""
modelform 
form
"""

class ContactForm(forms.ModelForm):

    class Meta:
        model = CantactModel
        fields = '__all__'
