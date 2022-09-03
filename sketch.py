import copy
import consant_sketches as cs
from body_parts import BodyParts as bp

class Sketch:
    def __init__(self) -> None:
        self._sketch = []

    @property
    def sketch(self):
        return self._sketch
    
    @sketch.setter
    def sketch(self, value):
        self._sketch = copy.deepcopy(value)

    # TODO: 1) Rephrase error message
    # TODO: 2) Add inuput validation and error
    @classmethod
    def connect_sketches(cls, sketch1, sketch2, start_row = 0):
        connected_sketch = []
        if len(sketch1) >= start_row + len(sketch2):
            for row1, row2 in zip(sketch1[start_row:start_row + len(sketch2)], sketch2):
                connected_sketch.append(row1 + row2)
            return sketch1[:start_row] + connected_sketch + sketch1[start_row + len(sketch2):]
        raise ValueError("start_row pushes sketch2 out of sketch1 bounds")

    @classmethod
    def man_sketch(cls):
        dimensions = cs.PERSON['dimensions']
        sketch = [[' '] * dimensions[1] for _ in range(dimensions[0])]
        for part in bp:
            part_value = cs.PERSON[part]
            sketch[part_value[0]][part_value[1]] = part_value[2]
        return sketch

    @classmethod
    def standing_man(cls):
        sketch = Sketch.man_sketch()
        return Sketch.connect_sketches(cs.GALLOWS, sketch, len(cs.GALLOWS) - len(sketch))

    @classmethod
    def hanged_man(cls):
        sketch = Sketch.man_sketch()
        return Sketch.connect_sketches(cs.GALLOWS, sketch, 2)