def two_sum_2_hash_map(numbers, target):
    viable_numbers = filter(lambda n: n <= target, numbers)
    number_map = {}
    for i, curr in enumerate(viable_numbers):
        complement = target - curr
        if complement in number_map:
            indices = [number_map[complement], i]
            return [i + 1 for i in indices]
        number_map[curr] = i
    return False


def two_sum_2_pointers(numbers, target):
    p_left = 0
    p_right = len(numbers) - 1
    while p_left < p_right:
        current_sum = numbers[p_left] + numbers[p_right]
        if current_sum > target:
            p_right -= 1
        elif current_sum < target:
            p_left += 1
        else:
            return [p_left + 1, p_right + 1]
    return []
