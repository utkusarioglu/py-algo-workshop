import pytest
from min_heap import MinHeap
from src.shuffling_algorithms.fisher_yates import shuffle

TEST_CASES = [shuffle(list(range(50))) for _ in range(100)]


@pytest.fixture
def min_heap():
    minHeap = MinHeap()
    yield minHeap


@pytest.mark.parametrize("paramList", TEST_CASES)
def test_insert(min_heap, paramList):
    for param in paramList:
        min_heap.insert(param)
    head = min_heap.getHead()
    expected = min(paramList)
    assert head == expected


@pytest.mark.parametrize("paramList", TEST_CASES)
def test_pop(min_heap, paramList):
    for param in paramList:
        min_heap.insert(param)
    sortedList = []
    while min_heap.getHead() is not None:
        head = min_heap.popHead()
        sortedList.append(head)

    assert sortedList == sorted(paramList)
