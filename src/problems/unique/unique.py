# from decorator.decorator import duration

a: list[list[int]] = [[1, 2, 3], [1, 2, 3]]
L = list[int]


class Unique:
    # @duration
    def through_set(self, lst: L) -> L:
        return list(set(lst))

    def through_loop(self, lst: L) -> L:
        unique_items = []
        for item in lst:
            if item not in unique_items:
                unique_items.append(item)
        return unique_items
