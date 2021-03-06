import importlib
import os
import re
import socket


mode = os.environ.get('MODE')
if not mode and socket.gethostname() == 'ip-172-31-47-240':
    mode = 'live'
action_var = os.getenv('ACTION')


def _load_settings(m):
    module = importlib.import_module('settings.' + m)
    settings = {k: v for k, v in module.__dict__.items()
                if not re.match('^(_|@)', k)}
    globals().update(settings)

for m in ['default', mode]:
    _load_settings(m)
