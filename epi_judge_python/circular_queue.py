from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        self.arr = [None for x in range(capacity)]
        self.capacity = capacity
        self._size = 0
        self.head = 0
        self.tail = 0
        return

    def enqueue(self, x):
        if self._size == self.capacity:
            new_arr = [None for x in range(2 * len(self.arr))]
            new_arr[:len(self.arr)] = self.arr[self.head:] + self.arr[:self.head]
            self.arr = new_arr
            self.head = 0
            self.tail = self._size - 1
            self.capacity = len(self.arr)

        if self._size == 0:
            self.arr[self.head] = x
            self._size += 1
            return

        if self.head == 0:
            self.head = self.capacity - 1
        else:
            self.head -= 1
        self._size += 1
        self.arr[self.head] = x
        return

    def dequeue(self):
        if self._size == 0:
            raise ValueError("empty queue")

        val = self.arr[self.tail]
        self._size -= 1
        self.arr[self.tail] = None
        if self._size > 0:
            if self.tail == 0:
                self.tail = self.capacity - 1
            else:
                self.tail -= 1
        return val

    def size(self):
        return self._size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
