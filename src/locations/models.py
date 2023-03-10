# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()
from django.db import models
import uuid

from django.conf import settings


ENTRY_STATUS_CHOICES = (
    ('T', 'Geo Location can change'),
    ('D', 'Geo Location Official')
    )
# Create your models here.
class GeographicalUnit(models.Model):

    GeographicalUnitId = models.CharField(max_length=15,help_text='Political Unit:')
    GEOGRAPHICAL_UNIT_CATEGORIES = (
        ('Planet','Planet'),
        ('Continent','Continent'),
        ('Sea','Sea'),
        ('Ocean','Ocean'),
        ('Country','Country'),
        ('State','State'),
        ('City','City'),
        ('Commune','Commune')
    )
    GeographicalUnitCategory=models.CharField(max_length=15,choices=GEOGRAPHICAL_UNIT_CATEGORIES)
    GeographicalUnitName = models.CharField(max_length=100)
    GeographicalUnitShortName = models.CharField(max_length=100)
    HierarchyLevel= models.IntegerField(default=0)
    IsPartOf = models.ForeignKey("self",on_delete=models.SET_NULL,
    blank=True, null=True, help_text='Select a the geographical Unit it belogs to')
    EntryStatus= models.CharField(max_length=15,choices=ENTRY_STATUS_CHOICES, default='T')

    def __str__(self):
        return f'{self.GeographicalUnitCategory} - {self.GeographicalUnitName}'
    class Meta:
        # https://docs.djangoproject.com/en/4.1/ref/models/options/
        permissions = [('can_manage_locations', 'Can manage locations')]
        constraints =  [
            models.UniqueConstraint(fields=['IsPartOf','GeographicalUnitId'], name='locations_geographicalunit_unique_code'),
            models.UniqueConstraint(fields=['IsPartOf','GeographicalUnitName'], name='locations_geographicalunit_unique_name'),        
            models.UniqueConstraint(fields=['IsPartOf','GeographicalUnitShortName'], name='locations_geographicalunit_unique_short_name'),        ]


        
class Continent(GeographicalUnit):
    ContinentCode = models.CharField(max_length=2,help_text='Code for Continent :')

    @property
    def ContinentName(self):
        return self.GeographicalUnitName
    @ContinentName.setter
    def ContinentName(self,value):
        self.GeographicalUnitName = value
    @ContinentName.deleter
    def ContinentName(self):
        del self.GeographicalUnitName
    @property
    def ContinentShortName(self):
        return self.GeographicalUnitShortName
    @ContinentShortName.setter
    def ContinentShortName(self,value):
        self.GeographicalUnitShortName = value
    @ContinentShortName.deleter
    def ContinentShortName(self):
        del self.GeographicalUnitShortName

    def save(self,*args,**kwargs):
        self.GeographicalUnitCategory = 'Continent'
        self.ContinentCode = self.ContinentCode.upper()
        self.GeographicalUnitId = self.GeographicalUnitCategory+'_'+self.ContinentCode
        self.HierarchyLevel = 20
        # self.IsPartOf = 'Planet_Earth'

        return super(Continent,self).save(*args,**kwargs)
    

class Country(GeographicalUnit):
    CountryCode = models.CharField(max_length=2,help_text='Iso2 Code for country :')
    ISO3CountryCode = models.CharField(max_length=3,help_text='Iso3 Code for Country :') 
    PhonePrefix = models.CharField(max_length=10,blank=True,help_text='Phone Code for Country :',null=True) 
    InternetSuffix = models.CharField(max_length=200,blank=True,help_text='Internet suffix Code for Country with dot (example .fr) :',null=True) 
    ISO3166Country = models.CharField(max_length=3,help_text='Iso316 Code for Country :',null=True) 

    class Meta:
        ordering = ['GeographicalUnitName','IsPartOf',]

    
    @property
    def CountryName(self):
        return self.GeographicalUnitName
    @CountryName.setter
    def CountryName(self,value):
        self.GeographicalUnitName = value
    @CountryName.deleter
    def CountryName(self):
        del self.GeographicalUnitName

    @property
    def CountryShortName(self):
        return self.GeographicalUnitShortName
    @CountryShortName.setter
    def CountryShortName(self,value):
        self.GeographicalUnitShortName = value
    @CountryShortName.deleter
    def CountryShortName(self):
        del self.GeographicalUnitShortName

    def __str__(self):
        return f'{self.CountryShortName} ({self.CountryCode}) - {self.IsPartOf.GeographicalUnitName} '
    def save(self,*args,**kwargs):
        self.GeographicalUnitCategory = 'Country'
        self.CountryCode = self.CountryCode.upper()
        self.GeographicalUnitId = self.GeographicalUnitCategory+'_'+self.CountryCode
        self.ISO3CountryCode = self.ISO3CountryCode.upper()
        self.HierarchyLevel = 30
        return super(Country,self).save(*args,**kwargs)

class City(GeographicalUnit):
    CityCode = models.CharField(max_length=100,help_text='Code for city :')
    # PostalCode = models.CharField(max_length=10,help_text='Postal Code:')
    
    

    @property
    def CityName(self):
        return self.GeographicalUnitName
    @CityName.setter
    def CityName(self,value):
        self.GeographicalUnitName = value
    @CityName.deleter
    def CityName(self):
        del self.GeographicalUnitName

    @property
    def CityShortName(self):
        return self.GeographicalUnitShortName
    @CityShortName.setter
    def CityShortName(self,value):
        self.GeographicalUnitShortName = value
    @CityShortName.deleter
    def CityShortName(self):
        del self.GeographicalUnitShortName

    def __str__(self):
        return f'{self.CityName} - {self.IsPartOf.GeographicalUnitName} '
        
    def save(self,*args,**kwargs):
        self.GeographicalUnitCategory = 'City'
        self.CityCode = self.CityCode.upper().replace(' ','_')
        self.GeographicalUnitId = self.GeographicalUnitCategory+'_'+self.CityCode
        self.HierarchyLevel = 40
        return super(City,self).save(*args,**kwargs)


class GeneralAddress(models.Model):
    AddressId = models.CharField(unique=True,max_length=128,# default=uuid.uuid4, 
                                 help_text= 'Unique visible number location')
    SequenceNumber = models.IntegerField(default=1,help_text='address sequence number')
    ADDRESS_CATEGORIES = (
        ('Address','Address as managed by postal service'),
        ('box','Place of a box in an address'),
    )
    AddressCategory = models.CharField(max_length=40,default = 'UnSpecified', choices=ADDRESS_CATEGORIES,help_text='Enter selection:')
    AccessCodes = models.CharField(null=True,blank=True,max_length=100,help_text = 'AccessCodes:')
    EntryStatus= models.CharField(max_length=15,choices=ENTRY_STATUS_CHOICES, default='D')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
    
def generate_AddressId(obj,city,country,street):
    # generate_AddressId(self,self.City,self.Country,self.Street)
    
    suf  = f"_{'' if not hasattr(obj,'Country') else obj.Country.CountryCode}"
    suf += f"_{'' if not hasattr(obj,'City') else obj.City.CityCode}"
    suf += f"_{'' if not hasattr(obj,'Street') else obj.Street}"
    suf += f"_{str(uuid.uuid4())[0:8]}"
    return suf
    
    
    
class Address(GeneralAddress):
    ADDRESS_TYPES = (
        ('UnSpecified', 'The type of address is not specified'),
        ('MainResidentialAddress', 'Residential address of Person'),
        ('BoxMainAccessPlace', 'Place where the boxes are located'),
        ('AddressOfHeadquarters', 'Addess of headquarter'),
        ('Other','Other type of address')
    )
    AddressType = models.CharField(max_length=40,default = 'UnSpecified', choices=ADDRESS_TYPES,help_text='Enter selection:')
    Street = models.CharField(max_length=256,help_text='Street :')
    HouseNumber = models.CharField(max_length=10, help_text= 'House number :')
    PostBoxNumber = models.CharField(max_length=40, help_text= 'Post Box Number :',blank=True)
    AdditionalAddressLine = models.CharField(blank=True,max_length=60, help_text='Additional Address Line :')
    PostalCode = models.CharField(max_length=10,help_text='Postal Code:',blank=True)
    City = models.ForeignKey(City,on_delete=models.DO_NOTHING,blank=True,null=True,help_text = 'Select a city or add one:')
    Region = models.CharField(null=True,blank=True,max_length=20,help_text ='Postal Code:')
    Country = models.ForeignKey(Country,on_delete=models.DO_NOTHING,blank=True,null=True,help_text = 'Enter a country:')
    Latitude = models.DecimalField(null=True,blank=True,max_digits=19, decimal_places=16,help_text='Latitude (parallel to equator):')
    Longitude = models.DecimalField(null=True,blank=True,max_digits=19, decimal_places=16,help_text='Longitude (Through Nord and south Pole)):')    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name= 'addressCreated_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False) 
    @property
    def GPSCoordinate(self):
        return f"{self.Latitude}, {self.Longitude}"
    
    @GPSCoordinate.setter
    def GPSCoordinate(self,value):
        self.Latitude, self.Longitude = value.split(',')
    
    @GPSCoordinate.deleter
    def GPSCoordinate(self):
        del self.Latitude
        del self.Longitude

    class Meta:
        ordering = ['Country','City','Street']
    
    def __str__(self):
        return f'{self.AddressId} - {self.AddressType} - {self.Street}'
    
    def save(self,*args,**kwargs):
        self.AddressCategory ='Address'
        if self.id is None:
            suf = generate_AddressId(self,self.City,self.Country,self.Street)
            self.AddressId = f"{self.AddressCategory}_{suf}"

        if len(self.AddressId) < 2:
            suf = generate_AddressId(self,self.City,self.Country,self.Street)
            self.AddressId = f"{self.AddressCategory}_{suf}"

        return super(Address,self).save(*args,**kwargs)
    
class Box(GeneralAddress):
    IsPartOf = models.ForeignKey(Address,on_delete=models.SET_NULL,
    blank=True, null=True,
    help_text='Select ')
    BoxReference = models.CharField(null=True,blank=True,max_length=100,help_text = 'BoxReference:')
    BoxDepth = models.DecimalField(max_digits=8,decimal_places=2,help_text='The depth of the box')
    BoxEntryWidth = models.DecimalField(max_digits=8,decimal_places=2,help_text='The width of the box')
    BoxEntryHeight = models.DecimalField(max_digits=8,decimal_places=2,help_text='The height of the box')
    BoxDescription = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name= 'boxCreated_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False) 

    def __str__(self):
        return f'{self.AddressId} - {self.BoxReference} - {self.IsPartOf.AddressId} - {self.IsPartOf.Street} '
    
    def save(self,*args,**kwargs):
        pass
        self.AddressCategory ='Box'
        self.AddressId = f"{self.AddressCategory}_{uuid.uuid4()}"
        return super(Box,self).save(*args,**kwargs)


class LivingUnit(GeneralAddress):
    IsPartOf = models.ForeignKey(Address,on_delete=models.SET_NULL,
    blank=True, null=True,
    help_text='Select ')
    Building = models.CharField(null=True,blank=True,max_length=40,help_text = 'Building:')
    Floor = models.CharField(null=True,blank=True,max_length=20,help_text = 'Floor:')
    AppartmentReference = models.CharField(null=True,blank=True,max_length=50,help_text = 'Appartment Reference:')
    AppartmentDescription = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name= 'livingUnitCreated_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False) 

    def __str__(self):
        return f'{self.AddressId} - {self.AppartmentReference} - {self.IsPartOf.SequenceNumber} - {self.IsPartOf.Street}'
    
    def save(self,*args,**kwargs):
        pass
        self.AddressCategory ='LivingUnit'
        self.AddressId = f"{self.AddressCategory}_{uuid.uuid4()}"
        return super(Address,self).save(*args,**kwargs)

