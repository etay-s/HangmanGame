from body_parts import BodyParts as bp
from sketch_blueprint import Blueprint

EMPTY = ' '

HANGMAN = {
    'dimensions': (4,3),
    'elements': {
        bp.HEAD: Blueprint(0,1,'O'),
        bp.LEFT_HAND: Blueprint(1,0,'/'),
        bp.UPPER_BODY: Blueprint(1,1,'|'),
        bp.RIGHT_HAND: Blueprint(1,2,'\\'),
        bp.LOWER_BODY: Blueprint(2,1,'|'),
        bp.LEFT_LEG: Blueprint(3,0,'/'),
        bp.RIGHT_LEG: Blueprint(3,2,'\\')
    }
    
    }

# TODO: Simplify to specification form (e.g. PERSON above)
# TODO: Use box drawing unicode characters
GALLOW = [
        [' ',' ',' ','_','_','_','_','_','_','_','_','_'],
        [' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ','|'],
        [' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
        ['_','_','_','|','_','_','_',' ',' ',' ']
    ]

GALLOWS = {
    'dimensions': (8,12),
    'elements': {
        'left_base': Blueprint(7,0,'_',3),
        'right_base': Blueprint(7,4,'_',3),
        'pole': Blueprint(1,3,'|',7,1),
        'bar': Blueprint(0,3,'_',9),
        'rope': Blueprint(1,11,'|')
    }
}