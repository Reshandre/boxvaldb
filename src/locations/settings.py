from django.conf import settings
from pathlib import Path
import os

PROJECT_NAME = settings.PROJECT_NAME
APP_NAME = os.path.basename(os.path.dirname(__file__))


