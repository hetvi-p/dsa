class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DLL:

    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addEnd(self, endNode: Node) -> Node:
        endNode.next = self.tail
        endNode.prev = self.tail.prev
        self.tail.prev.next = endNode
        self.tail.prev = endNode
        return self.tail.prev

    def popLeft(self) -> int:
        front = self.head.next
        self.head.next = front.next
        self.head.next.prev = self.head
        return front.key

    def removeNode(self, remove: Node) -> None:
        remove.prev.next = remove.next
        remove.next.prev = remove.prev
        return None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DLL()
        self.size = 0
        self.map = {}
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        
        value = node.value

        self.dll.removeNode(node)
        addedNode = self.dll.addEnd(node)
        self.map[key] = addedNode

        return value


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.dll.removeNode(node)
            self.dll.addEnd(node)
            return None 

        if self.size >= self.capacity:
            removedKey = self.dll.popLeft()
            self.size -= 1
            del self.map[removedKey]
        
        node = Node(key, value)
        keyNode = self.dll.addEnd(node)
        self.map[key] = keyNode
        self.size += 1

        return None




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


