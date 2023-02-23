
from importlib import import_module


def alternateKeys(model):
    cConstraints = model._meta.constraints   
    if (len(cConstraints) > 0):
        cConstraints = model._meta.constraints[0]
        constraints = list(cConstraints.__dict__['fields'])
    else:
        constraints = []
    if len(model._meta.unique_together) > 0:
        uniqueTogether = model._meta.unique_together[0]
    else:
        uniqueTogether = []
    result = []
    if not ((len(constraints) == 0) and (len(uniqueTogether) == 0)):
        if len(constraints) != 0:
            result = constraints
        else:          
            result = uniqueTogether
    return result

def foreignKeys(model):
    result = []
    for f in model._meta.fields:
        if f.__class__.__name__ == 'ForeignKey':
            result.append([f.related_model,f.attname,alternateKeys(f.related_model)])   
    return result


def getKeys(model):
    result=[]
    uniqueList=[]
    primaryKeyList=[]
    for f in model._meta.fields:
        if f.name == 'id':
            pk = model.__name__.lower()+'_'+f.name
            primaryKeyList.append(pk)    
            continue   
        if f.unique:
            uniqueList.append(f.name)
        if f.primary_key:
            primaryKeyList.append(f.name)    

    cConstraints = model._meta.constraints   
    if (len(cConstraints) > 0):
        cConstraints = model._meta.constraints[0]
        constraints = list(cConstraints.__dict__['fields'])
    else:
        constraints = []
    if len(model._meta.unique_together) > 0:
        uniqueTogether = model._meta.unique_together[0]
    else:
        uniqueTogether = []
    if ((len(constraints) == 0) and (len(uniqueTogether) == 0)):
        result += uniqueList
        result += primaryKeyList
    else:
        result += constraints
        result += uniqueTogether
    result1=set()
    result1.update(result)
    result2=list(result1)
    return result2

def allkeys(model):
    fld=[]
    for f in model._meta.fields:
        if f.__class__.__name__ == 'ForeignKey':
            ks = getKeys(f.related_model)
            fld += ks 
        else:
            fld.append(f.name)
    fields = set(fld)
    fld = list(fields)
    return fld
def fetchFields(model):
    result = {}
    for f in model._meta.fields:
        item = {}    
        subitem = {}
        subitem['type'] = type(f).__name__
        item[f.__dict__['name']] =  subitem
        result.update(item)
    result1={}
    for f in model._meta.fields:
        if f.__class__.__name__ == 'ForeignKey':           
            result2 = fetchFields(f.related_model) 
            toKeep = alternateKeys(f.related_model)
            result3 = result2.copy()
            for ff in result2:
                if ff in toKeep:
                    pass
                else:
                    result3.pop(ff)
            result1 = result1 | result3
            pass
    return result | result1



def depthModel(model):
    depth = 0
    for f in model._meta.fields:
        if f.__class__.__name__ == 'ForeignKey':
            depth = max(depth,depthModel(f.related_model))
    return depth+1

def listALLmodels(app_name):
    module = import_module(f"{app_name}.models")
    result = []
    for o in dir(module):
        if (getattr(module,o).__class__.__name__ == 'ModelBase'):
            result.append(getattr(module,o))
    return result

def depthSortedModels(app_name):
    modelList = listALLmodels(app_name)
    modelLevels=[]
    for model in modelList:
        item = (depthModel(model),model.__name__,model)
        modelLevels.append(item)
    modelLevels = sorted(modelLevels)
    return [x[2] for x in modelLevels]



def detectDelimitter(line):
    possible_delimitters = (",",";")
    delim = ""
    for c in possible_delimitters:
        wrds= line.split(c)
        if len(wrds) > 1:
            return c
            
def cleanupWords(wrds):
    def chars(*args):
        return [chr(i) for a in args for i in range(ord(a[0]), ord(a[1])+1)]
    # base64chars = list(chars('AZ', 'az', '09', '++', '//','__','--','  ',"««","»»"))
    base64chars = list(chars('AZ', 'az', '09', '++', '//','__','--','  '))
    result=[]
    for w in wrds:
        if w is not None:
            ww =[*w]
            www = ww.copy()
            for c in ww:
                if c not in base64chars:
                    www.remove(c)
            wwww = "".join(www)
            result.append(wwww)

    return result


def convertValue(val,givenClass):
    match givenClass: 
        case "DateField":
            if (val == None or val == ""):
                return None
            sVal = str(val) if  type(val).__name__ == 'int' else val  
            if len(sVal) == 4:
                sVal += '-1-1'
            return sVal
        case "IntegerField":
            return int(val)
        case _:
            return val

def fetchParameters(*args):
    components = args[0].split(",")
    params = {}
    for c in components:
        par=c.split("=")
        d = {}
        d[par[0]]=par[1]
        params.update(d)
    return params

