
from State import State
from .ws_state import WebSocketState

from WebSocketStateAction import WebSocketStateAction
from WebSocketStateMachine import WebSocketStateMachine


class WebSocketListening(WebSocketState):

    def run(self):
        print("-- Web Socket Listening --")
        # self.keep_alive = Thread(target=self._keep_alive)
        return

    def next(self, action):
        if action == WebSocketStateAction.disconnect:
            return WebSocketStateMachine.disconnecting
        return WebSocketStateMachine.listening
