

from importlib import import_module




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

