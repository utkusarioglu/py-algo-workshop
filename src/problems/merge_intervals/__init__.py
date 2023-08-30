class MergeIntervals:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda i: i[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            finish = intervals[i][1]
            if start > merged[-1][1]:
                merged.append([start, finish])
            else:
                curr = merged.pop()
                merged.append([
                    min([start, curr[0]]),
                    max([finish, curr[1]])
                ])
        return merged
