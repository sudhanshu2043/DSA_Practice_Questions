class LRUCache:
    class node:
        def __init__(self,_key,_value):
            self.key=_key
            self.value=_value
            self.next=None
            self.prev=None

    def __init__(self, capacity: int):
        self.cap=capacity
        self.mpp={}
        self.head=self.node(-1,-1)
        self.tail=self.node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head

    def addNode(self,newNode):
        temp=self.head.next
        self.head.next=newNode
        newNode.prev=self.head
        newNode.next=temp
        temp.prev=newNode
        
    def delNode(self,delnode):
        delnext=delnode.next
        delprev=delnode.prev
        delprev.next=delnext
        delnext.prev=delprev

    def get(self, key: int) -> int:
        if key in self.mpp:
            resNode=self.mpp[key]
            res=resNode.value
            del self.mpp[key]
            self.delNode(resNode)
            self.addNode(resNode)
            self.mpp[key]=self.head.next
            return res
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mpp:
            existingNode=self.mpp[key]
            del self.mpp[key]
            self.delNode(existingNode)
        if len(self.mpp)==self.cap:
            del self.mpp[self.tail.prev.key]
            self.delNode(self.tail.prev)
        self.addNode(self.node(key, value))
        self.mpp[key] = self.head.next
            



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)