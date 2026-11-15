class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use set for constant lookup
        numSet = set(nums)
        longest = 0

        # only consider numbers that can be start of sequences
        for num in nums:
            if (num - 1) not in numSet:
                currLength = 0

                while(num + currLength) in numSet:
                    currLength += 1
                
                if currLength > longest:
                    longest = currLength
        
        return longest
