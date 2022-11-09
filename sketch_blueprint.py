from dataclasses import dataclass

# TODO: Modify to support diagonal / multiple cells of same character/part
@dataclass
class Blueprint():
    y: int
    x: int
    character: str
    count: int = 1
    direction: int = 0