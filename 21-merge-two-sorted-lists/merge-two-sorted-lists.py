# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        ans=dummy
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                dummy.next=list1
                list1=list1.next
            else:
                dummy.next=list2
                list2=list2.next
            dummy=dummy.next
        # some element left in list1
        while list1!=None:
            dummy.next=list1
            list1=list1.next
            dummy=dummy.next
        # some element left in list2
        while list2!=None:
            dummy.next=list2
            list2=list2.next
            dummy=dummy.next
        dummy.next=None
        return ans.next

