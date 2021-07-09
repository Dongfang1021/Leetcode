class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        res = 0
        left = 0
        right = len(height) - 1
        for i in range(len(height)):
            width = abs(left - right)
            if height[left] < height[right]:
                res = width * height[left]
                left += 1
            else:
                res = width * height[right]
                right -= 1
            if water < res:
                water = res
        return water
        