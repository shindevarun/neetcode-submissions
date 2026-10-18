# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# You need to just do inorder traversal of the BST since inorder of BST will organize nodes in ascending order
# due to BST property. kth smallest in ascending list is just list[k-1]
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(curr):
            if not curr:
                return

            inorder(curr.left)
            res.append(curr.val) # in order: visit left first, then mark curr, then visit right
            inorder(curr.right)

        inorder(root)

        return res[k-1]