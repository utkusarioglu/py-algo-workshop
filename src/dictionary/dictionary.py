def tuple_keys():
    a = {(2, 3): 4}
    return a


def comprehension():
    a = [
        1,
        2,
    ]
    b = [
        4,
        5,
    ]
    return dict([a, b])


def array_merge_to_dict():
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    d = {}
    if len(a) != len(b):
        raise "Error: Unequal array lengths"
    for i in range(len(a)):
        d[a[i]] = b[i]
    return d


def negative_index():
    a = [1, 2, 3, 4]
    a[-1] = 5
    return a
