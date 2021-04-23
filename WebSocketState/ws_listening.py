
from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from .ws_keeping_alive import WebSocketKeepingAlive
from constants import actions_constants


class WebSocketListening(WebSocketState):
    def __init__(self):
        WebSocketState.__init__(self)

    def run(self):
        print("-- Web Socket Listening --")

        return

    def next(self, action):
        if len(self.transitions) == 0:
            self.transitions = {
                actions_constants.MESSAGE:  WebSocketKeepingAlive
            }
        return WebSocketState.next(self, action)
