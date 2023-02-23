from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.utils.translation import gettext as _

# Create your models here.
# The model is used to map imported data
class ModelFieldMapper(models.Model):
    AppName = models.CharField(max_length=100,help_text=_('Name of the application which fields are to be mapped or FK established'))
    ModelName = models.CharField(max_length=100,help_text=_('Name of the model which fields are to be mapped'))
    ModelFieldName = models.CharField(max_length=100,help_text=_('Name of the model field to which the field needs to be mapped'),null=True)
    ModelMappedName = models.CharField(max_length=100,help_text=_('Name of the mapped Model Field which needs to be mapped back to the field name'),null=True)
    AppForeignKeyName = models.CharField(max_length=100,help_text=_('Name of the model field to which the field needs to be mapped'),null=True)    
    ModelForeignKeyModel = models.CharField(max_length=100,help_text=_('Name of the foreign model to use'),null=True)
    ModelForeignKeyField = models.CharField(max_length=100,help_text=_('Name of the Field of the foreign model to use'),null=True)
    ModelDoNotExport = models.BooleanField(default=False)
    class Meta:
        constraints =  [
         UniqueConstraint(fields=['AppName','ModelName', 'ModelFieldName'], name='unique_Field'),
        ]
