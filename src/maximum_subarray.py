def maximum_subarray(numbers):
  if not len(numbers):
    return 0
  if len(numbers) ==1:
    return numbers[0]
  curr_sum = numbers[0]
  max_sum = curr_sum
  for curr in numbers:
    curr_sum = max(curr_sum, 0)
    curr_sum += curr
    max_sum = max(max_sum, curr_sum)
    print(max_sum, curr)
  return max_sum

def maximum_subarray_with_indices(numbers):
  # if not len(numbers):
  #   return 0
  # if len(numbers) == 1:
  #   return numbers[0], 0, 0
  # curr_sum = numbers[0]
  max_map = [[numbers[0], 0, 0]] # map indexed by start pos
  for i, curr in enumerate(numbers):
    if max_map[-1][0] < 0:
      # curr_sum = 0
      max_map.append([0, i, i])
    max_map[-1] = [max_map[-1][0] + curr, max_map[-1][1], i]
  return max_map
