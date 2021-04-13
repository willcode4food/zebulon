import requests

from .cbp_client import CBPClient


class RestClient(CBPClient):
    def __init__(self, api_key, api_secret, api_passphrase):
        self.session = requests.Session()
        self.response = None
        self.headers = None

    def __call__(self, method, url, body):
        self.method = method
        self.url = url
        self.body = body
        self.request = requests.Request(
            method, url, self.headers, body).prepare()
        self.response = self.session.send(self.request)
        return self.response

    def set_headers(self, headers):
        self.session.headers.update(headers)
