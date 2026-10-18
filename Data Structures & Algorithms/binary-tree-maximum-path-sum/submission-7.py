# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def dfs(curr, leftMax, rightMax):
            if not curr:
                return 0

            leftMaxCurr = dfs(curr.left, leftMax, rightMax)
            rightMaxCurr = dfs(curr.right, leftMax, rightMax)
            
            # case 1: path sum = leftMax + currNode + rightMax
            currSum1 = leftMaxCurr + curr.val + rightMaxCurr

            # case 2: path sum = leftMax + currNode
            currSum2 = leftMaxCurr + curr.val

            # case 3: path sum = currNode + rightMax
            currSum3 = curr.val + rightMaxCurr

            # case 4: path sum = just currNode and not it's values
            currSum4 = curr.val

            currMaxSum = max(currSum1, currSum2, currSum3, curr.val)
            if currMaxSum > self.maxSum:
                self.maxSum = currMaxSum

            return max(currSum2, currSum3, currSum4)

        dfs(root, float('-inf'), float('-inf'))

        return self.maxSum

