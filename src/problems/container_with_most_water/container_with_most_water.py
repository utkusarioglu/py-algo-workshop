class ContainerWithMostWater:
    def greedy(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        local_max = 0
        while right > left:
            height = min(heights[left], heights[right])
            distance = right - left
            local_max = max(local_max, height * distance)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return local_max
