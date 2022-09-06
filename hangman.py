import heapq
from body_parts import BodyParts as bp
from part import Part

import os
from time import sleep

class Hangman:
    def __init__(self) -> None:
        self._parts = {part: Part(part) for part in bp}
        self._hangman_body = [(part.rank, part) for part in self._parts.values()]
        heapq.heapify(self._hangman_body)

    def lose_part(self, part : bp = None):
        lost_parts = []
        if part:
            # TODO: Fix for missing hand
            if part == bp.LOWER_BODY:
                lower_body_rank = self._parts[bp.LOWER_BODY].rank
                hands_order = int(
                    self._parts[bp.LEFT_HAND].rank > self._parts[bp.RIGHT_HAND].rank
                    )
                self._parts[bp.LEFT_HAND].rank = lower_body_rank + 1 + hands_order
                self._parts[bp.RIGHT_HAND].rank = lower_body_rank + 2 - hands_order

            if self._parts[part].kind.is_core:
                while min(self._hangman_body)[-1].kind != part:
                    self._detach_part(lost_parts)
            else:
                # TODO: Look for a better way of removing a non-core part
                hold_parts = []
                while min(self._hangman_body)[-1].kind != part:
                    hold_parts.append(heapq.heappop(self._hangman_body))
                self._detach_part(lost_parts)
                while hold_parts:
                    heapq.heappush(self._hangman_body, hold_parts.pop())
        else:
            self._detach_part(lost_parts)

        return lost_parts

    def _detach_part(self, lost_parts: list[Part]):
        _, lost_part = heapq.heappop(self._hangman_body)
        lost_part.detach()
        lost_parts.append(lost_part)

# ----------------------------------------------------------------------
def show():
    _ = os.system('clear') if os.name == 'posix' else os.system('cls')
    #print(hm.show_hangman())
    sleep(1)

def step(part=None):
    _ = os.system('clear') if os.name == 'posix' else os.system('cls')
    hm.lose_part(part)
    #print(hm.show_hangman())
    sleep(1)

if __name__ == '__main__':
    hm = Hangman()
    print([p.kind for p in hm.lose_part(bp.LEFT_LEG)])
    #show()
    # for _ in range(7):
    #     step()
    # step(bp.HEAD)

    # risk leves - low, medium, high, all or nothing
    # remove by risk and drop lower priorities
