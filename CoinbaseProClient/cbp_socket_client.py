from .cbp_client import CBPClient
from Client import SocketClient


class CBPSocketClient(SocketClient, CBPClient):

    def __init__(self, api_key, api_secret, api_passphrase):
        self.api_url = 'wss://ws-feed.pro.coinbase.com'
        CBPClient.__init__(self, api_key, api_secret, api_passphrase)

    def __call__(self, products):
        self.products = products
        if not isinstance(self.products, list):
            print("Errorproducts is not a list")
            return
        self.channels = [{"name": "ticker", "product_ids": [
            product_id for product_id in self.products]}]
        self.sub_params = {'type': 'subscribe',
                           'product_ids': self.products, 'channels': self.channels}
        message = 'GET' + '/users/self/verify'
        self.set_headers(message)

    def set_headers(self, message):
        CBPClient.set_headers(self, message)
