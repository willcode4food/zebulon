
from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from .ws_keeping_alive import WebSocketKeepingAlive
from .ws_disconnecting import WebSocketDisconnecting
from constants import actions_constants
from datetime import datetime


class WebSocketListening(WebSocketState):
    def __init__(self):
        WebSocketState.__init__(self)

    def run(self):
        current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        print("-- Web Socket Listening --" + current_time)

        return

    def next(self, action):
        if len(self.transitions) == 0:
            self.transitions = {
                actions_constants.LISTEN:  WebSocketListening(),
                actions_constants.DISCONNECT: WebSocketDisconnecting()
            }
        return WebSocketState.next(self, action)
