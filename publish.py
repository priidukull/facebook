import re
import urllib.parse
import requests
from models import Session
from news_repository import NewsRepository
from parameters import PAGE_ACCESS_TOKEN, APP_ID, PAGE_ID


class Publishing():

    def publish(self):
        news = NewsRepository().get_unpublished()
        for a_news in news:
            self.publish_one(a_news)

    def publish_one(self, a_news):
        message = self._compose_message(a_news)
        resp = requests.post('https://graph.facebook.com/v2.2/%s/feed?to=%s&from=%s&message=%s&access_token=%s' % (PAGE_ID, PAGE_ID, APP_ID, message, PAGE_ACCESS_TOKEN))
        if resp.status_code == 200:
            print("Posted message: %s" % message)
            a_news.published = True
            Session().commit()
        else:
            print("Tried to post message: %s \nFailed with resp: %s" % (message, resp.content))

    def test(self, message):
        message = message.replace('amp;', '')
        message = urllib.parse.quote(message)
        r = 'https://graph.facebook.com/v2.2/762468393802810/feed?message=%s&access_token=1522386624678645|IaRAAKIm1XGjsZhOn4Df7uN4GXk' % message
        resp = requests.post(r)

    def _compose_message(self, a_news):
        if re.match(r'^[0-9]-[0-9]-[0-9]-[0-9]+-[0-9]+', a_news.title):
            content = a_news.summary
        else:
            content = a_news.title
        message = '%s\n\n%s' % (content, a_news.link)
        message = message.replace('&amp;', '&')
        message = urllib.parse.quote(message)
        return message


if __name__ == '__main__':
    Publishing().test('Osaühing Tomex Tööd kassatsioon Tallinna Ringkonnakohtu 28.05.2014. a otsusele Osaühing Tomex Tööd hagis IF P&amp;C Insurance AS vastu kindlustushüvitise 48749.40 euro ja viivise 6327.25 euro saamiseks.')