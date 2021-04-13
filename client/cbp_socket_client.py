from client.cbp_client import CBPClient


class CBPSocketClient(CBPClient):

    def __init__(api_key, api_secret, api_passphrase):
        self.api_url = 'wss://ws-feed.pro.coinbase.com'
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase
        self.channels = [{"name": "ticker", "product_ids": [
            product_id for product_id in self.products]}]

    def _connect():

    def _disconnect():

    def get_product_trades():
