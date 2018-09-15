from test_framework import generic_test
from test_framework.test_failure import TestFailure


class my_linked_list:
    def __init__(self, isbn = None, price = None, left = None, right = None):
        self.price = price
        self.isbn = isbn
        self.left = left
        self.right = right

    def connect_left_right_to_each_other(self):
        if self.left is not None and self.right is not None:
            l = self.left
            r = self.right
            l.right = r
            r.left = l

    def add_self_to_left_of_node(self, node):
        if node.left:
            original_l = node.left
            original_l.right = self
            self.left = original_l
            node.left = self
            self.right = node
        else:
            self.left = node
            self.right = node
            node.left = self
            node.right = self
    def __repr__(self):
        return "ISBN: %d val: %d" % (self.isbn, self.price)
class linked_queue:
    def __init__(self, capacity):
        self._head = None
        self._hm = {}
        self.capacity = capacity

    def dequeue(self, isbn):
        if isbn not in self._hm:
            return False
        node = self._hm[isbn]
        if self._head is node:
            if node.right is node:
                self._head = None
            else:
                self._head = node.right
        node.connect_left_right_to_each_other()
        self._hm.pop(isbn)
        return True

    def enqueue(self, isbn, price):
        if isbn in self._hm:
            if self._head is not self._hm[isbn]:
                node = self._hm[isbn]
                node.connect_left_right_to_each_other()
                node.add_self_to_left_of_node(self._head)
        else:

            if len(self._hm) == self.capacity:
                if self.capacity == 1:
                    self.dequeue(self._head.isbn)
                else:
                    oldest = self._head.left
                    self.dequeue(oldest.isbn)
            new_node = my_linked_list(isbn, price)
            self._hm[isbn] = new_node
            if self._head:
                new_node.add_self_to_left_of_node(self._head)
        self._head = self._hm[isbn]

    def get_key(self, key):
        return self._hm.get(key)


class LruCache:
    def __init__(self, capacity):
        self._hashtable = {}
        self._queue = linked_queue(capacity)
        return

    def lookup(self, isbn):

        if isbn in self._queue._hm:
            price = self._queue.get_key(isbn).price
            self._queue.dequeue(isbn)
            self._queue.enqueue(isbn,price)
            return price
        return -1

    def insert(self, isbn, price):
        self._queue.enqueue(isbn, price)
        return

    def erase(self, isbn):
        return self._queue.dequeue(isbn)

def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
