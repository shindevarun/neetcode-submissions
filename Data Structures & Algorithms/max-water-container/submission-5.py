# 2 pointer approach: start the 2 pointers on either side of container to maximize distance
# then calculate the area for those 2 bars. the area will be bounded by the shorter height.
# then, we need to choose one of the pointers. we need to move the shorter height pointer inward. this is because this is the 
# only option to potentially increase area. moving the taller pointer results in keeping the minHeight the same while reducing the
# width so there is no possibility to increase the area. so at every iteration updating the current Area and then always moving
# the shorter height's pointer inwards allows you to optimally check meaningful boxes and get the max area
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

        