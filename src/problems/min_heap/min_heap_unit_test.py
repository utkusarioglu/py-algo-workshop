from . import MinHeap
import random


def test_getMin(capsys):
    with capsys.disabled():
        params = list(range(20))
        for _ in range(20):
            instance = MinHeap()
            random.shuffle(params)
            for param in params:
                instance.addNode(param)
            result = instance.getMin()
            expected = 0
            assert result == expected
            assert instance.validate()
