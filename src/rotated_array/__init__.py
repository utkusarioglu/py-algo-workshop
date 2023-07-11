class RotatedArray:
    def findMin(self, nums: list[int]) -> int:
        leftIndex = 0
        rightIndex = len(nums) - 1
        while leftIndex < rightIndex:
            midIndex = (leftIndex + rightIndex) // 2
            print(leftIndex, rightIndex, midIndex)
            if (nums[midIndex] > nums[leftIndex] or
                    nums[midIndex] > nums[rightIndex]):
                print("true")
                leftIndex = midIndex + 1
            else:
                rightIndex = midIndex
        return nums[rightIndex]
