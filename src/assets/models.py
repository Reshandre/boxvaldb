from django.db import models

# Create your models here.
from partners.models import BusinessPartner
from locations.models import Address


class Asset(models.Model):
    AssetId = models.CharField(unique=True,max_length=20,help_text='Identifies the asset:')
    COMPLETION_STATES=(
    ('ReadyForUse','Ready for use'),
    ('ReadyForOperation','Ready for Operation'),
    ('ReadyForRent','Ready for Rent'),
    ('ReadyForSale','Ready for Sale'),   
    ('InConstruction','In Construction'),   
    ('Removed','Removed, not used anymore'),
    ('In maintenance','In Maintenance'),
    ('UnknownState','Unknown State'),      
)
    CompletionState = models.CharField(max_length=20,help_text='What the Real estate is ready for', default='ReadyForOperation',choices=COMPLETION_STATES)
    OwnerOfAsset = models.ForeignKey('partners.BusinessPartner'
    ,on_delete=models.SET_NULL,null=True)
    AssetDescription = models.TextField(max_length=256,help_text='Describes the asset:')

class RealEstateProperty(Asset):
    REAL_ESTATE_TYPES = (
    ('Residential','Residential'),
    ('Commercial','Commercial'),
    ('Industrial','Industrial'),
    ('RawLand','Raw Land'),
    ('SpecialUse','Special Use'),
    )
    RealEstateType = models.CharField(max_length=20,help_text='Gross Qualification of the realEstate', default='commercial',choices=REAL_ESTATE_TYPES)
    USAGE_TYPES = (
        ('SubRentalCluster','Sub Rental Cluster'),
        ('SecialUse','Special Use'),
    )
    UsageType = models.CharField(max_length=20,help_text='Qualifies the nature of the realEstate', default='SubRentalCluster',choices=USAGE_TYPES)
    LocationOfPhysicalAsset = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True)

class Box(Asset):
    BelongsTo = models.ForeignKey(RealEstateProperty,on_delete=models.CASCADE)
    BoxUnit   = models.CharField(max_length=20,help_text='Place of multiple boxes located together')
    BoxSubUnit = models.CharField(max_length=20,help_text='Identifies the box uniquely')
    BoxIntendedVolume = models.DecimalField(max_digits=8,decimal_places=2,help_text='The overall Volume of the box')
    BoxWidth =  models.DecimalField(max_digits=6,decimal_places=3,help_text='The width of the Box',default=0)
    BoxHeight =  models.DecimalField(max_digits=6,decimal_places=3,help_text='The height of the Box',default=0)
    BoxDepth =  models.DecimalField(max_digits=6,decimal_places=3,help_text='The depth of the Box')
    @property
    def BoxCalculatedArea(self):
        return self.BoxWidth * self.BoxDepth
    @property
    def BoxCalculatedVolume(self):
        return self.CalculatedArea * self.BoxHeight
    @property
    def BoxDescription(self):
        return super.AssetDescription
