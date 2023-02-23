from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(BusinessPartner)
class BusinessPartnerAdmin(admin.ModelAdmin):
    fields = ['BusinessPartnerId','BusinessPartnerclass','ConsumerStatus']
    list_display = ['__str__','BusinessPartnerId','BusinessPartnerclass','ConsumerStatus','id']
# admin.site.register(BusinessPartner,BusinessPartnerAdmin)
@admin.register(IndividualPerson)
class IndividualPersonAdmin(admin.ModelAdmin):
    fields = [
        ('Title','Consultation'),('GivenName','LastName','NameAtBirth'),
        ('Gender','MaritalStatus'),
        ('PlaceOfBirth','CountryOfBirth','Nationality','SecondNationality'),
        ('DateOfBirth')
    ]
    # list_display = ['BusinessPartnerId','BusinessPartnerclass','ConsumerStatus','id']

@admin.register(Organization)
class OrganizationPersonAdmin(admin.ModelAdmin):
    fields = [
        ('Name','LegalForm'),('DateOfIncorporation','CountryOfIncorporation'),('Register','PlaceOfRegister'),
        ('RoleInClearing')
    ]
    # list_display = ['BusinessPartnerId','BusinessPartnerclass','ConsumerStatus','id']
