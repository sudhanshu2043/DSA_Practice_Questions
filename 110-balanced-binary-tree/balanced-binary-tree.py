# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findheight(self,root):
        if root==None: return 0
        left=self.findheight(root.left)
        if left==-1: return -1
        right=self.findheight(root.right)
        if right==-1: return -1
        if abs(left-right)>1: return  -1
        return 1+max(left,right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None: return True
        if root.left==None and root.right==None: return True
        return self.findheight(root)!=-1
        