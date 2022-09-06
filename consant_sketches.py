from body_parts import BodyParts as bp

HANGMAN = {
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
