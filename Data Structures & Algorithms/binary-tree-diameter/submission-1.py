# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# general approach: at each node, you want to get the height of the left subtree and the height of the right subtree.
# the height of the left subtree + height of the right subtree will give you the diameter. to get heights, we run
# a dfs algorithm that also computes the diameter and updates the global diameter at every iteration

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        # height function
        def dfs(curr):
            if curr is None:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.diameter = max(self.diameter, left+right)
            
            return 1 + max(left, right)
        
        dfs(root)

        return self.diameter
        