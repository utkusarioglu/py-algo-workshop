from .insertion_sort import InsertionSort as Sorter


def test_321(capsys):
    with capsys.disabled():
        unsorted = [3, 2, 1, 3, 1]
        instance = Sorter()
        response = instance.loop(unsorted)
        assert response == sorted(unsorted)


def test_101(capsys):
    with capsys.disabled():
        unsorted = [i for i in range(101)]
        unsorted.reverse()
        instance = Sorter()
        response = instance.loop(unsorted)
        assert response == sorted(unsorted)


def test_1001(capsys):
    with capsys.disabled():
        unsorted = [i for i in range(1001)]
        unsorted.reverse()
        instance = Sorter()
        response = instance.loop(unsorted)
        assert response == sorted(unsorted)


def test_unison(capsys):
    with capsys.disabled():
        unsorted = [1 for _ in range(1001)]
        unsorted.reverse()
        instance = Sorter()
        response = instance.loop(unsorted)
        assert response == sorted(unsorted)
