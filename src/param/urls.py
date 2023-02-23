from django.urls import path
from .views import (index, 
ImportExportModel
)


# SET THE NAMESPACE!
app_name = 'param'
urlpatterns = [
    path('', index, name='index'),
    path ('managemodels/',ImportExportModel,name='manage_models')
]