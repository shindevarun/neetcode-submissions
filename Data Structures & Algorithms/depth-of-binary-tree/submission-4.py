# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS. Take each node and then return 1 + the max of its subtree. So leaves return 1 and then all other nodes
# return 1 plus the max of its subtree. this way we keep track of the max
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        if root is None:
            return 0

        leftMax = 1 + self.maxDepth(root.left)
        rightMax = 1+ self.maxDepth(root.right)

        return max(leftMax, rightMax)
        