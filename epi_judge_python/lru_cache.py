from test_framework import generic_test
from test_framework.test_failure import TestFailure


class DoublyLinkedList:
    def __init__(self, k, v, l = None, r = None):
        self.l = l
        self.r = r
        self.k = k
        self.v = v
    def __repr__(self):
        return str(self.k) + " " + str(self.v)
class EnhancedLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.size = 0
        self.LEFT = DoublyLinkedList(None, None)
        self.RIGHT = DoublyLinkedList(None, None)
        self.LEFT.r = self.RIGHT
        self.RIGHT.l = self.LEFT

    def move_to_newest(self, node):
        old_l, old_r = node.l, node.r
        old_l.r = old_r
        old_r.l = old_l

        new_l = self.RIGHT.l
        new_r = self.RIGHT
        node.l, node.r = new_l, new_r
        new_l.r, new_r.l = node, node

    def remove(self, k):
        if k in self.dict:
            node =  self.dict[k]
            self.size -= 1
            old_l, old_r = node.l, node.r
            old_l.r, old_r.l = old_r, old_l
            del self.dict[k]

            del node
            return True
        else:
            return False

    def remove_oldest(self):
        k = self.LEFT.r.k
        self.remove(k)
        return k


    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.move_to_newest(node)
            return node.v
        else:
            return -1

    def add(self, key, v):
        if key in self.dict:
            node = self.dict[key]
            self.move_to_newest(node)
            return
        else:
            if self.size == self.capacity:
                self.remove_oldest()
            self.size += 1
            new_l, new_r = self.RIGHT.l, self.RIGHT
            node = DoublyLinkedList(key, v, new_l, new_r)
            new_l.r, new_r.l = node, node
            self.dict[key] = node

class LruCache:
    def __init__(self, capacity):
        self.d = EnhancedLinkedList(capacity)
        return

    def lookup(self, isbn):

        return self.d.get(isbn)

    def insert(self, isbn, price):
        self.d.add(isbn, price)
        return

    def erase(self, isbn):
        return self.d.remove(isbn)

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
