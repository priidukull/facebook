import pytest

from models import News, Post, Session
from tests.fixtures import session


@pytest.mark.usefixtures(session.__name__)
class Test:

    def test_news_all(self):
        news = News().all()

        assert len(news) > 50

    def test_post_init(self):
        a_news_202 = Session().query(News).filter_by(id=202).one()
        post = Post(a_news_202)

        assert 'Osaühing Tomex Tööd kassatsioon Tallinna Ringkonnakohtu 28.05.2014. a otsusele Osaühing Tomex Tööd hagis IF P&C Insurance AS vastu kindlustushüvitise 48749.40 euro ja viivise 6327.25 euro saamiseks.' == post.content
        assert 'http://www.riigikohus.ee/?id=11&tekst=RK/3-2-1-136-14&date=23.12.2014' == post.link