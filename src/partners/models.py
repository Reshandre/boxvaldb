from email.policy import default
from django.db import models

from locations.models import Country,City
from .codes import *
import uuid
# Create your models here.
class BusinessPartner(models.Model):
    BusinessPartnerId = models.CharField(unique=True,max_length=128,default=uuid.uuid4,help_text= 'Unique visible number of Business partner')
    BUSINESSPARTNER_CLASSES= (
    ('IndividualPerson', 'IndividualPerson'),
    ('Organization', 'Organization'),
    ('Company','Company')
    )
    BusinessPartnerclass = models.CharField(max_length=20,default = '',choices=BUSINESSPARTNER_CLASSES)
    CONSUMERSTATUS = (
        ('Suspended','Suspended'),
        ('Actif','Acif'),
        ('Open','Open'),
    )
    ConsumerStatus=models.CharField(max_length=20,default='Open')
    

    class Meta:
        abstract = False

    def __str__(self):
        if (self.BusinessPartnerclass =='IndividualPerson'):
            givenName = IndividualPerson.objects.get(pk=self.pk).GivenName
            return f'{self.BusinessPartnerclass} - {givenName}'
        elif (self.BusinessPartnerclass =='Organization'):
            name = Organization.objects.get(pk=self.pk).Name
            return f'{self.BusinessPartnerclass} - {name}'
        elif (self.BusinessPartnerclass =='Company'):
            return f'{self.BusinessPartnerclass} - {self.BusinessPartnerId}'
        return f'{self.BusinessPartnerclass} - {self.BusinessPartnerId}'

class IndividualPerson(BusinessPartner):
    GivenName = models.CharField(max_length = 60,null=False,help_text='Enter First Name like Bob:')
    LastName  = models.CharField(max_length = 60,null=False,help_text='Enter Last Name like Hansen, Dupond, Lloyd, Kahn...:')
    TITLE = (
        ('Mr','Mister'),
        ('Mrs','refer to a married woman '),
        ('Miss','refer to a unmarried woman'),
        ('Ms','Refer to a woman w/o referring to Marital status '),       
        ('Dr','Doctor'),
        ('M','refer to neutral gender'),
        ('Sir','Sir'),
        ('Other','Other'),
    )
    Title     = models.CharField(max_length = 40,null=False,blank=True,default='M',choices=TITLE,help_text='Enter Title or Blank:')
    Consultation = models.CharField(max_length = 40, blank=True,help_text='Combined Title like Mr and Mrs Smith') 
    GENDER=(
        ('M','Man'),
        ('W','Woman'),
        ('T','Transgender'),
        ('N','Non-Binary/Non-Conforming'),
        ('Neutral','No particular gender'),
        ('P','Prefer not respond'),
        ('O','Other'),
    )
    Gender = models.CharField(max_length = 40,null=False,default='M',choices=GENDER,help_text='Select Gender, optional used for access recovery')
    NameAtBirth = models.CharField(max_length = 256,blank=True,help_text='Name before it changed because of Marriage')
    DateOfBirth = models.DateField(null=True,help_text='Date of birth, used for password recovery:')
    PlaceOfBirth = models.ForeignKey(City,blank=True,null=True,on_delete=models.DO_NOTHING,help_text='Place of Birth, used for password recovery:')
    MARITALSTATUS = (
        ('Single','Single'),
        ('Married','Married'),
        ('Widowed','Widowed'),
        ('Divorced','Divorced'),
        ('Separated','Separated'),
        ('NeverMarried','Never married'),
        ('Other','Never married'),
    )
    MaritalStatus = models.CharField(max_length = 40,blank=True,default='',choices=MARITALSTATUS,help_text='Select one of the options')
    EDUCATIONLEVEL = (
        ('X',' No schooling'),
        ('0', 'Early childhood education'),
        ('1', 'Primary education'),
        ('2', 'Lower secondary education'),
        ('3', 'Upper secondary education'),
        ('4', 'Post-secondary non-tertiary education'),
        ('5', 'Short-cycle tertiary education'),
        ('6', 'Bachelor’s or equivalent level'),
        ('7', 'Master’s or equivalent level'),
        ('8', 'Doctoral or equivalent level'),
        ('9', 'Not elsewhere classified'),
    )
    EducationLevel = models.CharField(max_length = 40,blank=True,choices=EDUCATIONLEVEL)
    CountryOfBirth = models.ForeignKey(Country,blank=True,null=True,on_delete=models.DO_NOTHING,help_text='Select the country you were born as in your passport')
    Nationality = models.CharField(max_length = 2,blank=True,help_text='Select the country of your passport')
    SecondNationality = models.CharField(max_length = 2,blank=True,help_text='Select the country of your passport')

    def save(self,*args,**kwargs):
        self.BusinessPartnerclass = 'IndividualPerson'
        return super(IndividualPerson,self).save(*args,**kwargs)

    class Meta:
        abstract =False

    def __str__(self):
        return f'{self.GivenName} - {self.LastName}'

class Organization(BusinessPartner):
    Name = models.CharField(max_length = 256,null=False,help_text='Name of the organization:')
    LegalForm = models.CharField(max_length = 50,null=False,choices=LEGALFORM,help_text='Enter legal form of the cy')
    DateOfIncorporation = models.DateField(null=True)
    CountryOfIncorporation = models.ForeignKey(Country,on_delete=models.DO_NOTHING,blank=True,null=True)
    Register = models.CharField(max_length = 100,null=True,help_text='Code/Name of the registry where the company is registered')
    PlaceOfRegister = models.CharField(max_length = 256,blank=True)
    RoleInClearing = models.CharField(max_length = 50,blank=True)

    class Meta:
        abstract =False
    def __str__(self):
        return f'{self.Name} - {self.LegalForm}'

    def save(self,*args,**kwargs):
        self.BusinessPartnerclass = 'Organization'
        return super(Organization,self).save(*args,**kwargs)