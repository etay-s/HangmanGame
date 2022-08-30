import heapq
from importlib.abc import PathEntryFinder
from body_parts import BodyParts as bp
from part import Part
from sketches import Sketch

import os
from time import sleep

class Hangman:
    _sketch = Sketch.hanged_man()
    _parts = {part: Part(part) for part in bp}
    _hangman_body = [(part.rank, part) for part in _parts.values()]
    heapq.heapify(_hangman_body)

    def show_hangman(self):
        return '\n'.join(''.join(line) for line in self._sketch)

    def lose_part(self, part=None):
        dropped_parts = []
        if part:
            if part == bp.LOWER_BODY:
                lower_body_rank = self._parts[bp.LOWER_BODY].rank
                hands_order = int(self._parts[bp.LEFT_HAND].rank > self._parts[bp.RIGHT_HAND].rank)
                self._parts[bp.LEFT_HAND].rank = lower_body_rank + 1 + hands_order
                self._parts[bp.RIGHT_HAND].rank = lower_body_rank + 2 - hands_order

            while(min(self._hangman_body)[-1].kind != part):
                _, dropped_part = heapq.heappop(self._hangman_body)
                self.detach_part(dropped_part)
        _,  lost_part = heapq.heappop(self._hangman_body)
        self.detach_part(lost_part)

    def detach_part(self, part: Part):
        part.detach()
        y, x, _ = Sketch.PERSON[part.kind]
        self._sketch[y+2][x+10] = ' ' # TODO: Generalize according to Sketch specs

    def drop_part(self, part, x, y):
        self._sketch[y + 1][x] = self._sketch[y][x]
        self._sketch[y][x] = ' '
        

def show():
    os.system('clear') if os.name == 'posix' else os.system('cls')
    print(hm.show_hangman())
    sleep(1)

def step(part=None):
    os.system('clear') if os.name == 'posix' else os.system('cls')
    hm.lose_part(part)
    print(hm.show_hangman())
    sleep(1)

if __name__ == '__main__':
    hm = Hangman()
    show()
    # for _ in range(7):
    #     step()
    # step(bp.HEAD)

    # priorities parts - heapq
    # risk leves - low, medium, high, all or nothing
    # remove by risk and drop lower priorities