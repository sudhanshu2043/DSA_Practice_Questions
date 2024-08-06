# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateArray(self, arr, k):
        n = len(arr)
        k = k % n
        arr[:] = arr[-k:] + arr[:-k]
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # Convert linked list to array
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        # Rotate array
        self.rotateArray(arr, k)
        
        # Convert array back to linked list
        dummy_node = ListNode(-1)
        temp = dummy_node
        for val in arr:
            temp.next = ListNode(val)
            temp = temp.next
        
        return dummy_node.next
