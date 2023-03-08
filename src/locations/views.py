import json
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.views import generic
from django.contrib.auth.models import User

from param.models import ModelFieldMapper
from .forms import AddressForm
from .settings import APP_NAME
from .models import GeographicalUnit,Address
# from tools.script_tools import 

# from .forms import *
# from profiles.models import *
from tools.tools_global import ( exludeFields, getModel )


from param.tools import buildModelOutput, listForeignKeys

# Create your views here.


def index(request):
    message = APP_NAME
    return render (request, 'locations/index_simple.html', {'message':message})

def getApiParent(request,id):
    
    try:
        qs = GeographicalUnit.objects.filter(id=id)
        obj = qs[0]
        category = obj.GeographicalUnitCategory       
    except:
        message = f'id ({id}) of Geographic location not found'
        return JsonResponse(data={'Error':message},safe=False)      
    
    if category not in ['Country','City']:
        message = f'{category} id of Geographic location not in allowed values city or country'
        return JsonResponse(data={'Error':message},safe=False)      
    
    fatherId = obj.IsPartOf.id
    return JsonResponse(data={ 'id':fatherId },safe=False)
    
   

def viewLocation(request,what,place):
    def excludeIdFields(inDict):
        return exludeFields(inDict,['id','IsPartOf_id'])
        
    appName = APP_NAME
    locationHierarchy = ['City','Country','Continent']
    listOfCityKeys = ['id','GeographicalUnitName','GeographicalUnitShortName','CityCode','IsPartOf_id']
    listOfCountryKeys = ['id','GeographicalUnitName','GeographicalUnitShortName','CountryCode','ISO3CountryCode','InternetSuffix','ISO3166Country','IsPartOf_id']
    listOfContinentKeys =['id','GeographicalUnitName','GeographicalUnitShortName','ContinentCode']
    
    match what:
        case 'city':
            try:
                city =      buildModelOutput('locations','City',     listOfCityKeys,Q(CityCode__icontains=place))
                country =   buildModelOutput('locations','Country',  listOfCountryKeys,Q(pk=city[0]['IsPartOf_id']))
                continent = buildModelOutput('locations','Continent',listOfContinentKeys,Q(pk=country[0]['IsPartOf_id']))     
            except:
                message = f'{what} {place} not found or corresponding geografic location'
                return JsonResponse(data={'Error':message},safe=False)
                
        case 'country':
            try:
                country =   buildModelOutput('locations','Country',  listOfCountryKeys,Q(CountryCode__icontains=place))
                city =      buildModelOutput('locations','City',     listOfCityKeys,Q(IsPartOf_id=country[0]['id']))
                continent = buildModelOutput('locations','Continent',listOfContinentKeys,Q(pk=country[0]['IsPartOf_id']))     
            except:
                message = f'{what} {place} not found or corresponding geografic location'
                return JsonResponse(data={'Error':message},safe=False)
            
        case 'continent':
            try:
                continent = buildModelOutput('locations','Continent',listOfContinentKeys,Q(ContinentCode__icontains=place))     
                country =   buildModelOutput('locations','Country',  listOfCountryKeys,Q(IsPartOf_id=continent[0]['id']))
                city = []
                for indx,c in enumerate(country):
                    city += buildModelOutput('locations','City',   listOfCityKeys,Q(IsPartOf_id=country[indx]['id']))
            except:
                message = f'{what} {place} not found or corresponding geografic location'
                return JsonResponse(data={'Error':message},safe=False)
        case other:
            message= f'{what} seach type does not exist'
            return JsonResponse(data={'Error':message},safe=False)
    try:   
        collectContinent = []
        for cont in continent:
            continentCountries = [excludeIdFields(c) for c in country if cont['id'] == c['IsPartOf_id']]
            collectCountries = []
            for cntry in country:
                countryCities = [excludeIdFields(c) for c in city if cntry['id'] == c['IsPartOf_id']]
                collectCountries.append(excludeIdFields(cntry) | {'cities':countryCities})
            collectContinent.append(excludeIdFields(cont) | {'countries':collectCountries})
        collectContinentJson = json.dumps(collectContinent,indent = 2)
    except:
        message = f'Building up the tree on a {what} query '
        return JsonResponse(data={'Error':message},safe=False)
        
        
    
    return JsonResponse(data=collectContinent,safe=False)

def get_initialSet(user):
    return {"created_by":user,
            "updated_by":user}


def viewAddress(request):
    
    if request.method == "POST":
        addressForm = AddressForm(request.POST)
        if addressForm.is_valid():
            addressForm.save()
    else:
        addressForm = AddressForm(initial=get_initialSet(request.user))
        pass
    message = addressForm.errors
    templateName= f"{APP_NAME}/AddressCRUD.html"
    context = {
        "addressform": addressForm,
        "message": message,
    }
    
    return render(request,templateName,context)

def getValues(model,keyList):
    """Based on the keylist it returns the values of the items of the table.
       It will convert foreign keys based on choices of the modelfield mapper

    Args:
        model (class): a model (class)
        keyList (list of strings): List of fields

    Returns:
        _type_: List of values
    """    
    appName = '.'.join(model.__mro__[0].__module__.split('.')[0:-1])
    # model.__mro__[0].__module__.split('.')[0]
    modelName = model.__mro__[0].__name__
    listFKs = listForeignKeys(model,appName,modelName)
    object_list = model.objects.all()
    if len(object_list) == 0:
        return list(object_list)
    object_record_list = [rcrd.__dict__ for rcrd in object_list ]

    valueRecords = []
    for rcrd in object_record_list:
        valueList = []
        for key in keyList:
            if key in listFKs:
                keyId = f"{key}_id"
                if rcrd[keyId] == None:
                    valueList.append('')
                else:
                    qs = ModelFieldMapper.objects.filter(AppName=appName, ModelName=modelName, ModelFieldName=key)
                    if len(qs) > 0:
                        # valueList.append(rcrd) 
                        fkAppName = qs[0].AppForeignKeyName 
                        fkModelName = qs[0].ModelForeignKeyModel                        
                        fldName = qs[0].ModelForeignKeyField
                        fkModel=getModel(fkAppName, fkModelName)
                        fkObject = fkModel.objects.filter(**{'id': rcrd[keyId]})
                        value = eval(f"fkObject[0].{fldName}")
                        valueList.append(value)
            else:
                valueList.append(rcrd[key])
        valueRecords.append(valueList)
    return valueRecords
            
            
        
    # address_list_list_values = [[fld[k] for k in fld.keys() if k not in ['_state']]  for fld in address_list_list_aggregate]
    return list(object_list)          
               
class AddressList(generic.ListView):
    model = Address
    template_name = f"{APP_NAME}/AddressList.html"
    list_to_display = ['AddressId','AddressType','SequenceNumber'
        ,'Street','HouseNumber'
        ,'AdditionalAddressLine'
        ,'City'
        ,'Country'
        ,'Latitude','Longitude'   
        ,'updated','created'
        ,'created_by','updated_by'
        ,'id']
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # address_list_list_keys = [k for k in address_list_list_aggregate[0].keys() if k not in ['_state']]
        object_list = getValues(self.model,self.list_to_display)
        context['list_keys'] = self.list_to_display
        context['list_data'] = object_list
        context['theobject'] = "Address"
        return context
    
                 
    
   
        
        
            
            
