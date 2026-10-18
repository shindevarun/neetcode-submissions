# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS algorithm. Go to each node and then swap the children
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root is None:
        #     return

        # temp = root.left
        # root.left = root.right
        # root.right = temp

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        if root is None:
            return

        leftNode = root.left
        root.left = root.right
        root.right = leftNode

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root