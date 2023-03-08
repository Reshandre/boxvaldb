
from django.apps import apps

from tools.tools_global import getModel
from .models import ModelFieldMapper


from django.conf import settings as gsettings
from .settings import (
    DATA_LOAD_DUMP_DIR,
    DATA_LOAD_DUMP_EXPORT_SUFFIX,
    DATA_LOAD_DUMP_EXTENTION, 
    DATA_LOAD_DUMP_IMPORT_SUFFIX, )
from importlib import import_module

from param.models import ModelFieldMapper
from openpyxl.styles import Font
from openpyxl.styles import PatternFill
from openpyxl.styles.colors import Color
from openpyxl.styles.fills import Fill
from openpyxl.styles.fills import DEFAULT_GRAY_FILL,FILL_SOLID

from openpyxl import load_workbook, Workbook

"""Functions in support of the param app

 
 """


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




def mapColumns(columns, appName, modelName):
    """Columns of the excel sheet are transformed into the names of the model

    Args:
        columns (list of strings): Columns of the excel sheet
        appName (string): app name
        modelName (string): model name 

    Returns:
        list of string: list of model characteristics
    """
    mappedColumns = []
    for c in columns:
        modelFieldName = c
        qs = ModelFieldMapper.objects.filter(
            AppName=appName, ModelName=modelName, ModelMappedName=c)
        qsFound = len(qs) == 1
        if qsFound:
            modelFieldName = qs[0].ModelFieldName
        mappedColumns.append(modelFieldName)
    return mappedColumns


def composeColumns(wb, columns, modelName):
    """Sets the header in the first row

    Args:
        wb (WorkBook): WorkBook excel
        columns (_type_): _description_
        modelName (_type_): _description_
    """
    ws = wb[modelName]
    ft=Font(bold=True)
    ws.append(columns)
    # ft = Font(bold=True)
    for cell in ws[1:1]:
        cell.font = ft


def mapRawColumns(rawColumns, appName, modelName):
    """Replace name of importable fields of the model to the heading of the excel sheet

    Args:
        rawColumns (list of string): list of columns of the model
        appName (string): app name
        modelName (string): model name

    Returns:
        list of string: list of fields who become the list of the excel sheet first row
    """
    mappedColumns = []
    noExportList = getNoExportList(appName,modelName)
    for cr in rawColumns:
        modelMappedName = cr # in case not a mapped field
        if cr in noExportList:
            continue
        qs = ModelFieldMapper.objects.filter(
            AppName=appName, ModelName=modelName, ModelFieldName=cr)
        qsFound = len(qs) == 1
        if qsFound and len(qs[0].ModelMappedName) >0:
            modelMappedName = qs[0].ModelMappedName
        mappedColumns.append(modelMappedName)
    return mappedColumns


# 


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


def openWorkBook(fileName):
    wb = load_workbook(filename=fileName)
    return wb





def loadData(wb, mappedColumns, appName, modelName):
    modelObject = getModel(appName, modelName)
    lstForeignKeys = listForeignKeys(modelObject, appName, modelName)
    sheet = wb[modelName]
    constraints = uniqueFieldConstraintslist(modelObject, appName, modelName)
    for count, r in enumerate(sheet.rows):
        if count == 0:
            continue
        rowData = {}
        for indx, c in enumerate(mappedColumns):
            if r[indx].value == None:
                rowData[c] = None
            else:
                rowData[c] = r[indx].value
                if c in lstForeignKeys:
                    rowData[c] = getForeignKeyValue(
                        appName, modelName, c, rowData[c])
        # constraintsCache = constraints
        # aConstraintList = constraints[0]
        constraintKeys = {}
        constraintCollected=False
        for cns in constraints:
            if constraintCollected:
                break
            for cnsi in cns:
                if constraintCollected:
                    break
                constraintKeys = {}
                for cnsfld in cnsi:                    
                    if cnsfld in rowData.keys():
                        constraintKeys[cnsfld] = rowData[cnsfld]
                        if len(constraintKeys) == len(cnsi):
                            constraintCollected=True
                            break
                    else:
                        break
        # kwargs = {k: v for k, v in rowData.items() if k in aConstraintList}
        deltaDicUpdate = {}
        deltaDicUpdate['defaults'] = {
            k: v for k, v in rowData.items() if k not in constraintKeys}
        deltaDicCreate={k: v for k, v in rowData.items() if k not in constraintKeys}
        kwargsUpdate = constraintKeys | deltaDicUpdate
        kwargsCreate = constraintKeys | deltaDicCreate
        
        # module = import_module(f"{appName}.models")
        qs = modelObject.objects.filter(**constraintKeys)
        if (len(qs) > 0):
            kwargsCreate["id"] = qs[0].id
            o = modelObject(**kwargsCreate)
            o.save()
            pass
        else:
            modelObject.objects.create(**kwargsCreate)
            pass
        
        
        # obj, created = modelObject.objects.update_or_create(**kwargs)
        pass

def getNoExportList(appName,modelName):
        qs_noExportList = ModelFieldMapper.objects.filter(AppName=appName,ModelName=modelName,ModelDoNotExport = True)
        noExportList = [n.ModelFieldName for n in qs_noExportList]
        return noExportList

def fetchForeignKeyCode (id,fieldName,appName, modelName):
    qs = ModelFieldMapper.objects.filter(AppName=appName,ModelName=modelName,ModelFieldName = fieldName)
    if len(qs) == 0:
        resultValue = id
    else:
        fkAppForeignKeyName = qs[0].AppForeignKeyName
        fkModelForeignKeyModel = qs[0].ModelForeignKeyModel
        fkModelForeignKeyField =qs[0].ModelForeignKeyField
        fkModelObject = getModel(fkAppForeignKeyName, fkModelForeignKeyModel)
        if id is not None:
            fkQs = fkModelObject.objects.get(id=id)
            resultValue = eval(f"fkQs.{fkModelForeignKeyField}")
        else:
            resultValue = ''
    return resultValue
    
    
     
    
    
def buildWorkBook(wb, columns,rawColumns, appName, modelName):
    modelObject = getModel(appName, modelName)
    lstForeignKeys = listForeignKeys(modelObject,appName,modelName)
    ws = wb[modelName]
    constraints = uniqueFieldConstraintslist(modelObject, appName, modelName)
    qs = modelObject.objects.all()
    noExportList = getNoExportList(appName,modelName)
    for rownum,r in enumerate(qs):
        row = []
        for f in r.__dict__:
            fieldName = f
            if 'id' != f and'id' in f and f.split('_')[1]=='id':
                fieldName = f.split('_')[0]       
            if fieldName in  noExportList:
                continue
            if fieldName not in rawColumns:
                continue
            if fieldName not in  lstForeignKeys:
                row.append(r.__dict__[f])
            else:
                row.append(fetchForeignKeyCode(r.__dict__[f],fieldName,appName, modelName))
        ws.cell(row=rownum+1,column=1)
        ws.append(row)
        
       
                

            

def readColumns(wb, modelName):
    sheet = wb[modelName]
    columns = sheet[1]
    return [c.value for c in columns]


# def composeColumns(wb, columns):
#     pass


def getLoadData(appName):
    return gsettings.DATA_LOAD_DUMP_DIR / appName


def getLoadDataImportPath(appName, modelName):
    fileName = modelName + DATA_LOAD_DUMP_IMPORT_SUFFIX + \
        DATA_LOAD_DUMP_EXTENTION
    return DATA_LOAD_DUMP_DIR / appName / fileName


def getLoadDataExportPath(appName, modelName):
    fileName = modelName + DATA_LOAD_DUMP_EXPORT_SUFFIX + \
        DATA_LOAD_DUMP_EXTENTION
    return DATA_LOAD_DUMP_DIR / appName / fileName


def uniqueFieldConstraintslist(modelObject, appName, modelName):
    """Get fields or combination of fields that filters a model to a unique instance """
    uniqueFieldConstraintlst = []
    for fld in modelObject._meta.local_concrete_fields:
        if fld.unique:
            if '_' in fld.name:
                if fld.name.split('_')[1] == 'ptr':
                    continue
            cnstr = [fld.name]
            uniqueFieldConstraintlst.append(cnstr)
    
    for ol in modelObject.__mro__:
        if '__module__' not in ol.__dict__.keys():
            continue
        if ol.__dict__['__module__'].split('.')[0]==appName:
            for oc in ol._meta.constraints:
                cnstr = [oc.fields]
                uniqueFieldConstraintlst.append(cnstr)

    return uniqueFieldConstraintlst

def translateDict(aDict,appName, modelName):
    qs = ModelFieldMapper.objects.filter(
            AppName=appName, ModelName=modelName).values_list('AppName','ModelName','ModelFieldName','ModelMappedName')
    mapper = {e[2]:e[3] for e in qs if e[3]!= ""}
    mapperKeys = mapper.keys()
    returnDict = {}
    for k,d in aDict.items():
        if k in mapperKeys:
            newKey = mapper[k]
        else:
            newKey = k
        returnDict[newKey] = d
        
    return returnDict


def buildModelOutput(appName,modelName,fieldList,filter):
    """Returns a dictionary with a record of the model filtered with 'filter'

    Args:
        appName (string): project app name
        modelName (string): model name of the app
        fieldList (list): selection of fields to be extracted from teh record
        filter (Q object): Filters the record from the model

    Returns:
        Dictionary: LIst of fields
    """
    theModel = getModel(appName,modelName)
    qsEntries = theModel.objects.filter(filter)
    entriesDictTemp = qsEntries.values()
    entriesDictRenamedCols=[]
    for o in entriesDictTemp:    
        entriesDict = {k:o[k] for k in o.keys() if k in fieldList}
        entriesDictRenamedCols.append(translateDict(entriesDict,appName, modelName))    
    return entriesDictRenamedCols
