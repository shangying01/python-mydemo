import json
class HttpRequestBean(object):
    def __init__(self):
        self._cookies = None
        self._responseString=None
        self._responseJson = None

    def get_cookies(self):
        return self._cookies

    def set_cookies(self, cookies):
            self._cookies = cookies

    def get_responseString(self):
        return self._responseString

    def set_responseString(self, responseString):
            self._responseString = str(responseString)

    def get_responseJson(self):
        return self._responseJson

    def set_responseJson(self, responseJson):
            self._responseJson = responseJson