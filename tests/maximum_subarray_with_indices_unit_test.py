#!/home/python/venv/main/bin/python
import sys
sys.path.append("..")
import unittest
from src import maximum_subarray 

class MaximumSubarrayWithIndicesTest(unittest.TestCase):
  def test_default_values(self):
    param1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = [6, 3, 6]
    response = maximum_subarray.maximum_subarray_with_indices(param1)
    self.assertEqual(expected, response)
    
  def test_default_values(self):
    param1 = [-2, 1, -3, 4, -1, 2, 1, -6, 4, 1]
    expected = [6, 3, 6]
    response = maximum_subarray.maximum_subarray_with_indices(param1)
    self.assertEqual(expected, response)

if __name__ == "__main__":
  unittest.main()
