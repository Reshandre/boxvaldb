from django.conf import settings

PROJECT_NAME = settings.PROJECT_NAME

DATA_LOAD_DUMP_DIR = settings.BASE_DIR / 'dataloaddump'
DATA_LOAD_DUMP_IMPORT_SUFFIX = ''
DATA_LOAD_DUMP_EXPORT_SUFFIX = '_exp'
DATA_LOAD_DUMP_EXTENTION = '.xlsx'
DATA_LOAD_DUMP_BACKUP = 'archive'
