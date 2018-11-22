from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque


class QueueWithMax:
    def __init__(self):
        self.q = deque()
        self.s = deque()

    def enqueue(self, x):
        self.q.append(x)
        while self.s and self.s[-1] < x:
            self.s.pop()
        self.s.append(x)

    def dequeue(self):
        x = self.q.popleft()
        if x == self.s[0]:
            self.s.popleft()

        return x
    def max(self):
        return self.s[0]

    def __repr__(self):
        return f"Raw queue: {self.q} \n Queue with maxes: {self.possible_maxes_q}"
def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
