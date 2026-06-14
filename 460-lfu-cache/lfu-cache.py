from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        # key -> (value, frequency)
        self.key_map = {}
        # frequency -> OrderedDict(key -> True)
        # OrderedDict maintains insertion order, behaving like a Doubly Linked List
        self.freq_map = defaultdict(OrderedDict)

    def _update_frequency(self, key: int, value: int = None) -> int:
        """Helper to advance a key's frequency and move its position in O(1)"""
        curr_val, freq = self.key_map[key]
        # If a new value is provided (from a put operation), update it
        if value is not None:
            curr_val = value
        # 1. Remove the key from its current frequency bucket
        del self.freq_map[freq][key]
        
        # 2. If this bucket became empty and it was the global minimum frequency, increment min_freq
        if not self.freq_map[freq] and freq == self.min_freq:
            self.min_freq += 1
            del self.freq_map[freq]
            
        # 3. Insert the key into the incremented frequency bucket (moves to the end/most recent)
        new_freq = freq + 1
        self.freq_map[new_freq][key] = True
        self.key_map[key] = (curr_val, new_freq)
        
        return curr_val

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        return self._update_frequency(key)

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        # Scenario A: Key already exists, update its value and elevate its frequency
        if key in self.key_map:
            self._update_frequency(key, value)
            return

        # Scenario B: Cache is full, evict the LFU (and LRU if tied) element first
        if len(self.key_map) >= self.cap:
            # The first item in an OrderedDict is the oldest inserted (the tail of our DLL concept)
            evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.key_map[evict_key]
            
            if not self.freq_map[self.min_freq]:
                del self.freq_map[self.min_freq]

        # Scenario C: Insert the completely new element
        self.key_map[key] = (value, 1)
        self.freq_map[1][key] = True
        self.min_freq = 1  # Reset min_freq to 1 since a brand new item has just entered