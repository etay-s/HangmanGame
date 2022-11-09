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


    # TODO: Finish modifying to support sketch flexibility
    # @classmethod
    # def connect_sketches(cls, base_sketch, connect_sketch, start_row = 0, start_column = 0):
    #     result_sketch = copy.deepcopy(base_sketch)
    #     if (len(base_sketch) >= start_row + len(connect_sketch)
    #         and len(base_sketch[0]) >= start_column + len(connect_sketch[0])
    #         ):
    #         for y in range(start_row, len(connect_sketch)):
    #             for x in range(start_column, len(connect_sketch[0])):
    #                 # result_sketch = 
    #                 pass


    # TODO: Replace with above function
    @classmethod
    def connect_sketches(cls, base_sketch, connect_sketch, start_row = 0):
        connected_sketch = []
        if len(base_sketch) >= start_row + len(connect_sketch):
            for row1, row2 in zip(base_sketch[start_row:start_row + len(connect_sketch)], connect_sketch):
                connected_sketch.append(row1 + row2)
            return base_sketch[:start_row] + connected_sketch + base_sketch[start_row + len(connect_sketch):]
        raise ValueError("Connect sketch goes out of bounds of base sketch")

    #TODO: Genralize into one method (i.e. input type of sketch)
    @classmethod
    def man_sketch(cls):
        dimensions = cs.HANGMAN['dimensions']
        sketch = [[cs.EMPTY] * dimensions[1] for _ in range(dimensions[0])]
        for part in cs.HANGMAN['elements'].values():
            sketch[part.y][part.x] = part.character
        return sketch

    @classmethod
    def gallows_sketch(cls):
        dimensions = cs.GALLOWS['dimensions']
        sketch = [[cs.EMPTY] * dimensions[1] for _ in range(dimensions[0])]
        for part in cs.GALLOWS['elements'].values():
            if part.direction:
                for count in range(part.count):
                    sketch[part.y + count][part.x] = part.character
            else:
                for count in range(part.count):
                    sketch[part.y][part.x + count] = part.character
        return sketch

    @classmethod
    def standing_man(cls):
        sketch = Sketch.man_sketch()
        return Sketch.connect_sketches(cs.GALLOWS, sketch, len(cs.GALLOWS) - len(sketch))

    @classmethod
    def hanged_man(cls):
        sketch = Sketch.man_sketch()
        return Sketch.connect_sketches(Sketch.gallows_sketch(), sketch, 2)
