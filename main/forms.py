from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """Subscribe Form by email"""
    class Meta:
        model = Contact
        fields = '__all__'
