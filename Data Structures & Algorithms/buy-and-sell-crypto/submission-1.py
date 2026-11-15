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