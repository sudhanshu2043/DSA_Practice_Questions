# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self,preorder,left,right,target):
        for i in range(left,right+1):
            if preorder[i]>target:
                return i
        return right+1
    def helper(self,preorder,rootInd,left,right):
        if left>right or rootInd[0] >= len(preorder):
            return None
        root=TreeNode(preorder[rootInd[0]])
        split=self.search(preorder,left,right,preorder[rootInd[0]])
        rootInd[0]=rootInd[0]+1
        # Left subtree: values < rootVal
        root.left = self.helper(preorder, rootInd, rootInd[0], split-1)
        # Right subtree: values > rootVal
        root.right = self.helper(preorder, rootInd, split, right)
        
        return root
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==1:
            return TreeNode(preorder[0])
        rootInd=[0]
        return self.helper(preorder,rootInd,0,len(preorder)-1)