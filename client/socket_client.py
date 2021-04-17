from websocket import create_connection, WebSocketConnectionClosedException
from .Client import Client
from constants import client_constants


class SocketClient(Client):
    def __init__(self, api_key, api_secret, api_passphrase):
        self.api_url = client_constants.API_URL_SOCKET
        self.socket = create_connection(self.api_url)
        return

    def __call__(self, action, products):
        return

    def set_headers(self):
        return

    def _get_channels(self):
        return
