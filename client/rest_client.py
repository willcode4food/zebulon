import requests

from .client import Client


class RestClient(Client):
    def __init__(self):
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
