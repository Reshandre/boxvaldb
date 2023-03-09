from django import forms

from django.apps import apps

from tools.tools_global import getAppList, getModelList
from .models import ModelFieldMapper
# from .tools import ( getModelList  )



class GetAppForm(forms.Form):
    appName = forms.ChoiceField(label='App name',choices = () )
    modelName = forms.ChoiceField(label='Model name',choices = ())


    def __init__(self,*args,**kwargs):
        # isPost = kwargs.pop("isPost",False)
        if len(kwargs):
            appName = kwargs.pop("appName",'')
            modelName = kwargs.pop("modelName",'')
        else:
            appName = args[0]["appName"]
            modelName = args[0]["modelName"]

        self.myCleanedData = {}
        self.myCleanedData["appName"]=appName
        self.myCleanedData["modelName"]=modelName

        super(GetAppForm,self).__init__(*args,**kwargs)

        if len(appName) > 0 and len(modelName) > 0:
            self.fields['appName'].initial = appName
            self.fields['modelName'].initial = modelName
        elif len(appName) == 0 and len(modelName) == 0:
            appName = 'locations'
            modelName = 'City'
        elif len(appName) == 0 and len(modelName) > 0:
            appName = modelName.split('-')[0]
            self.fields['appName'].initial = appName
            self.fields['modelName'].initial = modelName
        elif len(appName) > 0 and len(modelName) == 0:
            self.fields['appName'].initial = appName

        self.fields['appName'].choices      =   getAppList() 
        self.fields['modelName'].choices    = getModelList(appName)

    # def clean(self):
    #         self.cleaned_data = super().clean()
    #         return self.myCleanedData

    # class meta:
    #     exclude = ('appName', 'modelName')

def contains(k,list):
    for l in list:
        if l in k:
            return True
    
# 
def dictToList(matchpattern,inDict):
    listfields = []
    nrFields = 6
    switch = 0
    r = []
    for k, itm in inDict.items():
        if not contains(k,matchpattern):
            continue
        if switch == 0:            
            count = int(k.split('_')[1])
            r.append(count)
        r.append(itm)
        switch += 1
        if switch == nrFields:
            r.append(itm)
            listfields.append(r)
            r = []
            switch = 0                
    return listfields
        

class ModelFieldMapperForm(forms.Form):
    appName = forms.CharField(label='App name')
    modelName = forms.CharField(label='Model name')

    def __init__(self,*args,**kwargs):
        if len(kwargs):
            self.listfields = kwargs.pop("listfields",'')
            self.appName = kwargs.pop("appName",'')
            self.modelName = kwargs.pop("modelName",'')
        else:
            # listfields = args[0]["listfields"]
            self.appName = args[0]["appName"]
            self.modelName = args[0]["modelName"]
            self.listfields = dictToList(['ModelFieldName_','ModelMappedName_','AppForeignKeyName_','ModelForeignKeyModel_','ModelForeignKeyField_','ModelDoNotExport_'],args[0])
            

        super(ModelFieldMapperForm,self).__init__(*args,**kwargs)

        self.fields['appName'].initial = self.appName
        self.fields['modelName'].initial = self.modelName
        # ModelDoNotExport
        for f in self.listfields:
            self.fields[f'ModelFieldName_{f[0]}'] = forms.CharField(label=f'field ')
            self.fields[f'ModelMappedName_{f[0]}'] = forms.CharField(label=f'Map To ',required=False)
            self.fields[f'AppForeignKeyName_{f[0]}'] = forms.CharField(label=f'Model To ',required=False)
            self.fields[f'ModelForeignKeyModel_{f[0]}'] = forms.CharField(label=f'Model To ',required=False)
            self.fields[f'ModelForeignKeyField_{f[0]}'] = forms.CharField(label=f'Model Field To ',required=False)
            self.fields[f'ModelDoNotExport_{f[0]}'] = forms.CharField(label=f'Model Field To ',required=False)
            
        for f in self.listfields:
            self.fields[f'ModelFieldName_{f[0]}'].initial = f[1]
            self.fields[f'ModelMappedName_{f[0]}'].initial = f[2]
            self.fields[f'AppForeignKeyName_{f[0]}'].initial = f[3]
            self.fields[f'ModelForeignKeyModel_{f[0]}'].initial = f[4]
            self.fields[f'ModelForeignKeyField_{f[0]}'].initial = f[5]
            self.fields[f'ModelDoNotExport_{f[0]}'].initial = f[6]

        pass    



    def save(self):
        pass
        for f in self.listfields:
            qs = ModelFieldMapper.objects.filter(AppName=self.appName,ModelName=self.modelName,ModelFieldName=f[1])
            qsExists = qs.count() == 1
            current_mapped = f[2]
            current_fkapp = f[3]
            current_fkmodel = f[4]
            current_fkmodelfield = f[5]
            current_modeldonotexport = f[6]
            currentIsEmpty =  not (current_mapped != '' or not (current_fkapp == '' and current_fkmodel == '') or current_fkmodelfield != ''
             or current_modeldonotexport != '')
            if qsExists:
                db_mapped  = qs[0].ModelMappedName
                db_fkmodel = '' if qs[0].ModelForeignKeyModel is None else qs[0].ModelForeignKeyModel
                db_fkapp = '' if qs[0].AppForeignKeyName is None else qs[0].AppForeignKeyName                
                db_fkmodelfield = '' if qs[0].ModelForeignKeyField is None else qs[0].ModelForeignKeyField
                db_modeldonotexport = '' if qs[0].ModelForeignKeyField else 'X'

                mapIsEqual = db_mapped == current_mapped and current_fkapp == db_fkapp and current_fkmodel == db_fkmodel and current_fkmodelfield == db_fkmodelfield and current_modeldonotexport==db_modeldonotexport
            else:
                db_mapped = ''
                mapIsEqual = False               
            if not mapIsEqual:
                if not currentIsEmpty:
                    if not qsExists:
                        MFM = ModelFieldMapper(AppName=self.appName,ModelName=self.modelName,
                        ModelFieldName=f[1],ModelMappedName=f[2],AppForeignKeyName=f[3],ModelForeignKeyModel=f[4],ModelForeignKeyField=f[5],ModelDoNotExport=(f[6]=='X'))
                        MFM.save()
                    elif qsExists:
                        # qs[0].ModelMappedName=f[2]
                        # qs[0].save()
                        qs.update(ModelMappedName=f[2],AppForeignKeyName=f[3],ModelForeignKeyModel=f[4],ModelForeignKeyField=f[5],ModelDoNotExport=(f[6]=='X'))
                elif currentIsEmpty:
                    qs.delete()
            elif mapIsEqual:
                toDelete = qsExists and currentIsEmpty
                if toDelete:
                    qs.delete()
    pass

            
                   

