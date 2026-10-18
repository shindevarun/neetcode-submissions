# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS: at every node, you can have a path in 4 ways: left subtree + current node, right subtree + current node, left subtree + current node + right subtree,
# and just current node no subtrees. you find max of these 4 paths and compare it to global max path sum and update.
# What you return is max of 3 of these cases, you can't return the sum that is left + current + right subtree because this is a fork in the tree that the parent
# is not allowed to count as a sum, has to be a direct path
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def dfs(curr):
            if not curr:
                return 0

            leftMax= dfs(curr.left)
            rightMax = dfs(curr.right)
            
            # case 1: path sum = leftMax + currNode + rightMax
            currSum1 = leftMax + curr.val + rightMax

            # case 2: path sum = leftMax + currNode
            currSum2 = leftMax + curr.val

            # case 3: path sum = currNode + rightMax
            currSum3 = curr.val + rightMax

            # case 4: path sum = just currNode and not it's values
            currSum4 = curr.val

            currMaxSum = max(currSum1, currSum2, currSum3, curr.val)
            if currMaxSum > self.maxSum:
                self.maxSum = currMaxSum

            return max(currSum2, currSum3, currSum4) # don't include the fork path, currsum1 in this

        dfs(root)

        return self.maxSum

