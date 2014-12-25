import importlib
import os
import re


def load_settings(env):
    module = importlib.import_module('settings.' + env)
    settings = {k: v for k, v in module.__dict__.items()
                if not re.match('^(_|@)', k)}
    globals().update(settings)

env_var = os.environ.get('MODE')
if env_var:
    env = env_var.lower()
else:
    env = 'dev'

load_settings(env)
