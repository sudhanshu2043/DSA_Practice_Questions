# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,inorder):
        if root==None:
            return
        inorder.append(root.val)
        self.dfs(root.left,inorder)
        self.dfs(root.right,inorder)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        inorder=[]
        self.dfs(root,inorder)
        temp = root
        temp.val = inorder[0]  # Set root value
        temp.left = None
        for i in range(1,len(inorder)):
            temp.right=TreeNode(inorder[i])
            temp=temp.right
        