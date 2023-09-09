from random import randint
from typing import Union

Element = Union[int, float]


def shuffle(vanilla: list[Element]) -> list[Element]:
    shuffled = vanilla.copy()
    for i in range(len(vanilla) - 1, -1, -1):
        j = randint(0, i)
        shuffled[i], shuffled[j] = (shuffled[j], shuffled[i])
    return shuffled
