class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.size =0
    def append(self, data):
        self.size += 1
        #Encapsulate the data in a Node
        node = Node(data)
            
        if self.head.next == None:
            self.head = node
        else:
            self.tail = node
            self.head = node
            current = self.tail
            while current.next:
                current = current.next
            current.next = node
    def size(self):
        count =0
        current = self.tail
        while current:
            count += 1
            current = current.next
        return count
    def iter(self):
        current =self.tail
        while current:
            val = current.next
            yield val
    
