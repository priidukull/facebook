import requests
from parameters import APP_ID, APP_SECRET, PERSONAL_ACCESS_TOKEN, \
    PAGE_ACCESS_TOKEN, TEST_APP_ID, TEST_APP_SECRET


class AccessToken:
    def personal(self):
        request = 'https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=http://www.legal.ee/facebook&scope=publish_actions,manage_pages,publish_stream' % APP_ID
        return requests.post(request)

    def personal_test(self):
        request = 'https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=http://www.legal.ee/facebook&scope=publish_actions,manage_pages,publish_stream' % TEST_APP_ID
        return requests.post(request)

    def get_access_token(self):
        request = 'https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials' % (TEST_APP_ID, TEST_APP_SECRET)
        return requests.post(request)

    def page(self):
        request = 'https://graph.facebook.com/me/accounts?access_token=%s' % PERSONAL_ACCESS_TOKEN
        return requests.post(request)

    def long(self):
        request = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % \
                  (APP_ID, APP_SECRET, PAGE_ACCESS_TOKEN)
        return requests.post(request)


if __name__ == '__main__':
    resp = AccessToken().get_access_token()
    pass
