"""
Queue with linked list.

Reference:
    - https://www.geeksforgeeks.org/queue-linked-list-implementation/
"""


class Node:
    def __init__(self, data):
        """ the data structure of a node. """
        self.data = data
        self.next = None

    
class Queue:
    """ use linked list to implement the class of queue. """
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self) -> bool:
        return self.front == None

    def enqueue(self, item):
        if not isinstance(item, Node):
            temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return self
        self.rear.next = temp
        self.rear = temp
        return self

    def dequeue(self) -> None:
        if self.is_empty():
            return
        
        # delete the front of queue.
        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def traverse_list(self):
        temp = self.front

        l = []
        while temp is not None:
            print(temp.data)
            l.append(temp.data)
            temp = temp.next
        return l


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.dequeue()
    q.enqueue(2)
    print(q.front.data, q.rear.data)

    res = q.traverse_list()
    print('the result = ', res)
