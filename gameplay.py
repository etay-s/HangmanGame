from mimetypes import init
from hangman import Hangman
from sketch import Sketch

class Gameplay():
    def __init__(self) -> None:
        self._hangman = Hangman()
        self._sketch = Sketch()
        self._sketch.sketch = Sketch.hanged_man()    


if __name__ == '__main__':
    game = Gameplay()