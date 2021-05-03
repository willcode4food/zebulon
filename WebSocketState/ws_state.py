from State import State
from .WebSocketStateAction import WebSocketStateAction
import sys


class WebSocketState(State):
    def __init__(self):
        self.transitions = {}
        self.keep_alive = None
        self.main_thread = None
        self.web_socket = None
        self.action = None
        self.message = None

    def run(self):
        return

    def next(self, action):
        self.action = WebSocketStateAction(action)
        if self.transitions[action]:
            return self.transitions[action]
        else:
            raise "Action not supported for current state"
