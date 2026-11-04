# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def rec(node):
            if node and node.left:
                if not (node.left.left or node.left.right):
                    return node.left.val + rec(node.right) if node.right else node.left.val  
                else:
                    return rec(node.left) + rec(node.right)
            return rec(node.right) if node else 0
        return rec(root)