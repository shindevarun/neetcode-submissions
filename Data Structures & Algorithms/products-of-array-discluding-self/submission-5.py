class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1]*len(nums)
        postfixProduct = [1]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                prefixProduct[i] = prefixProduct[i-1]*nums[i-1]
                postfixProduct[len(nums)-i-1] = postfixProduct[len(nums)-i]*nums[len(nums)-i]

        res = []
        for i in range(len(nums)):
            res.append(prefixProduct[i] * postfixProduct[i])

        return res

        
        