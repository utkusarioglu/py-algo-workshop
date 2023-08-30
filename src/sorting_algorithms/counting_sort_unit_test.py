from .counting_sort import CountingSort


def test_321(capsys):
    with capsys.disabled():
        unsorted = [3, 2, 1, 3, 1]
        instance = CountingSort()
        response = instance.loop(unsorted)
        assert response == sorted(unsorted)
