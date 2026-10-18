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
        # keep track of max diameter
        self.diameter = 0

        # standard dfs function w/ small diameter tweak
        def dfs(curr):
            if curr is None:
                return 0

            leftMax = dfs(curr.left)
            rightMax = dfs(curr.right)

            # only new thing here: calculating diameter at every node and updating overall diamter if needed
            curr_diameter = leftMax + rightMax
            if curr_diameter > self.diameter:
                self.diameter = curr_diameter

            return 1 + max(leftMax, rightMax)

        dfs(root)
        return self.diameter
