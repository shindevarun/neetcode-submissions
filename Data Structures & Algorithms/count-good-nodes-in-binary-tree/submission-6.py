# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS but just keep track of max value so far at every node
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0

        def dfs(curr, maxSoFar):
            if not curr:
                return

            if curr.val >= maxSoFar:
                self.goodNodes += 1

            currMax = max(maxSoFar, curr.val)

            dfs(curr.left, currMax)
            dfs(curr.right, currMax)

        dfs(root, root.val)

        return self.goodNodes