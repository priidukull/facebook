import os

from parameters import HOST, PORT
from app import app


os.environ['ACTION'] = 'bo'
app.run(host=HOST, port=PORT, debug=True)
