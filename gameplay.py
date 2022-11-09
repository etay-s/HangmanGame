from hangman import Hangman
from sketch import Sketch
import consant_sketches as cs

class Gameplay():
    def __init__(self) -> None:
        self._hangman = Hangman()
        self._sketch = Sketch()
        self._sketch.sketch = Sketch.hanged_man()

    def show_sketch(self):
        return '\n'.join(''.join(line) for line in self._sketch.sketch)

    def lose_part(self, part):
        lost_parts = self._hangman.lose_part(part)
        for lost_part in lost_parts:
            y_coord, x_coord, _ = cs.HANGMAN[part.kind]
            # TODO: Generalize according to Sketch specs
            self._sketch.sketch[y_coord + 2][x_coord + 10] = cs.EMPTY

    def drop_part(self, part, x_coord, y_coord):
        self._sketch.sketch[y_coord + 1][x_coord] = self._sketch.sketch[y_coord][x_coord]
        self._sketch.sketch[y_coord][x_coord] = cs.EMPTY

if __name__ == '__main__':
    game = Gameplay()
    print(game.show_sketch())
