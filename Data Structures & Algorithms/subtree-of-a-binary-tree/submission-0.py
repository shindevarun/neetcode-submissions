# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: 
            return True

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


    def isSameTree(self, s, t):
        if not s and not t:
            return True # base case of null nodes

        if not s or not t:
            return False # base case of one node has val while the other is null

        if s.val != t.val:
            return False # base case of same node in different trees have different vals

        left = self.isSameTree(s.left, t.left) # true if both's left subtree are equal
        right = self.isSameTree(s.right, t.right) # true if both's right subtree are equal

        return (left and right)
    

    
        