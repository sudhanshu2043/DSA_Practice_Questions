# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preInd=0
    def search(self,inorder,left,right,val):
        for i in range(left,right+1):
            if val==inorder[i]:
                return i
        return -1
    def buildTreeRecurrsive(self,preorder,inorder,preInd,left,right):
        if left>right :
            return None
        root=TreeNode(preorder[self.preInd])
        inInd=self.search(inorder,left,right,preorder[self.preInd])
        self.preInd+=1
        root.left=self.buildTreeRecurrsive(preorder,inorder,self.preInd,left,inInd-1)
        root.right=self.buildTreeRecurrsive(preorder,inorder,self.preInd,inInd+1,right)
        return root
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeRecurrsive(preorder,inorder,self.preInd,0,len(preorder)-1)