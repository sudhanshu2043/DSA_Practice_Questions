# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1 for _ in range(n)] for _ in range(m)]
        array = []
        while head:
            array.append(head.val)
            head = head.next
        size = len(array)
        t,b,l,r = 0,m-1,0,n-1
        idx = 0

        while t <= b and l <= r and idx < size:
            for i in range(l,r+1):
                if idx < size:
                    mat[t][i] = array[idx]
                    idx += 1
            t += 1
            for i in range(t,b+1):
                if idx < size:
                    mat[i][r] = array[idx]
                    idx += 1
            r -= 1
            if t <= b:
                for i in range(r,l-1,-1):
                    if idx < size:
                        mat[b][i] = array[idx]
                        idx += 1
                b -= 1
            if l <= r:
                for i in range(b,t-1,-1):
                    if idx < size:
                        mat[i][l] = array[idx]
                        idx += 1
                l += 1

        return mat

        