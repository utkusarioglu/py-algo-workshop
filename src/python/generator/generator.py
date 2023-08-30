class first_n(object):
    def __init__(self, n) -> None:
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        raise StopIteration()


def first_n_generator(n: int) -> int:
    num = 0
    while num < n:
        yield num
        num += 1
