from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from WebSocketStateMachine import WebSocketStateMachine


class WebSocketClosing(WebSocketState):
    def run(self):
        print("-- Web Socket Closing --")
        return

    def next(self, action):
        if action == WebSocketStateAction.disconnect:
            return WebSocketStateMachine.disconnecting
        return WebSocketStateMachine.closing
