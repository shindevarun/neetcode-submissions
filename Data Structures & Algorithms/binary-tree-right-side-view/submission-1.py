# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Just standard tree BFS. Only difference is we add last value in each level to res instead of the whole level
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                curr = q.popleft()

                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)

            if level:
                res.append(level[-1])

        return res