import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
    small, big = A[0], A[0]
    for i in range(1, len(A), 2):
        if A[i - 1] <= A[i]:
            left = A[i - 1]
            right = A[i]
        else:
            left = A[i]
            right = A[i - 1]
        if left <= small:
            small = left
        if right >= big:
            big = right

    if len(A) % 2 == 1:
        small = min(A[-1], small)
        big = max(A[-1], big)


    return MinMax(small, big)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
