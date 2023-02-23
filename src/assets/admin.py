from django.contrib import admin
from django.contrib.admin.options import TabularInline

from .models import *
# Register your models here.

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    fields= ['AssetId','CompletionState','OwnerOfAsset','AssetDescription']
    list_display = ['AssetId','CompletionState','OwnerOfAsset','AssetDescription']

@admin.register(RealEstateProperty)
class RealEstatePropertyAdmin(admin.ModelAdmin):
    fields = ['AssetId','CompletionState','OwnerOfAsset','AssetDescription','RealEstateType','UsageType','LocationOfPhysicalAsset']
    list_display = ['AssetId','CompletionState','OwnerOfAsset','AssetDescription','RealEstateType','UsageType','LocationOfPhysicalAsset']
