import importlib
import os
import re


action_var = os.getenv('ACTION')

def _load_settings():
    module = importlib.import_module('settings.default')
    settings = {k: v for k, v in module.__dict__.items()
                if not re.match('^(_|@)', k)}
    globals().update(settings)
    module = importlib.import_module('settings.' + os.environ.get('MODE'))
    settings = {k: v for k, v in module.__dict__.items()
                if not re.match('^(_|@)', k)}
    globals().update(settings)

_load_settings()
