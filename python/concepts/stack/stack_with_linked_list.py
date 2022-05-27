"""
implement the stack with linked list.

Reference:
    - https://www.geeksforgeeks.org/stack-in-python/?ref=lbp
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:

    def __init__(self):
        self.head = Node('head')
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        """ get the top item of the stack. """
        if self.is_empty():
            raise Exception('peeking from an empty stack.')
        return self.head.next.val

    def push(self, val):
        """ push a value into the stack. """
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        """ remove a value from the stack and return. """
        if self.is_empty():
            raise Exception('popping from an empty stack.')

        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.val

if __name__ == '__main__':
    stack = Stack()

    for i in range(1, 11):
        stack.push(i)

    print(f'Stack: {stack}')

    for _ in range(1, 6):
        remove = stack.pop()
        print(f'Pop: {remove}')
    print(f'Stack: {stack}')

    