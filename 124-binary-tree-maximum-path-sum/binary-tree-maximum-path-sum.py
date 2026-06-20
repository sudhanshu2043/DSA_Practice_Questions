# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, root, ans):
        if root is None: 
            return 0
        
        # Get the maximum path sum from left and right subtrees.
        # If the path sum is negative, we prune it by taking 0.
        left = max(0, self.func(root.left, ans))
        right = max(0, self.func(root.right, ans))
        
        # Check if the path passing through the current root as a 'turn' (hook) 
        # is the maximum path found so far.
        ans[0] = max(ans[0], left + right + root.val)
        
        # Return the maximum single path gain this node can offer to its parent
        return max(left, right) + root.val
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize with a very small integer instead of float('-inf') to match your style
        ans = [-int(1e9)] 
        self.func(root, ans)
        return ans[0]