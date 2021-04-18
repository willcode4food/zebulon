
from State import State
from threading import Thread


class WebSocketState(State):
    def run(self):
        self.transitions = {}
        return

    def next(self, action):
        if action in self.transitions:
            return self.transitions[action]
        return
