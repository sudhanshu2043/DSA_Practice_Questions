class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)  # Dummy head
        self.tail = Node(None, None)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_node(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def remove_last(self):
        if self.head.next == self.tail:
            return None
        last_node = self.tail.prev
        self.remove_node(last_node)
        return last_node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.node_map = {}  # key -> Node
        self.freq_map = {}  # freq -> DoublyLinkedList
    
    def _update_freq(self, node):
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        
        if not self.freq_map[freq].head.next != self.freq_map[freq].tail:
            if self.min_freq == freq:
                self.min_freq += 1
        
        node.freq += 1
        new_freq = node.freq
        
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()
        
        self.freq_map[new_freq].add_node(node)
    
    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        
        node = self.node_map[key]
        self._update_freq(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._update_freq(node)
        else:
            if self.size == self.capacity:
                lfu_list = self.freq_map[self.min_freq]
                node_to_remove = lfu_list.remove_last()
                del self.node_map[node_to_remove.key]
                self.size -= 1
            
            new_node = Node(key, value)
            self.node_map[key] = new_node
            self.min_freq = 1
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].add_node(new_node)
            self.size += 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)