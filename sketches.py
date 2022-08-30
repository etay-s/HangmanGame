from body_parts import BodyParts as bp

class Sketch:
    PERSON = {
        'dimensions': (4,3),
        bp.HEAD: (0,1,'O'),
        bp.LEFT_HAND: (1,0,'/'),
        bp.UPPER_BODY: (1,1,'|'),
        bp.RIGHT_HAND: (1,2,'\\'),
        bp.LOWER_BODY: (2,1,'|'),
        bp.LEFT_LEG: (3,0,'/'),
        bp.RIGHT_LEG: (3,2,'\\')
    }

    # TODO: Simplify to specification form (e.g. PERSON above)
    # TODO: Use box drawing unicode characters
    GALLOWS = [
            [' ',' ',' ','_','_','_','_','_','_','_','_','_'],
            [' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ','|'],
            [' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
            ['_','_','_','|','_','_','_',' ',' ',' ']
        ]

    @staticmethod
    def connect_sketches(sketch1, sketch2, start_row = 0):
        connected_sketch = []
        if len(sketch1) >= start_row + len(sketch2):
            for row1, row2 in zip(sketch1[start_row:start_row + len(sketch2)], sketch2):
                connected_sketch.append(row1 + row2)
            return sketch1[:start_row] + connected_sketch + sketch1[start_row + len(sketch2):]
        raise ValueError("start_row pushes sketch2 out of sketch1 bounds")

    @staticmethod
    def man_sketch():
        dimensions = Sketch.PERSON['dimensions']
        sketch = [[' '] * dimensions[1] for _ in range(dimensions[0])]
        for part in bp:
            part_value = Sketch.PERSON[part]
            sketch[part_value[0]][part_value[1]] = part_value[2]
        return sketch

    @staticmethod
    def standing_man():
        sketch = Sketch.man_sketch()
        return Sketch.connect_sketches(Sketch.GALLOWS, sketch, len(Sketch.GALLOWS) - len(sketch))

    @staticmethod
    def hanged_man():
        sketch = Sketch.man_sketch()
        return Sketch.connect_sketches(Sketch.GALLOWS, sketch, 2)
