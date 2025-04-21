# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummyless=ListNode()
        dummygreEq=ListNode()
        ans=dummyless
        GreEqStart=dummygreEq
        temp=head
        while temp!=None:
            if temp.val<x:
                dummyless.next=temp
                dummyless=dummyless.next
            else:
                dummygreEq.next=temp
                dummygreEq=dummygreEq.next
            temp=temp.next
        dummyless.next=GreEqStart.next
        dummygreEq.next=None
        return ans.next