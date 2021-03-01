"""
implement the queue and stack with linked list.
"""


class Node:
    """ the data structure of node. """
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue(object):
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None and self.rear is None

    def enqueue(self, item):
        if not isinstance(item, Node):
            item = Node(item)

        if self.rear is None:
            self.front = self.rear = item
            return
        self.rear.next = item
        self.rear = item

    def dequeue(self):
        if self.is_empty():
            return

        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def traverse(self):
        temp = self.front

        while temp is not None:
            print(temp.data)
            temp = temp.next


class Stack(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.head == 0

    def push(self, item):
        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
        else:
            item.next = self.head
            self.head = item
        self.size += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            self.head = self.head.next
            self.size -= 1

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def traverse(self):
        temp = self.head

        while temp is not None:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':

    s = Stack()
    s.push(1)
    s.push(3)
    s.push(7)
    s.push(8)
    # print(s.head.data)
    s.pop()
    # print(s.head.data)
    # s.pop()
    # s.pop()
    # print(s.head.data) # cannot be used.
    s.traverse()
    print('the size of stack = ', s.size)

    print('###############################')
    q = Queue()
    q.enqueue(2)
    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(15)
    q.dequeue()
    q.dequeue()
    q.traverse()



