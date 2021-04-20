
from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from WebSocketStateMachine import WebSocketStateMachine


class WebSocketConnecting(WebSocketState):
    def run(self):
        print("-- Web Socket connecting -- ")
        return

    def next(self, action):
        if action == WebSocketStateAction.listen:
            return WebSocketStateMachine.listening
        return WebSocketStateMachine.connecting
