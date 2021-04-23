
from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction

# from .ws_keeping_alive import WebSocketKeepingAlive


class WebSocketMessaging(WebSocketState):
    def __init__(self):
        WebSocketState.__init__(self)

    def run(self):
        print("-- Web Socket Messaging --")
        return

    def next(self, action):
        # if action == WebSocketStateAction.listen:
        #     return WebSocketStateMachine.listening
        # return WebSocketStateMachine.message
        return
