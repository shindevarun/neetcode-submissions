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
        if root is None:
            return 0

        maxHeightLeftSubtree = self.maxDepth(root.left) # 1
        maxHeightRightSubtree = self.maxDepth(root.right) # 2

        currHeight = 1 + max(maxHeightLeftSubtree, maxHeightRightSubtree) # 2

        return currHeight

        
        