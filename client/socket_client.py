from websocket import create_connection, WebSocketConnectionClosedException
from .client import Client
from constants import client_constants


class SocketClient(Client):
    def __init__(self, api_key, api_secret, api_passphrase):
        self.api_url = client_constants.API_URL_SOCKET
        self.headers = None
        self.keep_alive_thread = None
        self.main_thread = None
        self.web_socket = None
        self.products = None
        self.channels = None
        self.sub_params = None

        return

    def __call__(self, products):
        self.products = products
        return

    def set_headers(self, message):
        return

    def _get_channels(self):
        return
