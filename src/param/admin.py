from django.contrib import admin
from .models import ModelFieldMapper

# Register your models here.


@admin.register(ModelFieldMapper)
class ModelFieldMapperAdmin(admin.ModelAdmin):
    list_display= ('AppName','ModelName','ModelFieldName','ModelMappedName','AppForeignKeyName','ModelForeignKeyModel', 'ModelForeignKeyField','pk')