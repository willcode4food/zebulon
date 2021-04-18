from State import State
from .ws_state import WebSocketState


class WebSocketDisconnecting(WebSocketState):
    def run(self):
        return

    def next(self, action):
        return
