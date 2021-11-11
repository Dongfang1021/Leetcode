# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes_val,track=[],[]
        
        while root!=None:
            
            if root.left!=None:
                track.append(root)  # since Left node should come first, we keep root for next turn
                root=root.left
            elif root.right!=None:   # when left is None but right node exists
                nodes_val.append(root.val)  # we push the root value and traverse the right sub tree
                root=root.right
            else:
                nodes_val.append(root.val)   # when we have reached a leaf node, we push the value and pop from stack
                if len(track)>0:
                    root=track.pop()
                    if root!=None:
                        root.left=None  #  eliminating the left sub tree, since it has already been traversed
                else:
                    root=None  # when track is empty
                    
        return nodes_val
                


        