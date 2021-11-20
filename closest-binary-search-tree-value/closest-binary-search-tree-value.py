# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        return min(inorder(root), key = lambda x: abs(target - x))
        