# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return 

        val = root.val
        if p.val <= val <= q.val or q.val <= val <= p.val:
            return root
        elif val < p.val:
            root = root.right
        else:
            root = root.left

        return self.lowestCommonAncestor(root, p, q)