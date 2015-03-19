from time import sleep

import feedparser
import requests

from calls.master import Publishing
from parameters import SECONDS_IN_MINUTE, FEED_URL
from repos.news import NewsRepository


def _remove(news):
    for n in news:
        f = requests.get(n['link']).text
        if '<b>kohtuasjaga seotud dokumente ei leitud</b>' in f:
            news.remove(n)
            print('Not collecting news with URL=%s' % n['link'])
    return news

def _collect():
    feed = feedparser.parse(FEED_URL)
    news = feed['entries']
    news = _remove(news)
    print('Collecting news')
    NewsRepository().save_news(news)

def _publish():
    news = NewsRepository().get_unpublished()
    for a_news in news:
        Publishing().publish_one(a_news)


if __name__ == '__main__':
    while True:
        _collect()
        _publish()
        minutes = 15
        print('Will sleep for %d minutes' % minutes)
        sleep(minutes * SECONDS_IN_MINUTE)