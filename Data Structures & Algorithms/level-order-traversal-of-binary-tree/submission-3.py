# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS: You start by creating a queue and append the root into it. This queue now represents the 1st level of the tree.
# Then, pop the queue 1 time (len(queue) = 1), add that Node's value if not null to a list that keeps tracks of values in that level.
# And if not null, add that nodes's children to the queue. Now that level is done so add the level list to res. 
# Now queue has 2 nodes, so iterate through queue twice. Popleft, if not null add to level and add children to queue. Same for right.
# Then add this level to the res. This happens until the queue becomes empty.
# This algorithm just adds the try level by level to the res list
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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

            if level: # level could just have null nodes / empty list
                res.append(level)

        return res