import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):
    intervals.sort(key= lambda x: (x.left.val, 0 if x.left.is_closed else 1))
    res = [intervals[0]]

    for i in range(1, len(intervals)):
        x = intervals[i]

        prev = res[-1]
        if (x.left.val == prev.right.val and (prev.right.is_closed or x.left.is_closed)) or x.left.val < prev.right.val:
            if prev.left.val == x.left.val:
                left_end = Endpoint(prev.left.is_closed or x.left.is_closed, x.left.val)
            else:
                left_end = prev.left
            if x.right.val < prev.right.val:
                right_end = prev.right
            elif x.right.val > prev.right.val:
                right_end = x.right
            else:
                right_end = Endpoint(x.right.is_closed or prev.right.is_closed, x.right.val)

            res[-1] = Interval(left_end, right_end)
        else:
            res.append(x)
    return res


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
