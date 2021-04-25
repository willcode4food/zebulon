
from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from .ws_connecting import WebSocketConnecting
from .ws_disconnecting import WebSocketDisconnecting
from constants import actions_constants


class WebSocketStarting(WebSocketState):
    def __init__(self, url, params):
        self.api_url = url
        self.parameters = params
        WebSocketState.__init__(self)

    def run(self):
        print("-- Web Socket Starting --")
        return

    def next(self, action):
        if len(self.transitions) == 0:
            self.transitions = {
                actions_constants.CONNECT: WebSocketConnecting(
                    self.api_url, self.parameters),
                actions_constants.DISCONNECT: WebSocketDisconnecting()
            }
        return WebSocketState.next(self, action)
