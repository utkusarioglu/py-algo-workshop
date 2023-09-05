class InsertionSort:
    def loop(self, unsorted: list[int]) -> list[int]:
        for i in range(1, len(unsorted)):
            for j in range(i, 0, -1):
                if unsorted[j - 1] > unsorted[j]:
                    temp = unsorted[j]
                    unsorted[j] = unsorted[j - 1]
                    unsorted[j - 1] = temp
        return unsorted
