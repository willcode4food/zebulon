from State import State
from .ws_state import WebSocketState
from .WebSocketStateAction import WebSocketStateAction
from websocket import WebSocketConnectionClosedException
from constants import actions_constants
import sys


class WebSocketDisconnecting(WebSocketState):
    def __init__(self):
        WebSocketState.__init__(self)

    def run(self):
        try:
            if WebSocketState.web_socket:
                WebSocketState.web_socket.close()
                print("-- Web Socket Disconnected -- ")
        except WebSocketConnectionClosedException as e:
            raise e
        finally:
            return

    def next(self, action):
        print("-- Client Shutting Down -- ")
        sys.exit()
