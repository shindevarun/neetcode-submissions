# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# key is to use the BST property. We know that the overAll root will always be a common
# ancestor to all nodes in the tree, so we initalize the currNode to root. Then we 
# compare the values of p & q with the currNode. If both p & q are greater than currNode,
# we know currNode is not the LCA and also that p & q will have an LCA in the right subtree
# of the currNode, so we set currNode to the right subtree. Exact same for left. Last 2 cases
# are caught by else statement. If p is in the left subtree and q is in the right subtree
# of the currNode (or vice versa), we know that the currNode is the LCA of p & q. We also 
# know that if currNode is every equal to p or q, that it has to also be the LCA. All 
# of these are caught by the else statement
# Takes O(h) time where h is the height of the tree

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # currNode = root

        # while currNode is not None:
        #     if (p.val > currNode.val and q.val > currNode.val):
        #         currNode = currNode.right
        #     elif (p.val < currNode.val and q.val < currNode.val):
        #         currNode = currNode.left
        #     else:
        #         return currNode


        currNode = root

        while currNode is not None:
            if p.val > currNode.val and q.val > currNode.val:
                currNode = currNode.right
            elif p.val < currNode.val and q.val < currNode.val:
                currNode = currNode.left
            else:
                return currNode

        