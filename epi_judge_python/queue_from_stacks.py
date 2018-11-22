from test_framework import generic_test


class Queue:
    def __init__(self):
        self.main_stack, self.secondary_stack = [], []
    def enqueue(self, x):
        self.main_stack.append(x)

    def dequeue(self):
        if not self.main_stack and not self.secondary_stack:
            raise IndexError("empty")
        if not self.secondary_stack:
            while self.main_stack:
                self.secondary_stack.append(self.main_stack.pop())
        return self.secondary_stack.pop()


def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
