# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        mapp=defaultdict(lambda:defaultdict(list))
        queue.append([root,0,0])
        while queue:
            root,x,y=queue.popleft()
            mapp[x][y].append(root.val)
            if root.left:
                queue.append([root.left,x-1,y+1])
            if root.right:
                queue.append([root.right,x+1,y+1])
        ans=[]
        for x in sorted(mapp):
            temp=[]
            for y in sorted(mapp[x]):
                temp.extend(sorted(mapp[x][y]))
            ans.append(temp)
        return ans