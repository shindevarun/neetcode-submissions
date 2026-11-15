class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # mySet = set(nums)
        
        # if(len(mySet) == len(nums)):
        #     return False
        # else:
        #     return True

        # arr = []

        # for num in nums:
        #     if num in arr:
        #         return True
            
        #     arr.append(num)
        
        # return False

        return len(set(nums)) < len(nums)