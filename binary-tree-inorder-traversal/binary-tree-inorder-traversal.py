# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.rtn = []
        self.helper(root)
        return self.rtn
    
    def helper(self, node):
        if node.left:
            self.helper(node.left)
        self.rtn.append(node.val)
        if node.right:
            self.helper(node.right)
        