# hashset method 1: iterate through nums and put all seen values into a hashset. Then 
# when you go to next value, check if it is alredy in the hashset. This is a O(1) lookup
# operation due to hashset. 

# hashset method 2: convert the whole nums into a hashset. Compare length of the hashset
# to the length of nums. The lengths will be the same if there are no duplicates in nums
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset method 1:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False