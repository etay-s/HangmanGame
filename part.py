from random import sample
from body_parts import BodyParts

class Part:
    _tie_breaker = (r for r in sample(range(4),4))

    def __init__(self, kind: BodyParts) -> None:
        self.kind = kind
        self.attached = True
        self.rank = kind.value
        if kind not in [BodyParts.HEAD, BodyParts.UPPER_BODY, BodyParts.LOWER_BODY]:
            self.rank += next(Part._tie_breaker)

    def detach(self):
        self.attached = False

    # TODO: getters and setters

    # def __getattribute__(self, __name):
    #     pass

    # def __setattr__(self, __name, __value):
    #     pass