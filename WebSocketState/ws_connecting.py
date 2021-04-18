
from State import State
from .ws_state import WebSocketState


class WebSocketConnecting(WebSocketState):
    def run(self):
        return

    def next(self, action):
        return
