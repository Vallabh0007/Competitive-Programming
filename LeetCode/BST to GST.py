#problem-https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
#author-Vallabh

#code
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        curr=0
        def util(node):
            nonlocal curr
            if node:
                util(node.right)
                curr+=node.val
                node.val=curr
                util(node.left)
        util(root)
        return root 