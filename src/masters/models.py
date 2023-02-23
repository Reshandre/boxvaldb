from django.db import models
from partners.models import BusinessPartner

# Create your models here.

class StandardizedVolume(models.Model):
    OwnerOfStandardization = models.ForeignKey(BusinessPartner,on_delete=models.SET_NULL,null=True)
    SourceOfStandardization = models.CharField(max_length=20,help_text='Qualifies the nature of the realEstate', default='Standard')
    STD_VOLUMEC_TYPE = (
        ('Small','Small'),
        ('Normal','Normal'),
        ('Big','Big'),
        ('VeryBig','Very big')
    )
    StdVolumeCategory = models.CharField(max_length=20,help_text='Qualifies the nature of the realEstate', default='Normal',choices=STD_VOLUMEC_TYPE)
    ObjectName = models.CharField(max_length=20,help_text='Qualifies the nature of the realEstate', default='Normal',choices=STD_VOLUMEC_TYPE)
    ObjectLength = models.DecimalField(max_digits=8,decimal_places=2,help_text='The length of the object')
    ObjectWidth = models.DecimalField(max_digits=8,decimal_places=2,help_text='The width of the object')
    ObjectHeight = models.DecimalField(max_digits=8,decimal_places=2,help_text='The width of the object')
    class meta:
        contraints = [
            models.UniqueConstraint('SourceOfStandardization', 'StdVolumeCategory','ObjectName', name='standard_key_combination')
        ]