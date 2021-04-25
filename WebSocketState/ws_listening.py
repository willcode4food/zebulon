
from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from .ws_disconnecting import WebSocketDisconnecting
from constants import actions_constants
from datetime import datetime
import json


class WebSocketListening(WebSocketState):
    def __init__(self):
        WebSocketState.__init__(self)

    def run(self):

        data = WebSocketState.web_socket.recv()
        msg = json.loads(data)
        print(msg)

    def next(self, action):
        if len(self.transitions) == 0:
            self.transitions = {
                actions_constants.LISTEN:  WebSocketListening(),
                actions_constants.DISCONNECT: WebSocketDisconnecting()
            }
        return WebSocketState.next(self, action)
