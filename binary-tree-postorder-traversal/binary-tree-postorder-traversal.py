# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def postorder(node, output):
            if node.left:
                postorder(node.left, output)
            if node.right:
                postorder(node.right, output)
            output.append(node.val)
        if not root:
            return output
        postorder(root, output)
        return output
