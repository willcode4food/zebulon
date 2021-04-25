from .cbp_client import CBPClient
from Client import SocketClient
from WebSocketStateMachine import WebSocketStateMachine
from constants import actions_constants
from constants import client_constants
import time
from threading import Thread, current_thread
import sys


class CBPSocketClient(SocketClient, CBPClient):

    def __init__(self, api_key, api_secret, api_passphrase):
        CBPClient.__init__(self, api_key, api_secret, api_passphrase)
        SocketClient.__init__(self, api_key, api_secret, api_passphrase)
        self.message = None
        self.state_machine = None
        self.api_url = client_constants.API_URL_SOCKET
        self.main_thread = Thread(
            target=self.start, args=(0,))

    def __call__(self, products):
        self.products = products
        if not isinstance(self.products, list):
            print("Errorproducts is not a list")
            return
        self.channels = [{"name": "ticker", "product_ids": [
            product_id for product_id in self.products]}]
        self.parameters = {'type': 'subscribe',
                           'product_ids': self.products, 'channels': self.channels}
        message = 'GET' + '/users/self/verify'
        self.set_headers(message)
        try:
            self.main_thread.start()
            while self.main_thread.is_alive():
                self.main_thread.join(0.5)
        except KeyboardInterrupt as e:
            self.stop(e)

    def set_headers(self, message):
        CBPClient.set_headers(self, message)

    def set_paramaters(self):
        self.parameters['signature'] = self.headers['CB-ACCESS-SIGN']
        self.parameters['key'] = self.headers['CB-ACCESS-KEY']
        self.parameters['passphrase'] = self.headers['CB-ACCESS-PASSPHRASE']
        self.parameters['timestamp'] = self.headers['CB-ACCESS-TIMESTAMP']

    def start(self, thread_id):
        print("--- Client Starting ---")
        current_running_thread = current_thread()
        self.state_machine = WebSocketStateMachine(
            actions_constants.START, self.api_url, self.parameters)
        self.state_machine.runAll(
            [actions_constants.CONNECT])

        while True:
            if not current_running_thread.is_alive:
                break
            self.message = self.state_machine.runAll(
                [actions_constants.LISTEN])
            print(self.message)
            time.sleep(1)

    def stop(self, exception):
        print("--- Client Stopping ---")
        if self.state_machine:
            self.state_machine.runAll([actions_constants.DISCONNECT])
        self.main_thread.alive = False
        self.main_thread.join()
