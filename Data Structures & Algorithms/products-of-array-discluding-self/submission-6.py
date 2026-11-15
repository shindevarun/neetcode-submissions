# optimal solution O(N). create a prefixProduct and postfixProduct list for nums.
# prefix product is product of all preceding elements for each index as you iterate through list. This can be done in single pass
# likewise postfix product is product of all preceding elements for each index as you iterate backwards through list.
# so now with single passes, you have a list that tells you the product on left of each index and another list that tells you the product
# on right of each index. therefore last pass just multiply the prefix and postfix product lists
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1]*len(nums)
        postfixProduct = [1]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                # leave each edge of prefix & postfix product as 1
                continue
            else:
                prefixProduct[i] = prefixProduct[i-1]*nums[i-1] # prefix product

                # postfix product is len(nums) - i - 1st index due to 0 indexing
                postfixProduct[len(nums)-i-1] = postfixProduct[len(nums)-i]*nums[len(nums)-i] 

        res = []
        for i in range(len(nums)):
            res.append(prefixProduct[i] * postfixProduct[i])

        return res

        
        