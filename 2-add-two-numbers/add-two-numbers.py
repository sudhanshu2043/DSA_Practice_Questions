# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> \
     Optional[ListNode]:
        temp=ListNode()
        ans=temp
        carry=0
        while l1 and l2:
            sum=l1.val+l2.val+carry
            temp.next=ListNode(sum%10)
            carry=sum//10
            temp=temp.next
            l1=l1.next
            l2=l2.next
        # if l1 have some element left
        while l1:
            sum=carry+l1.val
            temp.next=ListNode(sum%10)
            carry=sum//10
            l1=l1.next
            temp=temp.next
        # if l2 have some element left
        while l2:
            sum=carry+l2.val
            temp.next=ListNode(sum%10)
            carry=sum//10
            temp=temp.next
            l2=l2.next
        if carry>0:
            temp.next=ListNode(carry)
            temp=temp.next
        temp.next=None
        return ans.next


