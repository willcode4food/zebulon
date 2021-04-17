from __future__ import annotations


class State(object):

    def run(self) -> None:
        pass

    def next(self) -> State:
        pass
