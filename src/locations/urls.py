from django.urls import path
from .views import (viewLocation, index, viewAddress

)


# SET THE NAMESPACE!
app_name = 'locations'
urlpatterns = [
    path('', index, name='index'),
    path ('api/searchplace/<what>/<place>',viewLocation,name='api-place'),
    path ('managedata/address', viewAddress,name='manage-adddress')
]