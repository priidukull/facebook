import importlib
import os
import re


mode = os.environ["FB_MODE"]
action_var = os.getenv("ACTION")

def _load_settings(mode):
    module = importlib.import_module('settings.' + mode)
    settings = {k: v for k, v in module.__dict__.items()
                if not re.match('^(_|@)', k)}
    globals().update(settings)

for e in ['default', mode]:
    _load_settings(e)
