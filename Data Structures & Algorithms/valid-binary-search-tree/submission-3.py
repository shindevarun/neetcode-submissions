# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS but we keep track of a range of allowed values for each node. The range starts with infinity for overall root.
# When you get to new node, you first check if the node's value is between the allowed range. If it's not return False.
# If it is, you then search left subtree and update range to change upper bound to be the current node's value.
# Likweise when you search right subtree, you update range to change lower bound to be the current node's value.
# If return the bool of left AND right subtrees to indicate whether those subtrees pass BST check 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(curr, min_val, max_val):
            if not curr:
                return True

            if not min_val < curr.val < max_val:
                return False

            leftValid = dfs(curr.left, min_val, curr.val)
            rightValid = dfs(curr.right, curr.val, max_val)
            
            return (leftValid and rightValid)

        return dfs(root, float('-inf'), float('inf'))