import requests

from api import Api
from app.models import Session, Post
from parameters import PAGE_ACCESS_TOKEN, APP_ID, PAGE_ID
from repos.news import NewsRepository


class Publishing():

    def publish(self):
        news = NewsRepository().get_unpublished()
        if len(news) > 3:
            raise Exception("Too many unpublished news")
        for a_news in news:
            self.publish_one(a_news)

    def publish_one(self, a_news):
        message = self._compose_message(a_news)
        r = self._compose_request(message)
        resp = requests.post(r)
        if resp.status_code == 200:
            print("Posted message: %s" % message)
            a_news.published = True
            Session().commit()
        else:
            print("Tried to post message: %s \nFailed with resp: %s" %
                  (message, resp.content))

    def _compose_message(self, a_news):
        post = Post(a_news)
        return '%s\n\n%s' % (post.content, post.link)

    def _compose_request(self, message):
        r = Api().page_id(PAGE_ID).feed({'to': PAGE_ID,
                                         'from': APP_ID,
                                         'message': message,
                                         'access_token': PAGE_ACCESS_TOKEN})
        return r.url
