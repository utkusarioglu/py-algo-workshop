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
from class_vars import ClassVars
from koko import Koko
from smallest_divisor import SmallestDivisor
from rotated_array import RotatedArray

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
    print(answer)


def koko():
    instance = Koko()
    piles = [3, 6, 7, 11]
    h = 8

    piles = [30, 11, 23, 4, 20]
    h = 5

    piles = [30, 11, 23, 4, 20]
    h = 6

    # piles = [312884470]
    # h = 312884469

    # piles = [312884470]
    # h = 968709470

    print(instance.iterative(piles, h))


def smallestDivisor():
    instance = SmallestDivisor()
    nums = [1, 2, 5, 9]
    threshold = 6
    # Output: 5

    nums = [1, 2, 3]
    threshold = 3
    # Output: 3

    # nums = [21212, 10101, 12121]
    # threshold = 1000000
    # Output: 1

    # nums = [44, 22, 33, 11, 1]
    # threshold = 5
    # Output: 44
    
    output = instance.smallestDivisor(nums, threshold)
    print(output)


def rotatedArray():
    instance = RotatedArray()
    nums = [3, 4, 5, 6, 2]
    # Output: 1

    nums = [4,5,6,7,0,1,2]
    # Output: 0

    output = instance.findMin(nums)
    print(output)


if __name__ == "__main__":
    rotatedArray()
