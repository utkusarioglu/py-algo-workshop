#!/home/python/venv/main/bin/python
import sys

sys.path.append("..")
import unittest
from two_sum_2.two_sum_2 import two_sum_2_hash_map, two_sum_2_pointers


class TwoSum2Test(unittest.TestCase):
    def test_hash_map(self):
        numbers = [1, 3, 4, 5, 7, 10, 12]
        target = 9
        expected = [3, 4]
        response = two_sum_2_hash_map(numbers, target)
        self.assertEqual(expected, response)

    def test_pointers(self):
        numbers = [1, 3, 4, 5, 7, 10, 12]
        target = 9
        expected = [3, 4]
        response = two_sum_2_pointers(numbers, target)
        self.assertEqual(expected, response)


if __name__ == "__main__":
    unittest.main()
