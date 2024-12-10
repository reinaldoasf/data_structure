class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_prev(self,value):
        newNode = Node(value)
        newNode.next = self.head
        if self.head:
            self.head.prev = newNode
        else:
            self.tail = newNode
        self.head = newNode
    
    def add_front(self,value):
        newNode = Node(value)
        newNode.prev = self.tail
        if self.tail:
            self.tail.next = newNode
        else:
            self.head = newNode
        self.tail = newNode

    def pop_head(self):
        if not self.head:
            return None
        removedValue = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def pop_tail(self):
        if not self.tail:
            return None
        removedValue = self.head.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None

    def __repr__(self):
        iterator = self.head
        currString = ""
        while iterator.next:
            currString += f"{iterator.value}->"
            iterator = iterator.next
        currString += str(iterator.value)
        return currString
    

if __name__ == '__main__':
    linkedList = DoublyLinkedList()
    linkedList.add_front(2)
    linkedList.add_front(6)
    linkedList.add_prev(1)
    linkedList.add_front(9)
    print(linkedList)
    linkedList.pop_head()
    linkedList.pop_tail()
    linkedList.pop_tail()
    print(linkedList)