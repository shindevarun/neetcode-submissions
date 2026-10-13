# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# use same isSameTree helper function as last problem. Brute force is the only way. For each node in root, you want
# to check if the subRoot tree is a subtree of that node. If subRoot is null, it is a subtree of the root. If root 
# is null, subRoot can never be a subtree of root. O(m*n) where m is size of root and n is size of subRoot
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: 
            return True # empty subRoot is always a subtree of root

        if not root:
            return False # subRoot can never be a subtree of empty root

        if self.isSameTree(root, subRoot): # check if subRoot is a subtree of the current node in root
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) # DFS to check all nodes in root


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
    

    
        