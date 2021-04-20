
from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from WebSocketStateMachine import WebSocketStateMachine
# from .ws_keeping_alive import WebSocketKeepingAlive


class WebSocketMessaging(WebSocketState):

    def run(self):
        print("-- Web Socket Starting --")
        return

    def next(self, action):
        if action == WebSocketStateAction.listen:
            return WebSocketStateMachine.listening
        return WebSocketStateMachine.message