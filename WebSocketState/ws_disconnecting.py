from State import State
from .ws_state import WebSocketState
from WebSocketStateAction import WebSocketStateAction
from websocket import WebSocketConnectionClosedException


class WebSocketDisconnecting(WebSocketState):
    def __init__(self):
        return

    def run(self):
        try:
            if WebSocketState.web_socket:
                self.web_socket.close()
                print("-- Web Socket Disconnected -- ")
        except WebSocketConnectionClosedException:
            pass
        finally:
            return

    def next(self, action):
        return WebSocketState.next(self, action)
