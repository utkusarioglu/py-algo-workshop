from typing import Union

Element = Union[int, float]
ElementOrNone = Union[Element, None]
Index = int


class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, newElement: Element) -> None:
        self.heap.append(newElement)
        currentIndex = len(self.heap) - 1
        while currentIndex > 0:
            currentValue = self.heap[currentIndex]
            parentIndex = self.getParentIndex(currentIndex)
            parentValue = self.heap[parentIndex]
            if parentValue < currentValue:
                return
            self.swap(parentIndex, currentIndex)
            currentIndex = parentIndex

    def getParentIndex(self, index: Index) -> Index:
        return (index - 1) // 2

    def getLeftChildIndex(self, index: Index) -> Index:
        return index * 2 + 1

    def getRightChildIndex(self, index: Index) -> Index:
        return index * 2 + 2

    def swap(self, i1: Index, i2: Index) -> None:
        self.heap[i1], self.heap[i2] = (self.heap[i2], self.heap[i1])

    def getHead(self) -> ElementOrNone:
        if not len(self.heap):
            return None
        return self.heap[0]

    def popHead(self) -> ElementOrNone:
        head = self.getHead()
        if head is None:
            return None
        lastValue = self.heap.pop()
        if len(self.heap):
            self.heap[0] = lastValue
        self.reorder(0)
        return head

    def reorder(self, currentIndex: Index) -> None:
        lastIndex = len(self.heap) - 1
        leftChildIndex = self.getLeftChildIndex(currentIndex)
        rightChildIndex = self.getRightChildIndex(currentIndex)
        if leftChildIndex > lastIndex:
            return
        leftChildValue = self.heap[leftChildIndex]
        rightChildValue = (
            float("inf")
            if rightChildIndex > lastIndex
            else self.heap[rightChildIndex]
        )
        smallestChildIndex = (
            leftChildIndex
            if leftChildValue < rightChildValue
            else rightChildIndex
        )
        smallestChildValue = self.heap[smallestChildIndex]
        currentValue = self.heap[currentIndex]
        if smallestChildValue < currentValue:
            self.swap(smallestChildIndex, currentIndex)
        self.reorder(smallestChildIndex)
