from django.db import models

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
    IsPartOf = models.ForeignKey("self",on_delete=models.SET_NULL,#related_name='composition',
    blank=True, null=True,
    help_text='Select a the geographical Unit it belogs to')
    ENTRY_STATUS_CHOICES = (
       ('T', 'Geo Location can change'),
        ('D', 'Geo Location Official')
    )
    EntryStatus= models.CharField(max_length=15,choices=ENTRY_STATUS_CHOICES, default='D')

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
        return f'{self.CountryShortName} ({self.CountryCode})'
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
    
    
    def __str__(self):
        return f'{self.id} {self.CityName} {self.CityCode}'
    
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
    
    def save(self,*args,**kwargs):
        self.GeographicalUnitCategory = 'City'
        self.CityCode = self.CityCode.upper().replace(' ','_')
        self.GeographicalUnitId = self.GeographicalUnitCategory+'_'+self.CityCode
        self.HierarchyLevel = 40
        return super(City,self).save(*args,**kwargs)


class Address(models.Model):

    ADDRESS_TYPES = (
    ('MainResidentialAddress', 'Residential address of Person'),
    ('BoxMainAccessPlace', 'Place where the boxes are located'),
    ('AddressOfHeadquarters', 'Addess of headquarter'),
    ('Other','Other type of address')
)
    AddressType = models.CharField(max_length=40,default = 'BoxMainAccessPlace',choices=ADDRESS_TYPES,help_text='Enter selection:')
    SequenceNumber = models.IntegerField(help_text='address sequence number')
    Street = models.CharField(max_length=256,help_text='Street :')
    HouseNumber = models.CharField(max_length=10, help_text= 'House number :')
    PostBoxNumber = models.CharField(blank=True,max_length=40, help_text= 'Post Box Number :')
    AdditionalAddressLine = models.CharField(blank=True,max_length=60, help_text='Additional Address Line :')
    PostalCode = models.CharField(max_length=10,help_text='Postal Code:')
    City = models.CharField(null=True,blank=True,max_length=256,help_text = 'City:')
    Region = models.CharField(null=True,max_length=20,help_text ='Postal Code:')
    Country = models.ForeignKey(Country,on_delete=models.DO_NOTHING,blank=True,null=True,help_text = 'Enter a country:')
    Latitude = models.DecimalField(null=True,max_digits=20, decimal_places=6,help_text='Latitude (parallel to equator):')
    Longitude = models.DecimalField(null=True,max_digits=20, decimal_places=6,help_text='Longitude (Through Nord and south Pole)):')    

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
        return f'{self.AddressType} - {self.SequenceNumber} - {self.Street}'