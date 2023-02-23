from django.urls import path
from .views import (index, 

)


# SET THE NAMESPACE!
app_name = 'masters'
urlpatterns = [
    path('', index, name='index'),
  #  path ('customizing/importexport/',ImportExportModel,name='import_export_model')
]