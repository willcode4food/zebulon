import json
from State import State
from .ws_state import WebSocketState
from .WebSocketStateAction import WebSocketStateAction
from .ws_listening import WebSocketListening
from .ws_disconnecting import WebSocketDisconnecting
from constants import actions_constants
from websocket import create_connection


class WebSocketConnecting(WebSocketState):

    def __init__(self, url, params):
        self.api_url = url
        self.parameters = params
        WebSocketState.__init__(self)

    def run(self):
        print("-- Web Socket Connecting -- ")
        WebSocketState.web_socket = create_connection(self.api_url)
        WebSocketState.web_socket.send(json.dumps(self.parameters))
        print("-- Web Socket Connected -- ")
        return

    def next(self, action):
        if len(self.transitions) == 0:
            self.transitions = {
                actions_constants.LISTEN:  WebSocketListening()
            }
        return WebSocketState.next(self, action)
