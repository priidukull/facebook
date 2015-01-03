from time import sleep

import feedparser

from calls.master import Publishing
from collect import collect
from parameters import SECONDS_IN_MINUTE, FEED_URL
from repos.news import NewsRepository


def collect():
    feed = feedparser.parse(FEED_URL)
    news = feed['entries']
    print("Collecting news")
    NewsRepository().save_news(news)

def publish():
    news = NewsRepository().get_unpublished()
    if len(news) > 3:
        raise Exception("Too many unpublished news")
    for a_news in news:
        Publishing().publish_one(a_news)

while True:
    collect()
    publish()
    minutes = 15
    print("Will sleep for %d minutes" % minutes)
    sleep(minutes * SECONDS_IN_MINUTE)