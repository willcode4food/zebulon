import time

from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from WebSocketStateMachine import WebSocketStateMachine


class WebSocketKeepingAlive(WebSocketState):
    def __init__(self):
        WebSocketState.__init__(self)

    def run(self, interval=30):

        while self.web_socket.connected:
            print("-- Web Socket Keeping Alive")
            self.web_socket.ping("keepalive")
            time.sleep(interval)
        return

    def next(self, action):
        if action == WebSocketStateAction.disconnect:
            return WebSocketStateMachine.disconnecting
        return
