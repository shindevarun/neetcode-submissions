class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = dict()

        for i, n in enumerate(nums):
            mapping.update({n: i})

        print(mapping)
        for i, n in enumerate(nums):
            diff = target - n
            if(diff in mapping and mapping[diff] != i):
                # if i < mapping[diff]:
                #     return[i, mapping[diff]]
                # else:
                #     return [mapping[diff], i]
                return[i, mapping[diff]]
                