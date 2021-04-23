from StateMachine import StateMachine
from constants import actions_constants
from WebSocketState import WebSocketStarting
from WebSocketState import WebSocketConnecting
from WebSocketState import WebSocketDisconnecting
from WebSocketState import WebSocketKeepingAlive
from WebSocketState import WebSocketListening
from WebSocketState import WebSocketMessaging


class WebSocketStateMachine(StateMachine):
    def __init__(self, initialState, url):
        stateToInitialize = None

        if initialState == actions_constants.START:
            stateToInitialize = WebSocketStarting(url)
        if initialState == actions_constants.CONNECT:
            stateToInitialize = WebSocketConnecting(url)
        if initialState == actions_constants.LISTEN:
            stateToInitialize = WebSocketListening()
        if initialState == actions_constants.KEEP_ALIVE:
            stateToInitialize = WebSocketKeepingAlive()
        if initialState == actions_constants.MESSAGE:
            stateToInitialize = WebSocketMessaging()
        if initialState == actions_constants.DISCONNECT:
            stateToInitialize = WebSocketDisconnecting()

        if stateToInitialize:
            StateMachine.__init__(self, stateToInitialize)
        return

    def runAll(self, inputs):
        StateMachine.runAll(self, inputs)
        return
