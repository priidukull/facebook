import os

from app import app


os.environ['ACTION'] = 'bo'
app.run(debug=True)
