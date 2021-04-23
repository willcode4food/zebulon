
from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from .ws_listening import WebSocketListening
from .ws_disconnecting import WebSocketDisconnecting
from constants import actions_constants
from websocket import create_connection


class WebSocketConnecting(WebSocketState):

    def __init__(self, url):
        self.api_url = url
        WebSocketState.__init__(self)

    def run(self):
        WebSocketState.web_socket = create_connection(self.api_url)
        print("-- Web Socket Connected -- ")
        return

    def next(self, action):
        if len(self.transitions) == 0:
            self.transitions = {
                actions_constants.LISTEN:  WebSocketListening(),
                actions_constants.DISCONNECT: WebSocketDisconnecting()
            }
        return WebSocketState.next(self, action)
