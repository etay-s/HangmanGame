from aenum import Enum, NoAlias

class BodyParts(Enum, settings=(NoAlias)):
    LEFT_LEG = 0
    RIGHT_LEG = 0
    LEFT_HAND = 0
    RIGHT_HAND = 0
    LOWER_BODY = 4
    UPPER_BODY = 7
    HEAD = 8

    @property
    def is_core(self):
        return self in [BodyParts.LOWER_BODY, BodyParts.UPPER_BODY, BodyParts.HEAD]
