import time

from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from constants import actions_constants


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
        if len(self.transitions) == 0:
            self.transitions = {
                actions_constants.MESSAGE:  WebSocketKeepingAlive()
            }
        return WebSocketState.next(self, action)
