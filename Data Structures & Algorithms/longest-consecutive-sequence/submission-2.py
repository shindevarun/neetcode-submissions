# first turn nums to a hashset for constant lookup
# then instead of checking sequence length of every num in nums, you want to check for sequences only for actual sequence starts
# this means only nums for who nums - 1 does not exist in the numSet. since this means that num is gaurunteed to be the start of a new sequence
# then for each of these candiate, just do a while loop where you you check if currLength + num is still in numSet. if it is, increment currLength. so this allows you to get sequence lengths for each new sequence
# then just return the longest of these
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
