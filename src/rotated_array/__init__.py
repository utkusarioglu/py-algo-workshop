class RotatedArray:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2
            left_num = nums[left]
            right_num = nums[right]
            mid_num = nums[mid]
            if mid_num > left_num and mid_num > right_num:
                left = mid
            else:
                right = mid
        return nums[right] if nums[right] < nums[left] else nums[left]
