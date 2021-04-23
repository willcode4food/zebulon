from StateAction import StateAction
from constants import actions_constants


class WebSocketStateAction(StateAction):
    def __init__(self, action):
        self.action = action

    def __str__(self): return self.action

    def __eq__(self, other):
        return self.action == other

    # Necessary when __eq__ is defined
    # in order to make this class usable as a
    # dictionary key:

    def __hash__(self):
        return hash(self.action)


WebSocketStateAction.connect = WebSocketStateAction(actions_constants.CONNECT)
WebSocketStateAction.disconnect = WebSocketStateAction(
    actions_constants.DISCONNECT)
WebSocketStateAction.keep_alive = WebSocketStateAction(
    actions_constants.KEEP_ALIVE)
WebSocketStateAction.listen = WebSocketStateAction(actions_constants.LISTEN)
WebSocketStateAction.message = WebSocketStateAction(actions_constants.MESSAGE)
WebSocketStateAction.start = WebSocketStateAction(actions_constants.START)
