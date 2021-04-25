import requests
import hmac
import hashlib
import base64
import time

from .cbp_client import CBPClient
from Client import RestClient
from constants import client_constants


class CBPRestClient(RestClient, CBPClient):

    def __init__(self, api_key, api_secret, api_passphrase):
        CBPClient.__init__(self, api_key, api_secret, api_passphrase)
        RestClient.__init__(self)
        self.api_url = client_constants.API_URL_REST
        self.endpoints = {'product_trades_btc': '/products/BTC-USD/trades'}

    def __call__(self, method, endpoint, body):
        endpoint_url = self.api_url + self.endpoints[endpoint]
        self.set_headers(''.join([method, endpoint_url, (body or '')]))
        return RestClient.__call__(self, method, endpoint_url, body)

    def set_headers(self, message):
        CBPClient.set_headers(self, message)
        RestClient.set_headers(self, self.headers)
