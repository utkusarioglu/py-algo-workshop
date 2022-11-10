#!/home/python/venv/main/bin/python
import sys
sys.path.append("..")
import unittest
from src import maximum_subarray

class MaximumSubarrayTest(unittest.TestCase):
  def test_default_values(self):
    param1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6
    result = maximum_subarray.maximum_subarray(param1)
    self.assertEqual(expected, result)

  def test_extended_values(self):
    param1 = [-2, 1, -3, 4, -1, 2, 1, -6, 4, 1, 1]
    expected = 6
    result = maximum_subarray.maximum_subarray(param1)
    self.assertEqual(expected, result)

if __name__ == "__main__":
  unittest.main()
