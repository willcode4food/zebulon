from __future__ import annotations


class State(object):
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        pass

    def next(self, input) -> State:
        pass
