#!/home/python/venv/main/bin/python
from maximum_subarray import maximum_subarray_with_indices

if __name__ == "__main__":
  arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  print(arr)
  result = maximum_subarray_with_indices(arr)
  print(result)
