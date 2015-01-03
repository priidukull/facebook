import os

from parameters import HOST

from app import app


os.environ['ACTION'] = 'bo'
app.run(host=HOST, debug=True)
