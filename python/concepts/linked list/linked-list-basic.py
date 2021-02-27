"""
Basic linked list structure.

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

    def add(self, item) -> None:
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def traverse_list(self):
        pass

    def reverse(self):
        pass

    def oven_linked_list(self):
        pass

    def odd_linked_list(self):
        pass


if __name__ == '__main__':
    sll = SingleListedList()
    sll.add(5)
    sll.add(6)
    sll.add(11)
    sll.add(33)
    print(f'the head: {sll.head.data}, the next data for the head: {sll.head.next.data} the tail: {sll.tail.data}')

