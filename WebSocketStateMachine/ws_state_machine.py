from StateMachine import StateMachine
from WebSocketState import WebSocketStarting
from WebSocketState import WebSocketConnecting
from WebSocketState import WebSocketDisconnecting
from WebSocketState import WebSocketKeepingAlive
from WebSocketState import WebSocketListening
from WebSocketState import WebSocketMessaging


class WebSocketStateMachine(StateMachine):
    def __init(self):
        StateMachine.__init__(self, WebSocketStateMachine.starting)
        return


WebSocketStateMachine.starting = WebSocketStarting()
WebSocketStateMachine.connecting = WebSocketConnecting()
WebSocketStateMachine.disconnecting = WebSocketDisconnecting()
WebSocketStateMachine.keeping_alive = WebSocketKeepingAlive()
WebSocketStateMachine.listening = WebSocketStarting()
WebSocketStateMachine.message = WebSocketMessaging()
