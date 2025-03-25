# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append([root,0])
        if root.left==None and root.right==None:
            return 1
        width=1
        while q:
            size=len(q)
            mini=q[0][1]
            fInd,LInd=0,0
            for i in range(size):
                node,currInd=q.popleft()
                if i==0: fInd=currInd
                if i==(size-1): LInd=currInd
                if node.left:
                    q.append([node.left,currInd*2+1])
                if node.right:
                    q.append([node.right,currInd*2+2])
            width=max(width,LInd-fInd+1)
        return width