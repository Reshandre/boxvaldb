from django.urls import path
from .views import (AddressList, getApiParent, viewLocation, index, AddressCreate,AddressUpdate
)


# SET THE NAMESPACE!
app_name = 'locations'
urlpatterns = [
    path('', index, name='index'),
    path ('api/searchplace/<what>/<place>',viewLocation,name='api-place'),
    path ('api/parentid/<int:id>',getApiParent,name='api-getparent'),
    path ('address/create', AddressCreate,name='address-create'),
    path ('address/<int:id>/update', AddressUpdate,name='address-update'),
    path ('listdata/address',AddressList.as_view(),name='list-address'),
]