import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Jug = collections.namedtuple('Jug', ('low', 'high'))


def check_feasible(jugs, L, H):
    cache = {}

    def solve_feasible(L,H):
        if (L,H) in cache:
            return cache[(L,H)]
        if L < 0 or H < 0 or L > H:
            return False
        res = False
        for j in jugs:
            if (L <= j.low and j.high <= H) or solve_feasible(L - j.low, H - j.high):
                cache[(L,H)] = True
                return True
        cache[(L,H)] = False
        return False

    return solve_feasible(L,H)


@enable_executor_hook
def check_feasible_wrapper(executor, jugs, l, h):
    jugs = [Jug(*x) for x in jugs]
    return executor.run(functools.partial(check_feasible, jugs, l, h))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "defective_jugs.py", 'defective_jugs.tsv', check_feasible_wrapper))
