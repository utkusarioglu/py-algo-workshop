from math import ceil


class SmallestDivisor:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def getCeilSum(nums: list[int], divisor: int, threshold: int) -> bool:
            return sum([ceil(num / divisor) for num in nums]) > threshold

        upper_bound = max(nums)
        lower_bound = ceil(sum(nums) / threshold)
        
        while upper_bound > lower_bound:
            print(upper_bound, lower_bound)
            divisor = (upper_bound + lower_bound) // 2
            if getCeilSum(nums, divisor, threshold):
                lower_bound = divisor + 1
            else:
                upper_bound = divisor

        return lower_bound
