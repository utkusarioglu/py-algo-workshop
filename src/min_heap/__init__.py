class MinHeap:
    def __init__(self) -> None:
        self.heap = []
        self.size = 0

    def getMin(self) -> int:
        return self.heap[0]

    def getHeap(self) -> list[int]:
        return self.heap

    def getParent(self, i: int) -> int:
        return (i - 1) // 2

    def getLeft(self, i: int) -> int:
        return 2 * i + 1

    def getRight(self, i: int) -> int:
        return self.getLeft(i) + 1

    def addNode(self, value: int) -> None:
        self.size += 1
        self.heap.append(value)
        self.heapify(self.size - 1)

    def heapify(self, i: int) -> None:
        parent = self.getParent(i)
        while i != 0 and self.heap[parent] > self.heap[i]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[parent]
            self.heap[parent] = tmp
            i = parent
            parent = self.getParent(i)

    def validate(self) -> bool:
        for i in range(self.size):
            left_i = self.getLeft(i)
            right_i = self.getRight(i)
            if left_i >= self.size or right_i >= self.size:
                continue
            parent_val = self.heap[i]
            left_val = self.heap[left_i]
            right_val = self.heap[right_i]
            if left_val < parent_val or right_val < parent_val:
                print(left_val, right_val, parent_val)
                return False
        return True
