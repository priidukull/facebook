import re

from sqlalchemy import Column, UnicodeText, Boolean, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from schema import engine
from schema.fb import news


Base = declarative_base()
session_factory = sessionmaker(bind=engine, expire_on_commit=False)
Session = scoped_session(session_factory)


class News(Base):
    __table__ = news

    def all(self):
        return Session().query(News).order_by(News.id.desc()).all()


class Post(Base):
    __tablename__ = 'post'
    id = Column(BigInteger, primary_key=True)
    content = Column(UnicodeText, nullable=False)
    link = Column(UnicodeText, nullable=False)
    published = Column(Boolean, nullable=False)

    def __init__(self, a_news):
        self.id = a_news.id
        self.content = self._content(a_news)
        self.link = a_news.link
        self.published = a_news.published

    def _content(self, a_news):
        if re.match(r'^[0-9]-[0-9]-[0-9]-[0-9]+-[0-9]+', a_news.title):
            content = a_news.summary
        else:
            content = a_news.title
        return content.replace('&amp;', '&')