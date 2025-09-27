# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # An empty tree is a subtree of any tree.
        if not subRoot:
            return True
        # An empty tree cannot contain a non-empty subtree.
        if not root:
            return False

        # Check if the tree starting at the current 'root' is identical to 'subRoot'.
        if self.isSameTree(root, subRoot):
            return True

        # If not, check if 'subRoot' is a subtree of the left or right child.
        # The 'or' is key: we only need to find it in one of them.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are identical.

        # If both nodes are None, they are the same.
        if not p and not q:
            return True
        
        # If one of the nodes is None, or their values are different, they are not the same.
        if not p or not q or p.val != q.val:
            return False
            
        # Recursively check if both the left and right subtrees are also identical.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)