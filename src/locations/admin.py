from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import Address,Box,LivingUnit,GeographicalUnit,City,Country,Continent

# Register your models here.

class CountryInline(TabularInline):
    # extra = 1
    model = Country
    fk_name = 'IsPartOf'
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields["GeographicalUnitName"].label = "CountryName"
    #     form.base_fields["GeographicalUnitShortName"].label = "CountryShortName"
    #     form.base_fields["IsPartOf"].label = "Continent"
    #     return form


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin): 
    inlines = [CountryInline]
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["GeographicalUnitName"].label = "ContinentName"
        form.base_fields["GeographicalUnitShortName"].label = "ContinentShortName"
        form.base_fields["IsPartOf"].label = "Earth"
        return form

    fields = ['ContinentCode','GeographicalUnitName','GeographicalUnitShortName','IsPartOf','EntryStatus']
    list_display = ['ContinentCode','EntryStatus','GeographicalUnitName','GeographicalUnitShortName','IsPartOf','id']



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
    fields = ['CountryCode','IsPartOf','GeographicalUnitName','ISO3CountryCode','GeographicalUnitShortName','PhonePrefix','InternetSuffix','EntryStatus']
    list_display = ['CountryCode','EntryStatus','GeographicalUnitName','ISO3CountryCode','GeographicalUnitShortName','PhonePrefix','InternetSuffix','id']



@admin.register(City)
class CityAdmin(admin.ModelAdmin): 
    # model = City

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["GeographicalUnitName"].label = "CityName"
        form.base_fields["GeographicalUnitShortName"].label = "CityShortName"
        form.base_fields["IsPartOf"].label = "Country"
        return form
    fields = ['CityCode','GeographicalUnitName','GeographicalUnitShortName','IsPartOf','EntryStatus']
    list_display = ['CityCode',
                    'hierarchy',
                    'geographicalunitname',
                    'ispartof','EntryStatus',
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
    list_display =  ('GeographicalUnitId','GeographicalUnitName','EntryStatus','GeographicalUnitShortName','GeographicalUnitCategory','hierarchy',
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

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    pass
    fields = ('AddressId','IsPartOf','BoxReference',
        ('BoxDepth','BoxEntryWidth','BoxEntryHeight')
        ,'BoxDescription'
        ,('created_by','updated_by')
        # ,('updated','created')
    )
    list_display = ('AddressId','IsPartOf','BoxReference'
        ,'BoxDepth','BoxEntryWidth','BoxEntryHeight'
        ,'created_by','updated_by'
        ,'updated','created'
        ,'id'
    )
  
@admin.register(LivingUnit)
class LivingUnitAdmin(admin.ModelAdmin):
    fields = ('AddressId','IsPartOf'
        ,('Buidling','Floor','AppartmentReference')
        ,('created_by','updated_by')
        # ,('updated','created')
    )
    list_display= ('AddressId','IsPartOf'
        ,'Building','Floor','AppartmentReference'
        ,'created_by','updated_by'
        ,'updated','created'
        ,'id'
    )

class LivingUnitInline(TabularInline):
    model= LivingUnit

class BoxInline(TabularInline):
    # extra = 1
    model = Box

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    # inlines = [BoxInline,LivingUnitInline]
    fields = ('AddressId'
        ,('AddressType','SequenceNumber')
        ,('Street','HouseNumber')
        ,'AdditionalAddressLine'
        ,('PostalCode','PostBoxNumber')
        ,('City','Region')
        ,'Country'
        ,('Latitude','Longitude')
        # ,('updated','created')
        ,('created_by','updated_by')
    )
    list_display= ('AddressId','AddressType','SequenceNumber'
        ,'Street','HouseNumber'
        ,'AdditionalAddressLine'
        ,'City'
        ,'Country'
        ,'Latitude','Longitude'   
        ,'updated','created'
        ,'created_by','updated_by',
        ,'id'
    )
    
