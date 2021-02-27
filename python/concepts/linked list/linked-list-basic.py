"""
Basic linked list structure.

- Single linked list
- Doubly linked list
- Circular linked list
- Linked list with header
- Sorted linked list

Reference:
    -  https://medium.com/@tobby168/%E7%94%A8python%E5%AF%A6%E4%BD%9Clinked-list-524441133d4d
"""


class ListNode:
    """ the data structure of a node. """
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleListedList:
    """ the data structure of a linked list. """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get_size(self):
        """ get the size of linked list. """
        return self.size

    def add(self, item):
        """ add a new element into the linked list. """
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        self.size += 1

    def insert(self, previous_one, item):
        """ insert a new element into the specific node. """
        if not isinstance(item, ListNode):
            item = ListNode(item)

        current_node = self.head
        while current_node is not None:
            if current_node.data == previous_one:
                item.next = current_node.next
                current_node.next = item
            current_node = current_node.next

    def traverse_list(self):
        """ show the linked list. """
        if not self.head:
            return
        
        l = []
        current_node = self.head
        while current_node is not None:
            # print(current_node.data)
            l.append(current_node.data)
            current_node = current_node.next
        return l

    def reverse(self):
        """ reverse the linked list. """
        pass

    def oven_linked_list(self):
        """ get the oven elements for the linked list. """
        pass

    def odd_linked_list(self):
        """ get the odd elements for the linked list. """
        pass


if __name__ == '__main__':
    sll = SingleListedList()
    sll.add(5)
    sll.add(6)
    sll.add(11)
    sll.add(33)
    sll.insert(11, 9)
    print(f'the head: {sll.head.data}, the next data for the head: {sll.head.next.data} the tail: {sll.tail.data}')

    print('the size of linked list: ', sll.get_size())
    res = sll.traverse_list()
    print(f'the linked list: {res}')

