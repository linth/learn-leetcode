"""
The basic concept of stack.


Reference:
    - https://gist.github.com/travishen/fdb9f9ea4686d9952130b7ce679fe070#%E5%A0%86%E7%96%8A-stack
"""


class Stack(object):
    """ the stack implementation. """
    def __init__(self, inital_data):
        self.stack = []
        self.initial_data = inital_data

        if isinstance(inital_data, Iterable):
            self.stack = list(inital_data)
        else:
            raise NotImplementedError('Inital with not iterable object.')

    # def __repr__(self):
    #     return self.initial_data

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, i):
        return self.stack[i]

    @property
    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if not self.stack.is_empty():
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]


if __name__ == '__main__':
    s = [3, 4, 5]
    s.append(6)
    s.append(7)

    print(s)
    s.pop()
    s.pop()
    print(s)
