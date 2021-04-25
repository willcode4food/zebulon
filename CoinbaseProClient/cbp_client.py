import requests
import hmac
import hashlib
import base64
import time


from Client import Client


class CBPClient(Client):
    def __init__(self, api_key, api_secret, api_passphrase):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase

    def set_headers(self, message):
        timestamp = str(time.time())
        self.headers = {
            'Content-Type': 'Application/JSON',
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.api_passphrase,
            'User-Agent': 'Mosaic/1.0'
        }
        if(message):
            self._sign_message(''.join([timestamp, message]))

    def _sign_message(self, message):
        message = message.encode('ascii')
        hmac_key = base64.b64decode(self.api_secret)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')
        self.headers['CB-ACCESS-SIGN'] = signature_b64
