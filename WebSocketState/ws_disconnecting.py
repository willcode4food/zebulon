from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from WebSocketStateMachine import WebSocketStateMachine


class WebSocketDisconnecting(WebSocketState):
    def run(self):
        print("-- Web Socket Disconnecting -- ")
        return

    def next(self, action):
        if action == WebSocketStateAction.start:
            return WebSocketStateMachine.starting

        return WebSocketStateMachine.disconnecting
