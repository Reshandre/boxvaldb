

from importlib import import_module
from django.conf import settings as gsettings
from django.apps import apps

from param.models import ModelFieldMapper





def getModel(appName, modelName):
    """Returns the model class based on its app and name

    Args:
        appName (string): Name of the app
        modelName (string): Name of the model

    Raises:
        class of model not ound

    Returns:
        model.Model: class of model.Model
    """
    if '-' in modelName:
        modelName = modelName.split('-')[1]
    module = import_module(f"{appName}.models")
    result = None
    found = False
    for o in dir(module):
        if (getattr(module, o).__class__.__name__ in ('ModelBase')):
            if getattr(module, o).__name__ == modelName:
                result = getattr(module, o)
                found = True
                break
    if not found:
        raise Exception(f"Model  {appName} {modelName} not found  ")
    return result



def exludeFields(inDict, exclusionFields):
    return {k:inDict[k] for k in inDict.keys() if k not in  exclusionFields  }

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

def getAppList():
    """Get the list of apps for selection

    Returns:
        list of tupple: choice list (app,app)
    """
    return [(app, app) for app in gsettings.INSTALLED_APPS if not app.startswith("django")]


def getModelList(appName):
    """Get the list of models for selection (modeName,modelName)

    Args:
        appName (string): _description_

    Returns:
        list of tupple: _description_
    """
    return [(m.__name__, m.__name__) for m in apps.get_models() if m.__module__.split('.')[0] == appName]


def getSimpleModelList(appName):
    return [m.__name__ for m in apps.get_models() if m.__module__.split('.')[0] == appName]

#


def listALLmodels(app_name):
    """Returns the list of all models of an application (app)

    Args:
        app_name (string): Name of the app

    Returns:
        list: list of string with the name of modesl
    """
    module = import_module(f"{app_name}.models")
    result = []
    for o in dir(module):
        if (getattr(module, o).__class__.__name__ == 'ModelBase'):
            result.append(getattr(module, o))
    return result

# returns the model based on its name





def getRawColumns(modelObject):

    listField = getFields(modelObject)
    rawColumns = []
    for f in listField:
        if '_' in f[1]:
            if f[1].split('_')[1] == 'ptr':
                continue
        rawColumns.append(f[1])
    return rawColumns


#
def getFields(modelObject):
    """relevant fields of a model (entered as the objecft itself)
       [count,f.name,f.__class__.__name__,f.attname,f.max_length,rel[0],rel[1],'']

    Args:
        modelObject (models.Model): _description_

    Returns:
        list of list: list of lists of field properties
    """
    result = []
    count = 0
    for i, f in enumerate(modelObject._meta.concrete_fields):
        if (f.primary_key and 'pk' == f.name) or 'id' == f.name:
            continue
        rel = ('', '')
        if hasattr(f, 'remote_field'):
            rField = f.remote_field
            if (rField != None):
                rel = (type(rField).__name__, '........' if len(
                    rField.name) == 0 else rField.name)
        else:
            rel = ('', '')
        result.append([count, f.name, f.__class__.__name__, f.attname, f.max_length, rel[0],
                      rel[1], 'Unique' if f.unique else '', 'X' if f.null or f.blank or f.unique else ''])
        count += 1
    return result

def getForeignKeyValue(appName, modelName, column, value):
    """Get the instnce based of a foreign key value of a column  

    Args:
        appName (string): app name
        modelName (string): model name
        column (string): column name
        value (Any): foreign key as given by ModelFieldMapper

    Raises:
        Exception: _description_

    Returns:
        instance of model: instance of model
    """    
    qs = ModelFieldMapper.objects.filter(
        AppName=appName, ModelName=modelName, ModelFieldName=column)
    isFound = len(qs) == 1
    if not isFound:
        raise Exception(    f"No entry found for chosen foreign key {column} search")
    fkmodel = qs[0].ModelForeignKeyModel
    fkApp = qs[0].AppForeignKeyName
    fkModelObject = getModel(fkApp, fkmodel)
    fkField = qs[0].ModelForeignKeyField
    qsFK = fkModelObject.objects.filter(**{fkField: value})
    qsFKObject = qsFK[0]
    return qsFKObject

    # return the list the foreign key of a model


def listForeignKeys(modelObject,appName,modelName):
    """Returns the list of foreign keys of the object

    Args:
        modelObject (class of model): class of a model
        appName (string): app name
        modelName (string): model name


    Returns:
        list of strings: list of foreign keys columns
    """    
    lstForeignKeys = []
    for f in modelObject._meta.fields:
        if 'ptr' in f.name:
            if f.name.split('_')[1] == 'ptr':
                continue
        if f.is_relation:
            qs = ModelFieldMapper.objects.filter(AppName=appName,ModelName=modelName,ModelFieldName=f.name)
            if len(qs)!=0:
                if not qs[0].ModelDoNotExport:
                    lstForeignKeys.append(f.name)
            else:
                lstForeignKeys.append(f.name)
                
    return lstForeignKeys


