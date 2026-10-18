# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs where you recurse on both trees simulatanesously since isSameTree function takes both roots as parameters.
# You just need to validate that at every iteration, your left subtree and right subtree is equivalent for both trees. And also
# the value of the p and q node is equivalent.
# These are the base cases. If you hit any of these, return False immediately and it doesn't continue recursing. A single False
# will make the entire outcome False since using the "and" operator
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True # base case of null nodes

        if not p or not q:
            return False # base case of one node has value while the other is null
        
        if p.val != q.val:
            return False # base case of the 2 corresponding values being different

        left = self.isSameTree(p.left, q.left) # true if both trees' left subtrees are equal
        right = self.isSameTree(p.right, q.right) # true if both trees' right subtrees are equal

        return (left and right)
            
