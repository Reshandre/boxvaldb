from django import forms
from .models import *


class CountryForm(forms.ModelForm):
    class Meta:
        model= Country
        fields='__all__'