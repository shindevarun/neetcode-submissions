class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0

        left = 0
        right = len(heights) - 1

        while (right > left):
            minHeight = heights[right] if heights[left] > heights[right] else heights[left]

            area = minHeight * (right - left)

            most_water = area if area > most_water else most_water

            if(heights[right] < heights[left]):
                right -= 1
            else:
                left += 1

            
        return most_water
            

        