# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def __init__(self):
        self.maxi = 0  # Store max sum of any BST in the tree

    def validate(self, node, low=-float('inf'), high=float('inf')) -> bool:
        """Check if a subtree is a valid BST."""
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        return self.validate(node.left, low, node.val) and self.validate(node.right, node.val, high)

    def dfs(self, root):
        """DFS traversal that calculates the sum of valid BST subtrees."""
        if root is None:
            return 0, True, float('inf'), -float('inf')  # Sum, IsBST, Min, Max

        left_sum, is_left_bst, left_min, left_max = self.dfs(root.left)
        right_sum, is_right_bst, right_min, right_max = self.dfs(root.right)

        # Check if current subtree is BST
        if is_left_bst and is_right_bst and left_max < root.val < right_min:
            curr_sum = left_sum + right_sum + root.val
            self.maxi = max(self.maxi, curr_sum)
            return curr_sum, True, min(root.val, left_min), max(root.val, right_max)
        else:
            return 0, False, 0, 0  # If not BST, return 0 as sum

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        """Returns the maximum sum of any BST subtree."""
        self.dfs(root)
        return self.maxi
