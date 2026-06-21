class Solution:
    def helper(self, preorder, rootInd, bound):
        if rootInd[0] == len(preorder) or preorder[rootInd[0]] > bound:
            return None
        
        root = TreeNode(preorder[rootInd[0]])
        rootInd[0] += 1
        
        root.left = self.helper(preorder, rootInd, root.val)   # left < root.val
        root.right = self.helper(preorder, rootInd, bound)     # right < bound
        
        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        rootInd = [0]
        return self.helper(preorder, rootInd, float('inf'))
