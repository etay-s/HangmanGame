from random import sample
from body_parts import BodyParts

class Part:
    # TODO: Generalize range(?)
    _tie_breaker = (r for r in sample(range(4),4))

    def __init__(self, kind: BodyParts) -> None:
        self._kind = kind
        self._attached = True
        self._rank = kind.value
        if not kind.is_core:
            self._rank += next(Part._tie_breaker)

    @property
    def kind(self):
        return self._kind

    @property
    def attached(self):
        return self._attached

    def detach(self):
        self._attached = False

    @property
    def rank(self):
        return self._rank

    # TODO: Add inuput validation and error
    @rank.setter
    def rank(self, value):
        self._rank = value
