class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
        self.size = 0

    def getLeft(self, i: int) -> int:
        return 2 * i + 1

    def getRight(self, i: int) -> int:
        return self.getLeft(i) + 1

    def getParent(self, i: int) -> int:
        return (i - 1) // 2

    def heapify(self, i: int) -> None:
        parent = self.getParent(i)
        while i != 0 and self.heap[parent] < self.heap[i]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[parent]
            self.heap[parent] = tmp
            i = parent
            parent = self.getParent(i)

    def addNode(self, value: int) -> None:
        self.size += 1
        self.heap.append(value)
        self.heapify(self.size - 1)

    def getMax(self) -> int:
        return self.heap[0]

    def getHeap(self) -> int:
        return self.heap

    def validate(self) -> bool:
        i = 0
        while i < self.size:
            parent_val = self.heap[i]
            left_i = self.getLeft(i)
            right_i = self.getRight(i)
            i += 1
            if left_i >= self.size or right_i >= self.size:
                continue
            left_val = self.heap[left_i]
            right_val = self.heap[right_i]

            if parent_val < left_val or parent_val < right_val:
                return False
        return True
