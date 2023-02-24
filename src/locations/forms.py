from django import forms
from .models import (Address, Country)



class CountryForm(forms.ModelForm):
    class Meta:
        model= Country
        fields='__all__'
        
class AddressForm(forms.ModelForm):
    class Meta:
        model= Address
        fields='__all__'
        