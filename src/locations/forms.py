from django import forms
from .models import (Address, Country)



class CountryForm(forms.ModelForm):
    class Meta:
        model= Country
        fields='__all__'
        
class AddressForm(forms.ModelForm):
    class Meta:
        model= Address
        fields=['AddressType','SequenceNumber'
        ,'Street','HouseNumber'
        ,'AdditionalAddressLine'
        ,'PostalCode','PostBoxNumber'
        ,'City','Region'
        ,'Country'
        ,'Latitude','Longitude'
        ,'created_by','updated_by']
        
    def __init__(self,*args,**kwargs):
        super(AddressForm,self).__init__(*args,**kwargs)
        readOnlyFields = [ 'created_by','updated_by']
        onchangeFields = ['City']
        for visible in self.visible_fields():
            if visible.field.label not in readOnlyFields:
                visible.field.widget.attrs['class'] = 'form-control'
                visible.field.widget.attrs['placeholder'] = visible.field.label
            else:
                visible.field.widget.attrs['class'] = 'form-control-plaintext'
                # visible.field.widget.attrs['placeholder'] = visible.field.label
            if visible.field.label in onchangeFields:
                pass
                visible.field.widget.attrs['onchange'] = 'onchangeInputCity()'
                
        
    def save(self):
        pass
        super(AddressForm,self).save()

        