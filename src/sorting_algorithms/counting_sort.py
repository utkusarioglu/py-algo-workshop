class CountingSort:
    def loop(self, unsorted: list[int]) -> list[int]:
        minValue = min(unsorted)
        maxValue = max(unsorted)
        counts = [0 for _ in range(maxValue - minValue + 1)]
        for elem in unsorted:
            counts[elem - minValue] += 1
        sortedArray = []
        for offset, val in enumerate(counts):
            for _ in range(val):
                sortedArray.append(minValue + offset)
        return sortedArray
