class StateAction(object):

    def __init__(self, action) -> None:
        pass

    def __str__(self) -> str:
        pass

    def __eq__(self, other) -> bool:
        pass

    # Necessary when __eq__ is defined
    # in order to make this class usable as a
    # dictionary key:

    def __hash__(self) -> float:
        pass
