import datetime

from app.models import News, Session


class NewsRepository(News):

    def save_news(self, news):
        session = Session()
        q = session.query(News)
        for n in news:
            published = n['published_parsed']
            date = datetime.date(published[0], published[1], published[2])
            link = n['link']
            title = n['title']
            existing_news = q.filter(News.link == link).all()
            if not existing_news:
                news = News(date=date, title=title, summary=n['summary'],
                            link=link)
                session.add(news)
        session.commit()

    def get_unpublished(self):
        q = Session().query(News)
        return q.filter(News.published.is_(False)).order_by(News.date).all()
