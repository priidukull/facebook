from sqlalchemy import MetaData, Table

from schema import engine


meta = MetaData(schema='fb')
news = Table('news', meta, autoload=True, autoload_with=engine)