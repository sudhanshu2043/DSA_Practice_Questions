# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0   # global maximum sum

        def dfs(node):
            if not node:
                # For null nodes: valid BST with sum=0, min=+inf, max=-inf
                return True, 0, float('inf'), float('-inf')

            left_isBST, left_sum, left_min, left_max = dfs(node.left)
            right_isBST, right_sum, right_min, right_max = dfs(node.right)

            # Check BST property
            if left_isBST and right_isBST and left_max < node.val < right_min:
                total_sum = left_sum + right_sum + node.val
                self.maxi = max(self.maxi, total_sum)
                return True, total_sum, min(left_min, node.val), max(right_max, node.val)
            else:
                # Not a BST
                return False, 0, 0, 0

        dfs(root)
        return self.maxi
