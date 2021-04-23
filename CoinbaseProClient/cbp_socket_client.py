from .cbp_client import CBPClient
from Client import SocketClient
from WebSocketStateMachine import WebSocketStateMachine
from constants import actions_constants
from constants import client_constants


class CBPSocketClient(SocketClient, CBPClient):

    def __init__(self, api_key, api_secret, api_passphrase):
        CBPClient.__init__(self, api_key, api_secret, api_passphrase)
        SocketClient.__init__(self, api_key, api_secret, api_passphrase)
        self.state_machine = None
        self.api_url = client_constants.API_URL_SOCKET

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
        self.start()

    def set_headers(self, message):
        CBPClient.set_headers(self, message)

    def set_paramaters(self):
        self.parameters['signature'] = self.headers['CB-ACCESS-SIGN']
        self.parameters['key'] = self.headers['CB-ACCESS-KEY']
        self.parameters['passphrase'] = self.headers['CB-ACCESS-PASSPHRASE']
        self.parameters['timestamp'] = self.headers['CB-ACCESS-TIMESTAMP']

    def start(self):
        self.state_machine = WebSocketStateMachine(
            actions_constants.START, self.api_url, self.parameters)
        self.state_machine.runAll(
            [actions_constants.CONNECT, actions_constants.DISCONNECT])

        return

    def stop(self):
        if self.state_machine:
            self.state_machine.runAll([actions_constants.DISCONNECT])
        return
