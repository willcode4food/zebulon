
from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from .ws_connecting import WebSocketConnecting
from constants import actions_constants


class WebSocketStarting(WebSocketState):
    def __init__(self, url):
        self.api_url = url
        WebSocketState.__init__(self)

    def run(self):
        print("-- Web Socket Starting --")
        return

    def next(self, action):
        if len(self.transitions) == 0:
            self.transitions = {
                actions_constants.CONNECT: WebSocketConnecting(self.api_url)
            }
        return WebSocketState.next(self, action)
