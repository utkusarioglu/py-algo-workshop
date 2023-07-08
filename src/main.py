#!/home/python/venv/main/bin/python
from maximum_subarray.maximum_subarray import *
from two_sum_2.two_sum_2 import *
from house_robber.house_robber import HouseRobber
from complex_number.complex_number import *
from dictionary.dictionary import *
from generator.generator import *
from decorator.decorator import *
from unique.unique import *
from dunder.dunder import *
from longest_substring_without_repeats.substring import Solution
from number_reversal.number_reversal import NumberReversal


def two_sums_2():
    numbers = [1, 3, 4, 5, 7, 10, 12]
    target = 12
    return [
        two_sum_2_hash_map(numbers, target),
        two_sum_2_pointers(numbers, target),
    ]


def maximum_subarray():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    return [maximum_subarray(arr), maximum_subarray_with_indices(arr)]


def complex_number():
    return [complex_number()]


def tuple_keys():
    return [tuple_keys()[(2, 3)]]


def comprehension():
    return [comprehension()]


def array_merge_to_dict():
    return [array_merge_to_dict()]


def house_robber():
    house_robber = HouseRobber()
    return [house_robber.max_spoils_loop([1, 3, 1, 4])]


def negative_index():
    return [negative_index()]


def first_n():
    return [sum(first_n(10000000))]


def first_n_generator():
    return [sum(first_n_generator(1000))]


def decorated():
    return [decorated()]


def unique_through_set():
    lst = [1, 2, 3, 4, 4, 6, 7, 3, 4, 5, 2, 7]
    unique = Unique()
    return [unique.through_set(lst)]


def unique_through_loop():
    lst = [1, 2, 3, 4, 4, 6, 7, 3, 4, 5, 2, 7]
    unique = Unique()
    return [unique.through_loop(lst)]


def dunder():
    dunder = Dunder()
    del dunder["cc"]
    dunder += 2
    return [
        str(dunder),
        int(dunder),
        dunder["aa"],
        dunder["bb"],
        len(dunder),
        "x" in dunder,
        dunder + dunder,
        dunder(),
        dunder.__ne__,
        dir(dunder),
    ]


def longest_substring_without_repeats():
    solution = Solution()
    # param = "abcabcbb"
    param = "pwwkew"
    answer = solution.usingSets(param)
    return [answer]


def number_reversal():
    n = NumberReversal()
    param = -123
    # param = 1534236469
    answer = n.usingMath(param)
    return [answer]


def print_result(result):
    [print(line) for line in ["--", *result]]


if __name__ == "__main__":
    result = number_reversal()
    print_result(result)
