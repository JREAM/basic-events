"""
Local Settings
This file is to be renamed 'local.py', this file is in the .gitignore

(!) But since this is for example purposes I will keep it in git


For local/development change to:  from .development import *
For staging change to:            from .staging import *
For production change:            from .production import *
"""
from .development import *

# This obviously isn;t a secret for this demo app :)
SECRET_KEY =  'da key homie'

