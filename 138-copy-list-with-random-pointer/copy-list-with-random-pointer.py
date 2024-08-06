"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def insertCopyInBetween(self, head):
        temp = head
        while temp:
            nextElement = temp.next
            copy = Node(temp.val)
            copy.next = nextElement
            temp.next = copy
            temp = nextElement

    def connectRandomPointers(self, head):
        temp = head
        while temp:
            copyNode = temp.next
            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None
            temp = temp.next.next

    def getDeepCopyList(self, head):
        temp = head
        dummyNode = Node(-1)
        res = dummyNode
        while temp:
            res.next = temp.next
            res = res.next
            temp.next = temp.next.next
            temp = temp.next
        return dummyNode.next

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        self.insertCopyInBetween(head)
        self.connectRandomPointers(head)
        return self.getDeepCopyList(head)