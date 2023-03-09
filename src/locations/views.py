import json
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from param.models import ModelFieldMapper
from .forms import AddressForm
from .settings import APP_NAME
from .models import GeographicalUnit,Address
# from tools.script_tools import 

# from .forms import *
# from profiles.models import *
from tools.tools_global import ( exludeFields, getModel, getValues )


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
                city =      buildModelOutput(APP_NAME,'City',     listOfCityKeys,Q(CityCode__icontains=place))
                country =   buildModelOutput(APP_NAME,'Country',  listOfCountryKeys,Q(pk=city[0]['IsPartOf_id']))
                continent = buildModelOutput(APP_NAME,'Continent',listOfContinentKeys,Q(pk=country[0]['IsPartOf_id']))     
            except:
                message = f'{what} {place} not found or corresponding geografic location'
                return JsonResponse(data={'Error':message},safe=False)
                
        case 'country':
            try:
                country =   buildModelOutput(APP_NAME,'Country',  listOfCountryKeys,Q(CountryCode__icontains=place))
                city =      buildModelOutput(APP_NAME,'City',     listOfCityKeys,Q(IsPartOf_id=country[0]['id']))
                continent = buildModelOutput(APP_NAME,'Continent',listOfContinentKeys,Q(pk=country[0]['IsPartOf_id']))     
            except:
                message = f'{what} {place} not found or corresponding geografic location'
                return JsonResponse(data={'Error':message},safe=False)
            
        case 'continent':
            try:
                continent = buildModelOutput(APP_NAME,'Continent',listOfContinentKeys,Q(ContinentCode__icontains=place))     
                country =   buildModelOutput(APP_NAME,'Country',  listOfCountryKeys,Q(IsPartOf_id=continent[0]['id']))
                city = []
                for indx,c in enumerate(country):
                    city += buildModelOutput(APP_NAME,'City',   listOfCityKeys,Q(IsPartOf_id=country[indx]['id']))
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


def AddressUpdate(request,id):
    model = Address
    instance = get_object_or_404(model, id=id)
    if request.method == "POST":
        addressForm = AddressForm(request.POST,instance=instance)
        if addressForm.is_valid():
            addressForm.save()
    else:
        addressForm = AddressForm(instance=instance)
        pass
    message = addressForm.errors
    templateName= f"{APP_NAME}/AddressCRUD.html"
    context = {
        "addressform": addressForm,
        "message": message,
    }
    
    return render(request,templateName,context)

def AddressCreate(request):
    model=Address
    modelName = model.__name__
    if request.method == "POST":
        addressForm = AddressForm(request.POST)
        if addressForm.is_valid():
            addressForm.save()
    else:
        addressForm = AddressForm(initial= {"created_by":request.user,
                                            "updated_by":request.user})
    message = addressForm.errors
    templateName= f"{APP_NAME}/{modelName}CRUD.html"
    context = {
        "addressform": addressForm,
        "message": message,
    }
    
    return render(request,templateName,context)


            
            
        
    # address_list_list_values = [[fld[k] for k in fld.keys() if k not in ['_state']]  for fld in address_list_list_aggregate]
    return list(object_list)          
               
class AddressList(generic.ListView):
    model = Address
    template_name = f"{APP_NAME}/AddressList.html"
    list_to_display = ['AddressId','AddressType'
        # ,'SequenceNumber'
        ,'Street','HouseNumber'
        # ,'AdditionalAddressLine'
        ,'City'
        ,'Country'
        # ,'Latitude','Longitude'   
        ,'updated','created'
        ,'created_by','updated_by'
        ,'id']
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = getValues(self.model,self.list_to_display)
        context['list_keys'] = self.list_to_display
        context['list_data'] = object_list
        context['theobject'] = "Address"
        return context
    
                 
    
   
        
        
            
            
