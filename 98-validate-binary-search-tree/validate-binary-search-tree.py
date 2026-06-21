# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self,root,mini,maxi):
        if root==None:
            return True
        if not (mini<root.val<maxi):
            return False
        return self.validate(root.left,mini,root.val) and self.validate(root.right,root.val,maxi)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root,float('-inf'),float('inf'))