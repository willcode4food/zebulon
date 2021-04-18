from .cbp_client import CBPClient
from Client import SocketClient


class CBPSocketClient(SocketClient, CBPClient):

    def __init__(self, api_key, api_secret, api_passphrase):
        self.api_url = 'wss://ws-feed.pro.coinbase.com'
        CBPClient.__init__(self, api_key, api_secret, api_passphrase)
        # self.channels = [{"name": "ticker", "product_ids": [
        #     product_id for product_id in self.products]}]
