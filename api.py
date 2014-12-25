import urllib.parse


class Api():
    def __init__(self):
        self.url = 'https://graph.facebook.com/v2.2'

    def page_id(self, page_id):
        self.url = '%s/%s' % (self.url, page_id)
        return self

    def feed(self, kwargs):
        self.url = '%s/feed?%s' % (self.url, urllib.parse.urlencode(kwargs))
        return self