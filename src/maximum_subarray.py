def maximum_subarray(numbers):
  curr_sum = numbers[0]
  max_sum = curr_sum
  for curr in numbers:
    curr_sum = max(curr_sum, 0)
    curr_sum += curr
    max_sum = max(max_sum, curr_sum)
  return max_sum

def maximum_subarray_with_indices(numbers):
  curr_sum = numbers[0]
  max_map = [[curr_sum, 0, 0]]
  for i, curr in enumerate(numbers):
    if curr_sum < 0:
      curr_sum = 0
      max_map.append([curr_sum, i, i])
    curr_sum += curr
    if max_map[-1][0] < curr_sum:
      max_map[-1][0] = curr_sum
      max_map[-1][2] = i
  return max(max_map, key=lambda a: a[0])
