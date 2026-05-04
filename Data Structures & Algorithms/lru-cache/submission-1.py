class LRUCache:
    class LinkedList:
        def __init__(self, key = 0, val = 0, nxt = None, prev = None):
            self.key = key
            self.val = val
            self.nxt = nxt
            self.prev = prev
        def insert_back(self, node):
            temp = self.prev
            temp.nxt = node
            node.prev = temp
            node.nxt = self
            self.prev = node
        def remove(self):
            self.prev.nxt = self.nxt
            self.nxt.prev = self.prev

    def __init__(self, capacity: int):
        self.sentinel = self.LinkedList()
        self.sentinel.nxt = self.sentinel
        self.sentinel.prev = self.sentinel
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            if key == 1:
                print(self.cache)
            node = self.cache[key]
            node.remove()
            self.sentinel.insert_back(node)
            return node.val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.capacity:
                self.capacity -= 1
                
            else: 
                old_key = self.sentinel.nxt.key
                self.sentinel.nxt = self.sentinel.nxt.nxt
                self.sentinel.nxt.prev = self.sentinel
                self.cache.pop(old_key)
            
            newNode = self.LinkedList(key,value)
            self.cache[key] = newNode
            self.sentinel.insert_back(newNode)
        else:
            node = self.cache[key]
            node.remove()
            node.val = value
            self.sentinel.insert_back(node)

             
