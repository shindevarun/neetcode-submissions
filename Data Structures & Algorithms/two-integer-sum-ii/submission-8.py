# start 2 pointers at either end of array. if sum is bigger than target, you need to lower the sum so move right pointer left by 1.
# if sum is smaller than target, you need to increase the sum so move the left pointer right by 1.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l ,r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l+1, r+1]
