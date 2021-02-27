"""
The basic concept of queue.

Reference:
    - https://gist.github.com/travishen/fdb9f9ea4686d9952130b7ce679fe070#%E4%BD%87%E5%88%97-queue
"""


class Queue(object):
    """ the queue implementation. """
    def __init__(self, initial_data):
        self.queue = []
        self.initial_data = initial_data

        if isinstance(initial_data, list):
            self.queue = list(initial_data)
        else:
            raise NotImplementedError('Initial with not iterable object.')

    # def __repr__(self):
    #     return 'the initial_data = ' + self.initial_data

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        return self.queue.append(data())

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]


if __name__ == '__main__':
    arr = [1, 2, 6, 8, 11]
    q = Queue(arr)
    print(q.__len__())

    q.dequeue()
    print(q.queue)