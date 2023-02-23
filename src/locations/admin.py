from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import Address,GeographicalUnit,City,Country,Continent

# Register your models here.

class CountryInline(TabularInline):
    # extra = 1
    model = Country
    fk_name = 'IsPartOf'
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["GeographicalUnitName"].label = "CountryName"
        form.base_fields["GeographicalUnitShortName"].label = "CountryShortName"
        form.base_fields["IsPartOf"].label = "Continent"
        return form


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin): 
    inlines = [CountryInline]
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["GeographicalUnitName"].label = "ContinentName"
        form.base_fields["GeographicalUnitShortName"].label = "ContinentShortName"
        form.base_fields["IsPartOf"].label = "Earth"
        return form

    fields = ['ContinentCode','GeographicalUnitName','GeographicalUnitShortName','IsPartOf']
    list_display = ['ContinentCode','GeographicalUnitName','GeographicalUnitShortName','IsPartOf','id']



class CityInline(TabularInline):

    # extra = 1
    model = City
    fk_name = 'IsPartOf'



@admin.register(Country)
class CountryAdmin(admin.ModelAdmin): 
    inlines = [CityInline]
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["GeographicalUnitName"].label = "CountryName"
        form.base_fields["GeographicalUnitShortName"].label = "CountryShortName"
        form.base_fields["IsPartOf"].label = "Continent"
        return form
    fields = ['CountryCode','IsPartOf','GeographicalUnitName','ISO3CountryCode','GeographicalUnitShortName','PhonePrefix','InternetSuffix']
    list_display = ['CountryCode','GeographicalUnitName','ISO3CountryCode','GeographicalUnitShortName','PhonePrefix','InternetSuffix','id']



@admin.register(City)
class CityAdmin(admin.ModelAdmin): 
    # model = City

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["GeographicalUnitName"].label = "CityName"
        form.base_fields["GeographicalUnitShortName"].label = "CityShortName"
        form.base_fields["IsPartOf"].label = "Country"
        return form
    fields = ['CityCode','GeographicalUnitName','GeographicalUnitShortName','IsPartOf']
    list_display = ['CityCode',
                    'hierarchy',
                    'geographicalunitname',
                    'ispartof',
    ]
    @admin.display(description='hierarchy')
    def hierarchy(self,obj):
        return f'{obj.HierarchyLevel}'
    @admin.display(description='CityName')
    def geographicalunitname(self,obj):
        return f'{obj.GeographicalUnitName}'
    @admin.display(description='ispartof')
    def ispartof(self,obj):
        return f'{obj.IsPartOf.GeographicalUnitName}'
        
class GeographicalUnitInline(TabularInline):
    # extra = 1
    model = GeographicalUnit

@admin.register(GeographicalUnit)
class GeographicalUnitAdmin(admin.ModelAdmin):
    inlines = [GeographicalUnitInline]
    fields = ('GeographicalUnitId','GeographicalUnitName','GeographicalUnitShortName','IsPartOf','GeographicalUnitCategory','HierarchyLevel','id')
    list_display =  ('GeographicalUnitId','GeographicalUnitName','GeographicalUnitShortName','GeographicalUnitCategory','hierarchy',
                    'IsPartOf','id')
    @admin.display(description='hierarchy')
    def hierarchy(self,obj):
        return f'{obj.HierarchyLevel}'
    @admin.display(description='CityName')
    def geographicalunitname(self,obj):
        return f'{obj.GeographicalUnitName}'
    @admin.display(description='ispartof')
    def ispartof(self,obj):
        return f'{obj.IsPartOf.GeographicalUnitName}'

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = (
        ('AddressType','SequenceNumber')
        ,('Street','HouseNumber')
        ,'AdditionalAddressLine'
        ,('PostalCode','PostBoxNumber')
        ,('City','Region')
        ,'Country'
        ,('Latitude','Longitude')
        ,'GPSCoordinate'
    )
