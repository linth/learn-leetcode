'''
Design an LRU cache

Reference:
    - https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/lru_cache/lru_cache.ipynb
'''

class Node(object):
    
    def __init__(self, results):
        self.results = results
        self.prev = None
        self.next = None


class LinkedList(object):
    pass

