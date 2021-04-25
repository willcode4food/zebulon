from websocket import create_connection, WebSocketConnectionClosedException
from .client import Client


class SocketClient(Client):
    def __init__(self, api_key, api_secret, api_passphrase):
        self.api_url = None
        self.headers = None
        self.keep_alive_thread = None
        self.main_thread = None
        self.web_socket = None
        self.products = None
        self.channels = None
        self.parameters = {}

        return

    def __call__(self, products):
        self.products = products
        return

    def set_headers(self, message):
        return

    def start(self):
        return

    def stop(self):
        return
