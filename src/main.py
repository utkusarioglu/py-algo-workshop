#!/home/python/venv/main/bin/python
from enum import Enum
from maximum_subarray import maximum_subarray, maximum_subarray_with_indices
from two_sum_2 import two_sum_2_hash_map, two_sum_2_pointers

algo = Enum("algo", ["two_sums_2", "maximum_subarray"])

def main(selected_algo):
  match selected_algo:
    case algo.two_sums_2:
      numbers = [1,3,4,5,7,10,12]
      target = 12
      return [
        two_sum_2_hash_map(numbers, target),
        two_sum_2_pointers(numbers, target)
      ]

    case algo.maximum_subarray:
      arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
      return [
        maximum_subarray(arr),
        maximum_subarray_with_indices(arr)
      ]

def print_result(result):
  [print(line) for line in ["--", selected_algo.name, *result]]

if __name__ == "__main__":
  selected_algo = algo.two_sums_2
  result = main(selected_algo)
  print_result(result)
