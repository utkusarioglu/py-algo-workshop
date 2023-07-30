import random
from . import MaxHeap


def test_getMax(capsys):
    with capsys.disabled():
        params = list(range(20))
        for _ in range(10):
            instance = MaxHeap()
            random.shuffle(params)
            for param in params:
                instance.addNode(param)
            result = instance.getMax()
            expected = 19
            assert result == expected
