from django.shortcuts import render

from tools.tools_global import getFields, getModel, getSimpleModelList
from .forms import GetAppForm, ModelFieldMapperForm
from .models import ModelFieldMapper
from .XLSXinputoutput import runExport, runImport, runBackup


def index(request):
    message = "Version initiale"
    return render (request, 'masters/index_simple.html', {'message':message})

def ImportExportModel(request):
    context_delta = {}
    varApp = 'locations'
    varModel = 'Continent'
    submitList,submitDisplayTable,submitImportExport ='submit','none','none'
    message="Initial"
    if request.method == "POST":
        message="After Post"
        getAppForm = GetAppForm(request.POST)
        if len(dict(request.POST)['modelName'][0])>0 and len(dict(request.POST)['appName'][0])>0:
            varApp = dict(request.POST)['appName'][0]
            varModel = dict(request.POST)['modelName'][0]
            if varModel not in getSimpleModelList(varApp):
                varModel = getSimpleModelList(varApp)[0]
                getAppForm = GetAppForm(appName = varApp,modelName=varModel)
            else:
                submitList,submitDisplayTable ='submit','submit'
            # print(f"app and model is {varApp} {varModel}")
            if 'displayTable'  in request.POST:
                # varModel = varModel.split('-')[1]
                theModel = getModel(varApp,varModel)
                occurrenceCount = theModel.objects.count()
                fieldList = getFields(theModel) # the fieldslist:[[seq,fldname,class(type),length...],[same],...]
                fieldListInput = [] #fieldlist seq,fldname,
                for f in fieldList:
                    recordExists = ModelFieldMapper.objects.filter(AppName = varApp,ModelName = varModel,ModelFieldName=f[1]).exists()
                    modelMappedName,appForeignKeyName,modelForeignKeyModel,modelForeignKeyField,ModelDoNotExport = '','','','',''
                    if recordExists:
                        fldmap = ModelFieldMapper.objects.filter(AppName = varApp,ModelName = varModel,ModelFieldName=f[1])
                        modelMappedName = fldmap[0].ModelMappedName
                        appForeignKeyName = '' if fldmap[0].AppForeignKeyName == None else fldmap[0].AppForeignKeyName
                        modelForeignKeyModel = '' if fldmap[0].ModelForeignKeyModel == None else fldmap[0].ModelForeignKeyModel
                        modelForeignKeyField ='' if fldmap[0].ModelForeignKeyField == None else fldmap[0].ModelForeignKeyField
                        ModelDoNotExport = '' if not fldmap[0].ModelDoNotExport else 'X'
                    fieldListInput.append([f[0],f[1],modelMappedName,appForeignKeyName,modelForeignKeyModel,modelForeignKeyField,ModelDoNotExport])
                modelFieldMapperForm = ModelFieldMapperForm(appName = varApp,modelName=varModel,listfields=fieldListInput)
                context_delta["fieldlist"] = fieldList
                context_delta["mapper"] = modelFieldMapperForm
                context_delta["occurrencecount"] = occurrenceCount
            elif 'Mapper' in request.POST:
                modelFieldMapperForm = ModelFieldMapperForm(request.POST)      
                if modelFieldMapperForm.is_valid():
                    modelFieldMapperForm.save()
                theModel = getModel(varApp,varModel)
                # the fieldslist:[[seq,fldname,class(type),length...],[same],...]  
                fieldList = getFields(theModel)    
                submitList,submitDisplayTable,submitImportExport ='none','none','submit'
                context_delta["fieldlist"] = fieldList
                context_delta["mapper"] = modelFieldMapperForm
            elif 'Import'  in request.POST:
                pass
                runImport(varApp,varModel)
            elif 'Export' in request.POST:
                runExport(varApp,varModel)
                pass
            elif 'Backup' in request.POST:
                runBackup(varApp,varModel)

            
        else:
            pass
    else:        
        getAppForm = GetAppForm(appName = varApp,modelName=varModel)
        

    context = {
        "appform":getAppForm,
        "submitlist":submitList,
        "submitDisplayTable":submitDisplayTable,
        "submitImportExport":submitImportExport,
        
        "message":message,
    }
    context = context | context_delta
    return render(request, 'param/importExport_simple.html', context=context)

 

