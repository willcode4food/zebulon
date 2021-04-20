from State import State


class WebSocketState(State):
    def __init__(self):
        self.transitions = {}
        self.keep_alive = None
        self.main_thread = None
        self.web_socket = None

    def run(self):
        return

    def next(self, action):
        if action in self.transitions:
            return self.transitions[action]
        return
