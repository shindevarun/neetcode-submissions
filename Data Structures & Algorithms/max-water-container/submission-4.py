class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostWater = 0

        l, r = 0, len(heights) - 1

        while l < r:
            minHeight = min(heights[l], heights[r])
            currWater = minHeight * (r-l)

            if currWater > mostWater: mostWater = currWater
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            
        return mostWater

        