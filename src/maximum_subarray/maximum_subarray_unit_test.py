#!/home/python/venv/main/bin/python
import sys
sys.path.append("..")
import unittest
from maximum_subarray import maximum_subarray

class MaximumSubarrayTest(unittest.TestCase):
  def test_default_values_vanilla(self):
    param1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6
    result = maximum_subarray.maximum_subarray(param1)
    self.assertEqual(expected, result)

  def test_extended_values_vanilla(self):
    param1 = [-2, 1, -3, 4, -1, 2, 1, -6, 4, 1, 1]
    expected = 6
    result = maximum_subarray.maximum_subarray(param1)
    self.assertEqual(expected, result)

  def test_default_values_indices(self):
    param1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = [6, 3, 6]
    response = maximum_subarray.maximum_subarray_with_indices(param1)
    self.assertEqual(expected, response)
    
  def test_extended_values_indices(self):
    param1 = [-2, 1, -3, 4, -1, 2, 1, -6, 4, 1]
    expected = [6, 3, 6]
    response = maximum_subarray.maximum_subarray_with_indices(param1)
    self.assertEqual(expected, response)

if __name__ == "__main__":
  unittest.main()
