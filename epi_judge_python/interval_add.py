import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals, new_interval):
    i, res = 0, []
    added_new_interval = False
    for interval in disjoint_intervals:
        if interval.right < new_interval.left:
            res.append(interval)
        elif interval.left > new_interval.right:
            if not added_new_interval:
                added_new_interval = True
                res.append(new_interval)
            res.append(interval)
        else:
            new_interval = Interval(min(interval.left, new_interval.left), max(interval.right, new_interval.right))
    if not added_new_interval:
        res.append(new_interval)
    return res


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            'interval_add.tsv',
            add_interval_wrapper,
            res_printer=res_printer))
