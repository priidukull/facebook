import feedparser
from news_repository import NewsRepository
from parameters import FEED_URL


def collect():
    feed = feedparser.parse(FEED_URL)
    news = feed['entries']
    print("Collecting news")
    NewsRepository().save_news(news)

