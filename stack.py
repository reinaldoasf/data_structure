class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self,item):
        self._size +=1
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self._size == 0:
            raise IndexError("Empty Stack.")
        old_top = self.top
        self.top = self.top.next
        self._size -=1

        return old_top.value
    
    def peek(self):
        if self._size == 0:
            raise IndexError("Empty Stack.")
        return self.top.value
    
    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size

if __name__ == '__main__':
    test_stack = Stack()
    test_stack.push(1)
    test_stack.push(3)
    test_stack.push(2)
    print(test_stack.pop())
    print(test_stack.peek())
    print(test_stack.size())
    print(test_stack.pop())
    print(test_stack.is_empty())
    print(test_stack.pop())
    print(test_stack.is_empty())