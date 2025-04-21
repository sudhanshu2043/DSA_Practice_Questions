# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        length = 0
        current = head
        
        # First pass: find length
        while current:
            length += 1
            current = current.next
        
        # Second pass: remove (length - n)th node
        current = dummy
        for _ in range(length - n):
            current = current.next
        
        current.next = current.next.next
        return dummy.next
