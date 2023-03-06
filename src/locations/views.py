import json
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from locations.forms import AddressForm
from locations.settings import APP_NAME

# from tools.script_tools import 

# from .forms import *
# from profiles.models import *
from tools.tools_global import ( exludeFields )


from param.tools import buildModelOutput

# Create your views here.


def index(request):
    message = "Locations"
    return render (request, 'locations/index_simple.html', {'message':message})


def viewLocation(request,what,place):
    def excludeIdFields(inDict):
        return exludeFields(inDict,['id','IsPartOf_id'])
        
    appName='locations'
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
    templateName= f"{APP_NAME}/getAddress.html"
    context = {
        "addressform": addressForm,
        "message": message,
    }
    
    return render(request,templateName,context)
            
                
                
    
   
        
        
            
            
