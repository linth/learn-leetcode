"""
implement the queue and stack with array.
"""


class Queue(object):
    """ implement the queue class with array. """
    def __init__(self, input_data):
        self.queue = []
        self.input_data = input_data

        if isinstance(input_data, list):
            self.queue = input_data
        else:
            raise NotImplementedError('the input_data is not iterable.')

    def is_empty(self):
        """
        check the queue is empty or not.
        :return:
        """
        return len(self.queue) == 0

    def enqueue(self, data):
        """
        add an element into the queue.
        :param data:
        :return:
        """
        self.queue.append(data)

    def dequeue(self):
        """
        delete an oldest element in the queue. in case, the oldest element is the first one.
        :return:
        """
        self.queue.pop(0)

    def peek(self):
        """
        watch the value of the oldest element.
        :return:
        """
        return self.queue[0]


class Stack(object):
    """ implement the stack class with array. """
    def __init__(self, input_data):
        self.stack = []
        self.input_data = input_data

        if isinstance(input_data, list):
            self.stack = input_data
        else:
            raise NotImplementedError('the input_data is not iterable.')

    def is_empty(self):
        """
        check the stack is empty or not.
        :return:
        """
        return len(self.stack) == 0

    def push(self, data):
        """
        add an element into the stack.
        :param data:
        :return:
        """
        self.stack.append(data)

    def pop(self):
        """
        delete a last element in the stack. in case, the last is last one.
        :return:
        """
        if not self.is_empty():
            self.stack.pop()

    def peek(self):
        """
        watch the value of the last element.
        :return:
        """
        return self.stack[-1]

