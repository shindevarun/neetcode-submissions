# sliding window where we move start left and right at 0 and 1. we move right in ever iteration. if the new price at right
# is greater than the price at left, current profit is the difference between the 2. keep track of maxProfit too.
# if the new price at right is less than the price at left, you found a new lower price which gauruntees that the profit will be bigger
# if you buy at this new price, so move left of the window to this right position and move right forward by 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                currProfit = prices[r] - prices[l]
                maxProfit = max(currProfit, maxProfit)
                r += 1
            else:
                l = r
                r = l + 1

        return maxProfit