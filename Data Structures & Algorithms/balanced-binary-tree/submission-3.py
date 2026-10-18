# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# essentially same as previous problem. At every node, calculate the height of the left and right subtree.
# if the 2 heights a more than 1 apart, set a flag to false, else continue as normal 

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.balanced = True

        def dfs(curr):
            if curr is None:
                return 0

            leftMax = dfs(curr.left)
            rightMax = dfs(curr.right)

            if abs(leftMax - rightMax) > 1:
                self.balanced = False
            
            return 1 + max(leftMax, rightMax)

        dfs(root)
        return self.balanced
        