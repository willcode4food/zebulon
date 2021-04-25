from StateMachine import StateMachine
from constants import actions_constants
from WebSocketState import WebSocketStarting
from WebSocketState import WebSocketConnecting
from WebSocketState import WebSocketDisconnecting
from WebSocketState import WebSocketListening


class WebSocketStateMachine(StateMachine):
    def __init__(self, initialState, url, params):
        stateToInitialize = None

        if initialState == actions_constants.START:
            stateToInitialize = WebSocketStarting(url, params)
        if initialState == actions_constants.CONNECT:
            stateToInitialize = WebSocketConnecting(url, params)
        if initialState == actions_constants.LISTEN:
            stateToInitialize = WebSocketListening()
        if initialState == actions_constants.DISCONNECT:
            stateToInitialize = WebSocketDisconnecting()

        if stateToInitialize:
            StateMachine.__init__(self, stateToInitialize)
        return

    def runAll(self, inputs):
        StateMachine.runAll(self, inputs)
        if self.currentState.message:
            return self.currentState.message
        return
